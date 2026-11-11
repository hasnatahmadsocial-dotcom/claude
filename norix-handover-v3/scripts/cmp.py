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
                if ts.get('strikethrough'): c='[STRIKE '+c+']'
                if ts.get('backgroundColor',{}).get('color'): c='[HL '+c+']'
                s+=c
            if s.strip(): L.append(('* ' if p.get('bullet') else '')+s)
        out[tid]=(t['tabProperties']['title'],L)
    return out
A=load(sys.argv[1]); M=load(sys.argv[2])
pairs=[('t.bhoihpluhjif','t.lcgpye84tajs'),('t.g9egfs3e2ylq','t.gw6ghp53i6dq'),('t.rhqzebjztcyi','t.nxl644rzl84j'),('t.39oebud4655t','t.ltqe3tz004ud'),('t.occzji85c5pk','t.cmyg5l8i7ncg'),('t.sczr4x2u3puo','t.ksj0oxo622hq'),('t.c8eiokwbz5lq','t.bhiw8wr766y3'),('t.8a9rdm57doas','t.r0b6bckifm2p'),('t.yglczyvq32qk','t.p9mzgzn2o0on')]
for a,m in pairs:
    print('#####',A[a][0],'|| main:',M[m][0])
    for l in difflib.unified_diff(A[a][1],M[m][1],'attenda','main',n=0,lineterm=''):
        if l.startswith(('---','+++')): continue
        print(l[:400])
