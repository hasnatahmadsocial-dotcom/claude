import json,sys,re
exec(open('make5.py').read().split("if __name__")[0])
doc=json.load(open(sys.argv[1]))['content']
T={t['tabProperties']['tabId']:t for t in doc['tabs']}
ids=open('ids5.txt').read().split()
which=[int(x) for x in sys.argv[2:]] if len(sys.argv)>2 else range(len(P))
def sig(md):
    t,b,l=parse(md); return t,b,l
STY={'h1':'HEADING_1','h2':'HEADING_2','h3':'HEADING_3'}
for i in which:
    d=P[i]; t=T[ids[i]]; c=content(d)
    paras=[el['paragraph'] for el in t['documentTab']['body']['content'] if 'paragraph' in el]
    errs=[]
    if t['tabProperties']['title']!=d['tab']: errs.append('TITLE')
    if len(paras)!=len(c)+1: errs.append(f'count {len(paras)} vs {len(c)+1}')
    for (k,md),p in zip(c,paras):
        txt=''.join(r['textRun']['content'] for r in p['elements'] if 'textRun' in r).rstrip('\n')
        et,b,l=parse(md)
        if txt!=et: errs.append('TEXT:'+et[:40]); continue
        st=p['paragraphStyle'].get('namedStyleType')
        if st!=STY.get(k,'NORMAL_TEXT'): errs.append(f'STYLE {st}:{et[:30]}')
        bl=p.get('bullet')
        if (k in('b1','n1'))!=bool(bl): errs.append('BULLET:'+et[:30])
        if k=='n1':
            g=t['documentTab']['lists'][bl['listId']]['listProperties']['nestingLevels'][0].get('glyphType')
            if g!='DECIMAL': errs.append('NUMGLYPH')
        # bold & link chars
        pos=0;gb=[];gl=[]
        for r in p['elements']:
            tr=r.get('textRun'); 
            if not tr: continue
            n=len(tr['content'].encode('utf-16-le'))//2; ts=tr.get('textStyle',{})
            if ts.get('bold'): gb.append((pos,pos+n))
            if ts.get('link'): gl.append((pos,pos+n,ts['link'].get('url')))
            pos+=n
        def merge(x):
            out=[]
            for a,c2 in sorted(x):
                if out and out[-1][1]==a: out[-1]=(out[-1][0],c2)
                else: out.append((a,c2))
            return out
        gb=[(a,min(c2,len(et.encode("utf-16-le"))//2)) for a,c2 in gb]
        if merge(gb)!=merge(b): errs.append('BOLD:'+et[:30])
        if [(a,c2,u) for a,c2,u in gl]!=l: errs.append('LINK:'+et[:30])
    print(i,d['tab'],'OK' if not errs else errs[:6])
