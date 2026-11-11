import json,sys
doc=json.load(open(sys.argv[1]))['content']
U=lambda s: len(s.encode('utf-16-le'))//2
E={'t.gw6ghp53i6dq':[
 ('It bolts securely to the floor','It bolts securely to the floor,','It comes in floor-mount and free-standing versions,'),
 ('Tamper-Resistant Glides: Optional','Optional for the ATN120, ATN150, and ATN130','Optional for the floor-mount models (ATN120, ATN150, and ATN130)'),
]}
out={}
for t in doc['tabs']:
    tid=t['tabProperties']['tabId']
    if tid not in E: continue
    paras=[]
    for el in t['documentTab']['body']['content']:
        p=el.get('paragraph')
        if not p: continue
        runs=[(r['startIndex'],r['textRun']) for r in p['elements'] if 'textRun' in r]
        txt=''.join(tr['content'] for _,tr in runs)
        paras.append((el['startIndex'],txt,runs))
    ops=[]
    for anchor,old,new in E[tid]:
        m=[p for p in paras if anchor in p[1]]
        assert len(m)==1,(tid,anchor,len(m))
        st,txt,runs=m[0]
        assert txt.count(old)==1,(tid,old)
        # minimal diff
        a=0
        while a<min(len(old),len(new)) and old[a]==new[a]: a+=1
        b=0
        while b<min(len(old),len(new))-a and old[-1-b]==new[-1-b]: b+=1
        pos=txt.index(old)+a
        dels=old[a:len(old)-b]; ins=new[a:len(new)-b]
        s=st+U(txt[:pos]); e=s+U(dels)
        # style of preceding char vs deleted
        def style_at(i):
            for rs,tr in runs:
                if rs<=i<rs+U(tr['content']): return tr.get('textStyle',{})
        pre=style_at(s-1); cur=style_at(s)
        flag='' if (pre or {}).get('bold')==(cur or {}).get('bold') and 'link' not in (pre or {}) else ' !!STYLE'
        print(tid,s,e,repr(dels[:50]),'->',repr(ins[:60]),flag)
        ops.append((s,e,ins))
    ops.sort(key=lambda x:-x[0])
    # check overlap
    for i in range(len(ops)-1): assert ops[i+1][1]<=ops[i][0]
    req=[]
    for s,e,ins in ops:
        if e>s: req.append({'deleteContentRange':{'range':{'startIndex':s,'endIndex':e,'tabId':tid}}})
        if ins: req.append({'insertText':{'text':ins,'location':{'index':s,'tabId':tid}}})
    out[tid]=req
allreq=[r for tid in E for r in out[tid]]
json.dump(allreq,open(sys.argv[2],'w'),ensure_ascii=False)
print(len(allreq),'requests; rev',doc['revisionId'][:20])
