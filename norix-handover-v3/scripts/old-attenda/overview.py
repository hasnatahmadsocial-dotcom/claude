import re, json
def u16(s): return len(s.encode('utf-16-le'))//2
LINK = re.compile(r'\*\*(.+?)\*\*|\[(.+?)\]\((.+?)\)')
def parse(md):
    out='';bolds=[];links=[];pos=0
    for m in LINK.finditer(md):
        out+=md[pos:m.start()]
        if m.group(1) is not None:
            s=u16(out); out+=m.group(1); bolds.append((s,u16(out)))
        else:
            s=u16(out); out+=m.group(2); links.append((s,u16(out),m.group(3)))
        pos=m.end()
    out+=md[pos:]
    return out,bolds,links
STYLE={'h1':'HEADING_1','h2':'HEADING_2','h3':'HEADING_3'}
def build(tab, paras):
    texts=[];rs=[];rt=[];lists=[];idx=1;cur=None
    for kind,md in paras:
        t,b,l=parse(md); full=t
        start=idx; end=idx+u16(full)+1; off=start
        if kind in STYLE:
            rs.append({"updateParagraphStyle":{"range":{"startIndex":start,"endIndex":end,"tabId":tab},"paragraphStyle":{"namedStyleType":STYLE[kind]},"fields":"namedStyleType"}})
        for s,e in b:
            rt.append({"updateTextStyle":{"range":{"startIndex":off+s,"endIndex":off+e,"tabId":tab},"textStyle":{"bold":True},"fields":"bold"}})
        for s,e,u in l:
            ln={"tabId":u[1:]} if u.startswith('#') else {"url":u}
            rt.append({"updateTextStyle":{"range":{"startIndex":off+s,"endIndex":off+e,"tabId":tab},"textStyle":{"link":ln},"fields":"link"}})
        if kind in ('b1','n1'):
            preset='NUMBERED_DECIMAL_ALPHA_ROMAN' if kind=='n1' else 'BULLET_DISC_CIRCLE_SQUARE'
            if cur and cur['preset']==preset and cur['end']==start: cur['end']=end
            else: cur={'preset':preset,'start':start,'end':end}; lists.append(cur)
        else: cur=None
        texts.append(full); idx=end
    reqs=[{"insertText":{"location":{"index":1,"tabId":tab},"text":'\n'.join(texts)}}]+rs+rt
    for L in sorted(lists,key=lambda x:-x['start']):
        reqs.append({"createParagraphBullets":{"range":{"startIndex":L['start'],"endIndex":L['end']-1,"tabId":tab},"bulletPreset":L['preset']}})
    return reqs
tabs=[l.split() for l in open('tabs.txt') if l.strip()]
tid={int(a):b for a,b in tabs}
names=["ATN101 / ATN103: Platform Bed","ATN120 / ATN130 / ATN150: Space-Saver Bed","ATN140 / ATN145: Sleigh Bed","ATN250 / ATN255: Nightstand","ATN301: Three Shelf Storage Unit","ATN310: Wall-Mounted Bookshelf","ATN320: Two Shelf Storage Unit","ATN401: Four Shelf Storage Unit","ATN500: Floor-Mount Stool","ATN601: Floor-Mount Desk","ATN620 / ATN621 / ATN625: Wall-Mounted Desk","ATN700 / ATN750: Open Chest","ATN800 / ATN801: Wardrobe"]
P=[('h1','Norix Attenda Series: Product Page Updates'),
('p','This doc covers the 13 Norix Attenda products assigned on 10/31, with 34 variants in total. Each product has its own tab.'),
('h2','What Each Tab Includes'),
('b1','Recommended H1 and subtitle, with the current versions for comparison'),
('b1','Revised product description, with on-page H2 headings marked [H2]'),
('b1','Meta title and description'),
('b1','Notes and questions for your review'),
('h2','Changes Applied to All Attenda Pages'),
('b1',f'**Series section:** a new "About Norix Attenda Molded Bedroom Series" section, the same on every tab. Please review it on the [ATN601 Floor-Mount Desk tab](#{tid[9]}).'),
('b1','**Weights and dimensions:** taken from the current Norix spec sheets. Where the price list or your current page differs, it is noted in that tab.'),
('b1','**Variant weights:** almost all variants are set to 255 lbs in Shopify. Accurate weights are listed in each tab.'),
('b1','**Links:** collection links only, with no links to individual products.'),
('b1','**Images:** 11 of the 13 pages have more than 5 images. Each tab suggests which photos to remove.'),
('h2','Products in This Doc')]
for i,n in enumerate(names): P.append(('n1',f'[{n}](#{tid[i]})'))
P+=[('h2','Store Issues Found'),
('b1','**Platform Bed:** two variants are named "ATN101B." SKU N700186-03 looks like it should be ATN103B.'),
('b1','**Space-Saver Bed:** the ATN130 and ATN133 variants are named "Standard Bed," but the ATN130 is the bed with storage.'),
('b1','**Sleigh Bed:** two variants share SKU N700215-02, and the two drainage-hole variants are set to 0 lbs.'),
('b1','**Two Shelf Storage Unit:** the variant is named "ATN301," and the current description says "3-compartment."'),
('b1','**Open Chest:** the current description is written for the wall desk.'),
('b1','**Norix sources:** spec sheet typos (ATN320, ATN500, ATN700) and the reversed wall desk weights in the price list are noted in those tabs.')]
txt='\n'.join(t for _,t in P)
assert '—' not in txt
json.dump(build('t.0',P),open('req_ov.json','w'))
print(json.dumps(build('t.0',P),separators=(',',':')))
