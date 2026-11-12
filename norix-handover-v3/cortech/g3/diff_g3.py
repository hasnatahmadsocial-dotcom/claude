import json,sys,difflib,re
exec(open('mc3.py').read().split("if __name__")[0])
doc=json.load(open(sys.argv[1]))['content']
tabs={t['tabProperties']['title']:t for t in doc['tabs']}
sty={'h1':'HEADING_1','h2':'HEADING_2','h3':'HEADING_3'}
for d in P:
    t=tabs[d['tab']]
    want=[]
    for k,md in content(d):
        plain,b,l=parse(md); want.append(f"{sty.get(k,'P')[:9]}|{'•' if k in('b1','n1') else ' '}|{plain}")
    got=[]
    for e in t['documentTab']['body']['content']:
        if 'paragraph' in e:
            p=e['paragraph']; txt=''.join(x.get('textRun',{}).get('content','') for x in p['elements']).rstrip('\n')
            got.append(f"{p['paragraphStyle'].get('namedStyleType','P').replace('NORMAL_TEXT','P')[:9]}|{'•' if 'bullet' in p else ' '}|{txt}")
        elif 'table' in e: got.append('TABLE|'+json.dumps([[''.join(x.get('textRun',{}).get('content','') for c2 in c['content'] for x in c2.get('paragraph',{}).get('elements',[])) for c in r['tableCells']] for r in e['table']['tableRows']])[:300])
    while got and got[-1].endswith('|'): got.pop()
    df=[l for l in difflib.unified_diff(want,got,lineterm='',n=0) if not l.startswith(('---','+++'))]
    if df:
        print('=====',d['tab'])
        for l in df: print('  ',repr(l)[:260] if '\x0b' in l else l[:260])
