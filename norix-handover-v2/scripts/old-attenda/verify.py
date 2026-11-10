import json,sys,re
d=json.load(open(sys.argv[1]))
d=d.get('content',d)
def walk(tabs):
    for t in tabs:
        yield t; yield from walk(t.get('childTabs',[]))
for t in walk(d['tabs']):
    tp=t['tabProperties']; body=t['documentTab']['body']['content']
    paras=[];links=[];bul=0;heads={}
    for el in body:
        p=el.get('paragraph')
        if not p: continue
        txt=''.join(r.get('textRun',{}).get('content','') for r in p['elements'])
        st=p['paragraphStyle'].get('namedStyleType')
        if st.startswith('HEADING'): heads.setdefault(st,[]).append(txt.strip())
        if p.get('bullet'): bul+=1
        for r in p['elements']:
            l=r.get('textRun',{}).get('textStyle',{}).get('link')
            if l: links.append((r['textRun']['content'],l.get('url') or l.get('tabId')))
        paras.append(txt)
    full=''.join(paras)
    print('==',tp['title'],tp['tabId'],'chars',len(full),'bullets',bul,'emdash',full.count('—'))
    print('  H1',heads.get('HEADING_1')); print('  H2',heads.get('HEADING_2')); print('  H3',heads.get('HEADING_3'))
    bad=[(a,u) for a,u in links if a.startswith('http') and a.strip()!=u]
    print('  links',len(links),'mismatch',bad)
    for m in re.finditer(r'Meta (title|description) \((\d+) characters\): (.*)',full):
        if int(m.group(2))!=len(m.group(3)): print('  META MISMATCH',m.group(0))
