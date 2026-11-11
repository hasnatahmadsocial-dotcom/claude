import json,sys,re
exec(open('build3.py').read()); exec(open('p3.py').read())
A_='https://www.anchortex.com/products/'
def content(d):
    URL=A_+d['handle']
    sp=', '.join(f'[{n}]({u})' for n,u in d['specs'])
    p=[('h1',d['short']),('p',f"**Product URL:** [{URL}]({URL})"),('p',f"**Manufacturer page:** [{d['src']}]({d['src']})"),
       ('p',f"**Spec sheet{'s' if len(d['specs'])>1 else ''}:** {sp}"),('h2','Recommended H1 and Subtitle'),
       ('p',f"**H1:** {d['h1']}"),('p',f"**Current H1:** {d['cur_h1']}"),('p',f"**Subtitle:** {d['sub']}"),('p',f"**Current subtitle:** {d['cur_sub']}"),
       ('h2','Revised Product Description'),('p','Headings marked [H2] should be set as H2 on the page.')]
    p+=[('p',x) for x in d['intro']]+[('b1',x) for x in d['bullets']]
    if d['models']: p.append(('p','**Available Models and Options**')); p+=[('b1',x) for x in d['models']]
    p.append(('p','**Installation and Options**')); p+=[('b1',x) for x in d['install']]
    p+=d['apps']+d['series']+[('h3','[H2] About Norix Furniture'),('p',NXF)]
    p+=[('h2','Meta Title and Description'),('p',f"**Meta title ({len(d['mt'])} characters):** {d['mt']}"),('p',f"**Meta description ({len(d['md'])} characters):** {d['md']}")]
    p.append(('h2','Notes and Questions')); p+=[('n1',x) for x in d['notes']]
    return p
if __name__=='__main__':
    bad=0
    for i,d in enumerate(P):
        c=content(d); s=json.dumps(c,ensure_ascii=False)
        errs=[]
        if '—' in s: errs.append('EMDASH')
        if not(50<=len(d['mt'])<=65): errs.append('MT %d'%len(d['mt']))
        if not(140<=len(d['md'])<=160): errs.append('MD %d'%len(d['md']))
        if len(d['tab'])>50: errs.append('TAB')
        if d['h1'].count('–')!=1: errs.append('H1 endash')
        body=' '.join(t for k,t in c[10:] if True)
        # en dash only in H1 & model bullet labels
        for k,t in c:
            if '–' in t and not (t.startswith('**H1:**') or k=='h1' or re.match(r'\*\*[A-Z0-9][^*]* – ',t) or t.startswith('**Current')): errs.append('ENDASH:'+t[:50])
        links=re.findall(r'\]\(([^)]+)\)',s)
        if any('/products/' in l for l in links if 'anchortex' in l and l!=A_+d['handle']): errs.append('PRODUCTLINK')
        print(i,d['tab'],'paras',len(c),errs or 'ok'); bad+=bool(errs)
    print('bad',bad)
