import json,sys,difflib
def load(f):
    d=json.load(open(f))['content']; out={}
    for t in d['tabs']:
        tid=t['tabProperties']['tabId']; L=[]
        for el in t['documentTab']['body']['content']:
            p=el.get('paragraph')
            if not p: continue
            s=''
            for r in p['elements']:
                tr=r.get('textRun')
                if not tr: continue
                c=tr['content'].replace('\n',''); ts=tr.get('textStyle',{})
                if not c: continue
                if ts.get('bold'): c='<b>'+c+'</b>'
                if ts.get('italic'): c='<i>'+c+'</i>'
                if ts.get('link'): c='<a '+ts['link'].get('url',ts['link'].get('tabId','?'))+'>'+c+'</a>'
                if ts.get('strikethrough'): c='[STRIKE '+c+']'
                if ts.get('backgroundColor',{}).get('color'): c='[HL '+c+']'
                if ts.get('fontSize'): c='[FS'+str(ts['fontSize'].get('magnitude'))+' '+c+']'
                s+=c
            s=s.replace('</b><b>','')
            st=p['paragraphStyle'].get('namedStyleType','')[:9]
            bl=''
            if p.get('bullet'): bl='*L%d '%p['bullet'].get('nestingLevel',0)
            if s.strip(): L.append(st+' '+bl+s)
        out[tid]=(t['tabProperties']['title'],L)
    return out
A=load(sys.argv[1]); M=load(sys.argv[2])
pairs=[x.split(':') for x in sys.argv[3:]]
for a,m in pairs:
    print('#####',A[a][0],'|| main:',M[m][0], len(A[a][1]),len(M[m][1]))
    for l in difflib.unified_diff(A[a][1],M[m][1],'attenda','main',n=0,lineterm=''):
        if l.startswith(('---','+++')): continue
        print(l[:300])
