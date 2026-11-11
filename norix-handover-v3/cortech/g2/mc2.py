import json,re,sys
exec(open('../../scripts/doc-builder/build3.py').read())
exec(open('../pc.py').read())
exec(open('pc2.py').read())
NOMPN=('X-Series','Steel Leg','Structured Seating')
def content(d):
    URL=A+d['handle']
    sp=', '.join(f'[{n}]({u})' for n,u in d['specs'])
    lab='Spec sheets' if len(d['specs'])>1 else 'Spec sheet'
    src=', '.join(f'[{u}]({u})' for u in d['src'])
    ml='Manufacturer pages' if len(d['src'])>1 else 'Manufacturer page'
    p=[('h1',d['short']),('p',f"**Product URL:** [{URL}]({URL})"),('p',f"**{ml}:** {src}"),
       ('p',f"**{lab}:** {sp}"),('h2','Recommended H1 and Subtitle'),
       ('p',f"**H1:** {d['h1']}"),('p',f"**Current H1:** {d['cur_h1']}"),('p',f"**Subtitle:** {d['sub']}"),('p',f"**Current subtitle:** {d['cur_sub']}"),
       ('h2','Revised Product Description'),('p','Headings marked [H2] should be set as H2 on the page.')]
    p+=[('p',x) for x in d['intro']]+[('b1',x) for x in d['bullets']]
    p.append(('p','**Available Models and Options**')); p+=[('b1',x) for x in d['models']]
    p.append(('p','**Installation and Options**')); p+=[('b1',x) for x in d['install']]
    p+=d['apps']+d['series']+[('h3','[H2] About Cortech'),('p',CTF)]
    p+=[('h2','Meta Title and Description'),('p',f"**Meta title ({len(d['mt'])} characters):** {d['mt']}"),('p',f"**Meta description ({len(d['md'])} characters):** {d['md']}")]
    p.append(('h2','Notes and Questions')); p+=[('n1',x) for x in d['notes']]
    return p
if __name__=='__main__':
    for d in P:
        c=content(d); s=json.dumps(c,ensure_ascii=False); e=[]
        if '—' in s: e.append('EMDASH')
        if '‑' in s.replace(d['cur_h1'],''): e.append('NBHYPHEN')
        if not(50<=len(d['mt'])<=65): e.append('MT %d'%len(d['mt']))
        if not(140<=len(d['md'])<=160): e.append('MD %d'%len(d['md']))
        if len(d['tab'])>50: e.append('TAB %d'%len(d['tab']))
        want=0 if d['tab'].startswith(NOMPN) else 1
        if d['h1'].count('–')!=want: e.append('H1 endash')
        for k,t in c:
            if '–' in t and not (t.startswith('**H1:**') or re.match(r'\*\*[A-Z0-9][^*]* – [^*]*:\*\*',t)): e.append('ENDASH:'+t[:50])
            if '  ' in t: e.append('DBLSPACE:'+t[:40])
            if re.search(r'\d” [x×]|[x×] \d”',t) and k!='n1': e.append('DIMSPACE:'+t[:50])
            if '...' in t: e.append('ELLIPSIS:'+t[:40])
            if re.search(r'\d"',t) and not t.startswith('**Current') and k!='n1': e.append('STRAIGHTQ:'+t[:50])
        links=re.findall(r'\]\((https://www\.anchortex\.com/[^)]+)\)',s)
        bad=[l for l in links if '/products/' in l and l!=A+d['handle']]
        if bad: e.append('PRODLINK')
        print(d['tab'],'|',len(d['tab']),'| mt',len(d['mt']),'md',len(d['md']),'| paras',len(c),e or 'ok')
        if 'Anchortex' not in d['mt']: print('   MT+AT', len(d['mt']+' at Anchortex'))
