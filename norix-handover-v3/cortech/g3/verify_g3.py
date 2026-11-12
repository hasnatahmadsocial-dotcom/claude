import json,sys
exec(open('mc3.py').read().split("if __name__")[0])
doc=json.load(open(sys.argv[1]))['content']
ids=open('ids3.txt').read().split()
tabs={t['tabProperties']['title']:t for t in doc['tabs']}
sty={'h1':'HEADING_1','h2':'HEADING_2','h3':'HEADING_3'}
allok=True
for d,tid in zip(P,ids):
    t=tabs.get(d['tab']); title=d['tab']
    if t is None: print('MISSING TAB:',d['tab']); allok=False; continue
    want=content(d)
    paras=[e['paragraph'] for e in t['documentTab']['body']['content'] if 'paragraph' in e]
    got=[]
    for p in paras:
        txt=''.join(x.get('textRun',{}).get('content','') for x in p['elements']).rstrip('\n')
        bold=''.join('**'+x['textRun']['content'].rstrip('\n')+'**' if x.get('textRun',{}).get('textStyle',{}).get('bold') else x.get('textRun',{}).get('content','') for x in p['elements']).rstrip('\n')
        links=[x['textRun']['textStyle']['link']['url'] for x in p['elements'] if 'link' in x.get('textRun',{}).get('textStyle',{})]
        got.append((p['paragraphStyle'].get('namedStyleType'),'bullet' in p,txt,bold.replace('****',''),links))
    if got and got[-1][2]=='': got=got[:-1]
    errs=[]
    if title!=d['tab']: errs.append('TITLE')
    if len(got)!=len(want): errs.append(f'COUNT {len(got)} vs {len(want)}')
    import re
    for (k,md),(st,bul,txt,bold,links) in zip(want,got):
        plain,b,l=parse(md)
        if txt!=plain: errs.append('TEXT:'+plain[:60]+' || '+txt[:60])
        if st!=sty.get(k,'NORMAL_TEXT'): errs.append('STYLE:'+plain[:40])
        if bul!=(k in('b1','n1')): errs.append('BULLET:'+plain[:40])
        wb=re.sub(r'\[([^\]]+)\]\([^)]+\)',r'\1',md)
        if bold!=wb: errs.append('BOLD:'+plain[:40])
        wl=re.findall(r'\]\(([^)]+)\)',md)
        if [x for x in links]!=[u for u in wl for _ in [0]] and sorted(set(links))!=sorted(set(wl)): errs.append('LINK:'+plain[:40])
    print(title,'|',len(got),'paras |','OK' if not errs else errs[:6]); allok&=not errs
print('ALL OK' if allok else 'PROBLEMS')
