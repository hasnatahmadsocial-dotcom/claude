# Norix batch 11/23/2026 builder. Same tab format as scripts/doc-builder/make4.py (existing products) and make5.py (new products).
# Run from norix-nov23/:  python3 -I nb.py   (checks: MT 50-65, MD 140-160, dashes, double spaces, straight inch marks, product links)
import json,re
exec(open('../scripts/doc-builder/build3.py').read())
exec(open('../scripts/doc-builder/p3.py').read().split('P=[]')[0])
NXF=NXF.replace('psychiatric hospitals, correctional','psychiatric hospitals, police stations, correctional')   # Andrew added "police stations"
A_='https://www.anchortex.com/products/'
SEAT_SERIES=[
('h3','[H2] About Norix Seating'),
('p','Norix makes seating for behavioral healthcare, correctional, and other high-use facilities, from lightweight stackable chairs for staff areas to heavy, ballastable lounge seating for patient and inmate areas.'),
('p','The Norix seating range includes:'),
('b1','**Stackable Chairs:** Integra, Progress, and Affinity'),
('b1','**Guest and Lounge Seating:** Flux, Forté, Vesta, Hondo Nuevo, Ripple, Wink, and Toro'),
('b1','**Indoor and Outdoor Seating:** Coupe, Flux, Pax, Kube, Goby, and Riptide'),
('b1','**Upholstered Seating:** Forma, Element, Harmony, and Respite'),
('b1','**Rockers and Stools:** Flux, Rocksmart, Mix-Up, and B-Side'),
('b1','**Metal Seating:** VersaFrame, Boulder, and Terra'),
]
SEAT_NEW='New series section: this batch has three seating products (Progress, Rocksmart, and Respite), so I wrote an "About Norix Seating" section based on the Norix Seating Guide (September 2026). It has no links to individual products. Please review it here; the same section will go on the Rocksmart and Respite tabs.'
P=[]
def add(**k): P.append(k)
exec(open('pn1.py').read())
def content(d):
    sp=', '.join(f'[{n}]({u})' for n,u in d['specs'])
    if d.get('new'):
        p=[('h1',d['short']),('p','**Product URL:** New product (URL to come)')]
    else:
        URL=A_+d['handle']; p=[('h1',d['short']),('p',f"**Product URL:** [{URL}]({URL})")]
    p+=[('p',f"**Manufacturer page:** [{d['src']}]({d['src']})"),('p',f"**Spec sheet{'s' if len(d['specs'])>1 else ''}:** {sp}"),
        ('h2','Recommended H1 and Subtitle'),('p',f"**H1:** {d['h1']}")]
    if not d.get('new'): p.append(('p',f"**Current H1:** {d['cur_h1']}"))
    p.append(('p',f"**Subtitle:** {d['sub']}"))
    if not d.get('new'): p.append(('p',f"**Current subtitle:** {d['cur_sub']}"))
    p+=[('h2','Product Description' if d.get('new') else 'Revised Product Description'),('p','Headings marked [H2] should be set as H2 on the page.')]
    p+=[('p',x) for x in d['intro']]+[('b1',x) for x in d['bullets']]
    if d['models']: p.append(('p','**Available Models and Options**')); p+=[('b1',x) for x in d['models']]
    p.append(('p','**Installation and Options**'))
    p+=[('p',d['install'])] if isinstance(d['install'],str) else [('b1',x) for x in d['install']]
    p+=d['apps']+d['series']+[('h3','[H2] About Norix Furniture'),('p',NXF)]
    p+=[('h2','Meta Title and Description'),('p',f"**Meta title ({len(d['mt'])} characters):** {d['mt']}")]
    if not d.get('new'): p.append(('p',f"**Current meta title:** {d['cur_mt']}"))
    p.append(('p',f"**Meta description ({len(d['md'])} characters):** {d['md']}"))
    if not d.get('new'): p.append(('p',f"**Current meta description:** {d['cur_md']}"))
    p.append(('h2','Notes and Questions')); p+=[('n1',x) for x in d['notes']]
    return p
if __name__=='__main__':
    for d in P:
        c=content(d); s=json.dumps(c,ensure_ascii=False); e=[]
        if '—' in s: e.append('EMDASH')
        if not(50<=len(d['mt'])<=65): e.append('MT %d'%len(d['mt']))
        if not(140<=len(d['md'])<=160): e.append('MD %d'%len(d['md']))
        if len(d['tab'])>50: e.append('TAB %d'%len(d['tab']))
        if d['h1'].count('–')!=1: e.append('H1 endash')
        for k,t in c:
            if '  ' in t: e.append('DBLSPACE:'+t[:40])
            if '–' in t and not (t.startswith(('**H1:**','**Current')) or re.match(r'\*\*[A-Z0-9][^*]* – [^*]*:\*\*',t)): e.append('ENDASH:'+t[:50])
            if re.search(r'\d"',t) and not t.startswith('**Current') and k!='n1': e.append('STRAIGHTQ:'+t[:50])
        links=re.findall(r'\]\(([^)]+)\)',s)
        if any('anchortex.com/products/' in l and not l.endswith(d.get('handle','#')) for l in links): e.append('PRODUCTLINK')
        print(d['tab'],'| mt',len(d['mt']),'md',len(d['md']),'| paras',len(c),e or 'ok')
