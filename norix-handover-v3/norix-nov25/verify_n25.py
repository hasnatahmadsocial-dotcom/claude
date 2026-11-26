import json,re,sys

exec(open('nf25.py').read().split("if __name__")[0])
doc=json.load(open(sys.argv[1]))['content']
tabs={t['tabProperties']['title']:t for t in doc['tabs']}
print(list(tabs))
sty={'h1':'HEADING_1','h2':'HEADING_2','h3':'HEADING_3'}
for d in P:
    if d['tab'] not in tabs: print('MISSING',d['tab']); continue
    want=content(d)
    paras=[e['paragraph'] for e in tabs[d['tab']]['documentTab']['body']['content'] if 'paragraph' in e]
    got=[]
    for p in paras:
        txt=''.join(x.get('textRun',{}).get('content','') for x in p['elements']).rstrip('\n')
        bold=''.join('**'+x['textRun']['content'].rstrip('\n')+'**' if x.get('textRun',{}).get('textStyle',{}).get('bold') else x.get('textRun',{}).get('content','') for x in p['elements']).rstrip('\n').replace('****','')
        links=[x['textRun']['textStyle']['link']['url'] for x in p['elements'] if 'link' in x.get('textRun',{}).get('textStyle',{})]
        got.append((p['paragraphStyle'].get('namedStyleType'),'bullet' in p,txt,bold,links))
    while got and got[-1][2]=='': got.pop()
    errs=[]
    if len(got)!=len(want): errs.append(f'COUNT {len(got)} vs {len(want)}')
    for (k,md),(st,bul,txt,bold,links) in zip(want,got):
        plain,b,l=parse(md)
        if txt!=plain: errs.append('TEXT:'+plain[:50])
        if st!=sty.get(k,'NORMAL_TEXT'): errs.append('STYLE:'+plain[:40])
        if bul!=(k in('b1','n1')): errs.append('BULLET:'+plain[:40])
        if bold!=re.sub(r'\[([^\]]+)\]\([^)]+\)',r'\1',md): errs.append('BOLD:'+plain[:40])
        if sorted(set(links))!=sorted(set(re.findall(r'\]\(([^)]+)\)',md))): errs.append('LINK:'+plain[:40])
    print(d['tab'],'|',len(got),'paras |','OK' if not errs else errs[:5])
