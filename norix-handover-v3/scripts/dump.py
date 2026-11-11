import json,sys
d=json.load(open(sys.argv[1]))['content']
want=sys.argv[2:]
for t in d['tabs']:
    tid=t['tabProperties']['tabId']
    if want and tid not in want: continue
    print('=====',tid,t['tabProperties']['title'])
    for el in t['documentTab']['body']['content']:
        p=el.get('paragraph')
        if not p: continue
        st=p['paragraphStyle'].get('namedStyleType','')
        txt=''
        for r in p['elements']:
            tr=r.get('textRun')
            if not tr: continue
            s=tr['content']
            ts=tr.get('textStyle',{})
            if 'backgroundColor' in ts and ts['backgroundColor'].get('color'): s='{{HL:'+s+'}}'
            if tr.get('suggestedInsertionIds') or tr.get('suggestedDeletionIds'): s='{{SUG:'+s+'}}'
            txt+=s
        b='*' if p.get('bullet') else ' '
        print(el['startIndex'],el['endIndex'],st[:9],b,txt.rstrip('\n'))
