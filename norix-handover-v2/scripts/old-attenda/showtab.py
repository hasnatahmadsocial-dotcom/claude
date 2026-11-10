import json,sys
d=json.load(open(sys.argv[1])); TID=sys.argv[2]
def find(tabs):
    for t in tabs:
        if t['tabProperties']['tabId']==TID: return t
        r=find(t.get('childTabs',[]))
        if r: return r
t=find(d['content']['tabs'])
for el in t['documentTab']['body']['content']:
    p=el.get('paragraph')
    if not p: continue
    txt=''.join(e.get('textRun',{}).get('content','') for e in p['elements'])
    links=[e['textRun']['textStyle']['link']['url'].rstrip('/').split('/')[-1] for e in p['elements'] if e.get('textRun',{}).get('textStyle',{}).get('link')]
    st=p['paragraphStyle'].get('namedStyleType','')
    b=('*'*(1+p['bullet'].get('nestingLevel',0))) if 'bullet' in p else ' '
    print(el['startIndex'],st[:9].ljust(9),b.ljust(2),txt.strip()[:75],links if links else '')
    if '—' in txt or '\t' in txt: print('EMDASH/TAB!')
