# usage: python3 -I ads/check.py <ads handle> <before.json> <expected html> [weights lb comma list] [expected prices 'i:price/compare,...' (0-based variant index) for approved price fixes]
import json,re,sys,html,urllib.request,random,subprocess
h,before,exp=sys.argv[1:4]; W=[float(x) for x in sys.argv[4].split(',')] if len(sys.argv)>4 else None
EP={int(k):tuple(v.split('/')) for k,v in (x.split(':') for x in sys.argv[5].split(','))} if len(sys.argv)>5 else {}
get=lambda u: subprocess.run(['curl','-s',u],capture_output=True,text=True).stdout
B=json.loads(get(f'https://www.americandetentionsupplies.com/products/{h}.json?x={random.randint(1,99999)}'))['product']
A=json.load(open(before)); A=A.get('product',A)
n=lambda s: re.sub(r'\s+',' ',s).strip()
e=open(exp).read(); ok=n(B['body_html'])==n(e)
print('updated',B['updated_at']); print(('✅' if ok else '⚠️'),'description = expected HTML')
if not ok:
    import difflib
    for l in difflib.unified_diff(n(e).split('> '),n(B['body_html']).split('> '),lineterm='',n=0): print('   ',l[:220])
print('ℹ️ Anchortex count',B['body_html'].count('Anchortex'),'| American Detention Supplies count',B['body_html'].count('American Detention Supplies'))
for k in ['title','handle','vendor','product_type','tags']: print('✅' if A[k]==B[k] else '⚠️',k,'same' if A[k]==B[k] else f'{A[k]!r}->{B[k]!r}')
av={v['id']:v for v in A['variants']}
print('✅' if len(A['variants'])==len(B['variants']) else '⚠️','variants',len(A['variants']),'->',len(B['variants']))
for i,v in enumerate(B['variants']):
    a=av.get(v['id']); lb=round(v['grams']/453.592,2)
    exp=(a['title'],a['sku'])+(EP[i] if i in EP else (a['price'],a['compare_at_price'])) if a else None
    same=a and exp==(v['title'],v['sku'],v['price'],v['compare_at_price'])
    wok= W is None or abs(lb-W[i])<0.06
    print('✅' if same and wok else '⚠️',v['title'],v['sku'],v['price'],v['compare_at_price'],lb,'lb', ('(price fix as planned)' if i in EP else '') if same else f'UNEXPECTED: expected {exp}', '' if wok else f'WEIGHT expected {W[i]}')
ai=[x['src'].split('/')[-1].split('?')[0] for x in A['images']]; bi=[x['src'].split('/')[-1].split('?')[0] for x in B['images']]
print('✅' if ai==bi else 'ℹ️','images',len(ai),'->',len(bi), '' if ai==bi else bi)
