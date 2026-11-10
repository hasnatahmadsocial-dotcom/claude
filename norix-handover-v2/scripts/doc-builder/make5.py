import json,sys,re
exec(open('build3.py').read()); exec(open('p5.py').read())
def content(d):
    sp=', '.join(f'[{n}]({u})' for n,u in d['specs'])
    p=[('h1',d['short']),('p','**Product URL:** New product (URL to come)'),('p',f"**Manufacturer page:** [{d['src']}]({d['src']})"),
       ('p',f"**Spec sheet{'s' if len(d['specs'])>1 else ''}:** {sp}"),('h2','Recommended H1 and Subtitle'),
       ('p',f"**H1:** {d['h1']}"),('p',f"**Subtitle:** {d['sub']}"),
       ('h2','Product Description'),('p','Headings marked [H2] should be set as H2 on the page.')]
    p+=[('p',x) for x in d['intro']]+[('b1',x) for x in d['bullets']]
    p.append(('p','**Available Models and Options**')); p+=[('b1',x) for x in d['models']]
    p.append(('p','**Installation and Options**')); p+=[('b1',x) for x in d['install']]
    p+=d['apps']+d['series']+[('h3','[H2] About Norix Furniture'),('p',NXF)]
    p+=[('h2','Meta Title and Description'),('p',f"**Meta title ({len(d['mt'])} characters):** {d['mt']}"),('p',f"**Meta description ({len(d['md'])} characters):** {d['md']}")]
    p.append(('h2','Notes and Questions')); p+=[('n1',x) for x in d['notes']]
    return p
if __name__=='__main__':
    for d in P:
        c=content(d); s=json.dumps(c,ensure_ascii=False); e=[]
        if '—' in s: e.append('EMDASH')
        if not(50<=len(d['mt'])<=65): e.append('MT %d'%len(d['mt']))
        if not(140<=len(d['md'])<=160): e.append('MD %d'%len(d['md']))
        for k,t in c:
            if '–' in t and not (t.startswith('**H1:**') or re.match(r'\*\*[A-Z0-9][^*]* – ',t)): e.append('ENDASH:'+t[:40])
        print(d['tab'],len(d['tab']),len(c),e or 'ok')
