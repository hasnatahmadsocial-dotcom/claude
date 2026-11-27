# Audit in-scope ADS Norix products vs ANC (weights, variant names, prices, SKUs, images)
import json,subprocess,random,time,re
def get(u):
    for i in range(4):
        o=subprocess.run(['curl','-s',u+f'?x={random.randint(1,99999)}'],capture_output=True,text=True).stdout
        try: return json.loads(o)['product']
        except: time.sleep(3)
pairs=[l.split() for l in open('ads/pairs.txt')]
extra=[('norix-duravision-round-mirror','norix-duravision-round-mirror'),('duravision-rectangle-wall-mirror','norix-duravision-rectangle-mirror'),
('norix-citadel-property-storage-box-lids','norix-citadel-property-storage-box-lids'),('norix-citadel-property-storage-boxes','norix-citadel-property-storage-boxes'),
('norix-duravision-full-dome-mirror',None),('duravision-half-dome-safety-mirror',None),('duravision-mqd-quarter-dome-mirror-impact-resistant',None),
('norix-tank-box-property-storage-boxes',None),('norix-tank-box-property-storage-box-lids',None)]
m=json.load(open('ads/norix_sku2adshandle.json'))
out=[]
for a,b in pairs+extra:
    A=get(f'https://www.anchortex.com/products/{a}.json')
    if b is None:
        b=m[A['variants'][0]['sku'].split('-')[0]][0]
    B=get(f'https://www.americandetentionsupplies.com/products/{b}.json')
    av={v['sku']:v for v in A['variants']}; bv={v['sku'][4:]:v for v in B['variants']}
    iss=[]
    for s,x in av.items():
        y=bv.get(s)
        if not y: iss.append(f'SKU {s} missing on ADS'); continue
        if abs(x['grams']-y['grams'])>30: iss.append(f"wt {y['title'][:28]} {y['grams']/453.592:.1f}->{x['grams']/453.592:.1f}")
        if x['title']!=y['title']: iss.append(f"name '{y['title']}' -> '{x['title']}'")
        if (x['price'],x['compare_at_price'])!=(y['price'],y['compare_at_price']): iss.append(f"price {s} {y['price']}/{y['compare_at_price']} -> {x['price']}/{x['compare_at_price']}")
    for s in bv:
        if s not in av: iss.append(f'extra ADS SKU {s}')
    out.append((a,b,iss))
    print(('✅' if not iss else '⚠️'),b,'|',len(iss),'issues'); [print('    ',i) for i in iss[:12]]
json.dump(out,open('ads/audit.json','w'),indent=1)
