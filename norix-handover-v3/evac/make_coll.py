import json,re,sys
exec(open('../scripts/doc-builder/build3.py').read())
exec(open('collection_draft.py').read())
KW=('**Keywords (Ricky\'s sheet):** Primary: evacuation chair (600/mo). Secondary: evac chair (500), evacuation chairs for stairs (150), '
    'emergency evacuation chair (100), stair evacuation chair (90), emergency stair chair (90), evacuation wheelchair (80), evacuation sled (80), '
    'rescue chair (50). Ricky\'s note: keep stair evacuation chair and emergency evacuation chair on this page; the collection also covers rescue stretcher (200).')
c=[('h1','Collection: Evacuation Chairs and Rescue Stretchers'),
   ('p',f'**Collection URL:** [{URL}]({URL})'),
   ('p',KW),
   ('h2','Recommended H1'),
   ('p',f'**H1 (collection title):** {h1}'),
   ('p',f'**Current H1:** {cur_h1}'),
   ('h2','Revised Collection Description'),
   ('p','Headings marked [H2] should be set as H2 on the page.')]
for k,t in body:
    c.append(('h3','[H2] '+t) if k=='h2' else ('b1',t) if k=='b' else ('p',t))
c+=[('h2','Meta Title and Description'),
    ('p',f'**Meta title ({len(mt)} characters):** {mt}'),
    ('p',f'**Current meta title ({len(cur_mt)} characters):** {cur_mt}'),
    ('p',f'**Meta description ({len(md)} characters):** {md}'),
    ('p',f'**Current meta description ({len(cur_md)} characters):** {cur_md}'),
    ('h2','Notes and Questions')]+[('n1',n) for n in notes]
# process tab (written out, single-level lists so numbering stays intact)
P=[('h1','Process: How I Optimize a Page with Keywords'),
 ('n1','**Keywords (Ricky\'s sheet):** take the primary keyword, secondary keywords and Ricky\'s note for the page. The primary goes in the H1 or first sentence, the SEO title, the meta description, one heading, and the FAQs. Secondary keywords go where they read naturally. Keywords Ricky reserved for another page are not reused.'),
 ('n1','**Selling points (Andrew):** add Andrew\'s points and notes. For example, we don\'t sell an evacuation wheelchair, so that term is used only to explain what an evacuation chair does instead.'),
 ('n1','**Competitor research:** search the primary keywords and review the pages that rank (retailers, the manufacturer, buyer guides): what they cover, whether they have FAQs and which questions, and which keywords they use in product names.'),
 ('n1','**Facts:** every spec comes from our own product pages and the manufacturer\'s website or spec sheet. Where they disagree, I leave the number out and list the conflict in the notes for Andrew.'),
 ('n1','**Write:** a clear H1, a short intro, scannable bullets, H2 sections (types, how to choose, FAQs, about the brand), links to our collection pages only, an SEO title of 50 to 65 characters and a meta description of 140 to 160 characters. Copy reads like a person wrote it, with no claims comparing us to other brands.'),
 ('n1','**Review:** the draft goes into this doc with notes and questions. Andrew comments, and Ricky reviews how the keywords and selling points were used.'),
 ('n1','**Publish and check:** I update Shopify one page at a time, keeping the URL, SKUs and prices, then check the live page against the approved draft (text, SEO fields, headings, links, weights).'),
 ('h2','Collection Page Pilot: What the Research Found'),
 ('b1','**Who ranks for "evacuation chair" and "evacuation chairs for stairs":** manufacturers (Stryker, Evac+Chair), retailers (Grainger, Rehabmart, Global Industrial, Staples), and university and city buyer guides (NYC Mayor\'s Office for People with Disabilities, UC Berkeley).'),
 ('b1','**Retailer pages:** they put the capacity in the product name (for example "Evacuation Chair, 500 lb. Capacity"). Their category copy is thin, and the pages we could read had no FAQs.'),
 ('b1','**Buyer guides and the manufacturer FAQ:** they answer the same questions: how many operators, can it go up the stairs, capacity, stairway type, storage, training, and emergency action plans.'),
 ('b1','**What this page adds:** a "Types" section, a "How to choose" section, and four FAQs based on those questions, answered with facts from our product pages and the Evac+Chair website.'),
 ('b1','**Next for product pages:** consider adding the capacity to product names or subtitles, as the retailers do (Andrew to decide).')]
ids=sys.argv[1:]
if ids:
    for name,items,tid in (('coll',c,ids[0]),('proc',P,ids[1])):
        R,txt=build(tid,items); json.dump(R,open(f'req_{name}.json','w'),ensure_ascii=False); print(name,tid,len(R),len(json.dumps(R)))
else:
    s=json.dumps(c+P,ensure_ascii=False)
    print(len(c),len(P),'emdash' if '—' in s else 'no emdash','| dblspace' if '  ' in s else '')
    for k,t in P: print(k,'|',t[:100])
