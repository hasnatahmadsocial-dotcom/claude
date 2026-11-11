import sys,json,difflib
exec(open('scripts/cmp2.py').read().split('A=load')[0])
d=json.load(open(sys.argv[2]))['content']
print('LIVE title:',d['title'],'id',d['documentId'],'tabs',len(d['tabs']))
S=load(sys.argv[1]); L=load(sys.argv[2])
st={v[0]:k for k,v in S.items()}; lt={v[0]:k for k,v in L.items()}
print('only in snapshot:',[t for t in st if t not in lt])
print('only in live:',[t for t in lt if t not in st])
order_s=[v[0] for v in S.values()]; order_l=[v[0] for v in L.values()]
print('same order:',order_s==order_l)
n=0
for t in lt:
    if t not in st: continue
    a=S[st[t]][1]; b=L[lt[t]][1]
    if a!=b:
        n+=1; print('#####',t)
        for l in difflib.unified_diff(a,b,n=0,lineterm=''):
            if l.startswith(('---','+++')): continue
            print(l[:400])
print('changed tabs:',n)
