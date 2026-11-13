OK_NAMES={'7600 - Shelf / Step','8600 - Shelf / Step 2.0'}  # Andrew approved Nov 13
import json,sys,urllib.request,random,time,collections
H=sys.argv[1:]
for h in H:
    p=None
    for i in range(4):
        try:
            r=urllib.request.urlopen(f'https://www.anchortex.com/products/{h}.json?x={random.randint(1,10**9)}',timeout=30).read()
            p=json.loads(r)['product'];break
        except Exception as e: time.sleep(3)
    if not p: print('FETCH FAIL',h);continue
    iss=[]
    skus=collections.Counter(v['sku'] for v in p['variants'])
    for s,c in skus.items():
        if c>1: iss.append(f'duplicate SKU {s}')
    for v in p['variants']:
        pr=float(v['price']);ca=float(v['compare_at_price'] or 0)
        t=v['title']
        if pr==0: iss.append(f'PRICE $0 {v["sku"]} {t}')
        if ca==0: iss.append(f'compare-at $0 {v["sku"]} {t}')
        elif pr and abs(pr-ca*0.8)>0.01: iss.append(f'price not 80% of compare-at {v["sku"]} {pr} vs {ca}')
        if v['grams'] in (115666,0): iss.append(f'weight 255/0 {v["sku"]} {t}')
        if 'Solid' in t: iss.append(f'Solid in name {v["sku"]} {t}')
        if t.count(' / ')>=len(p['options']) and t not in OK_NAMES: iss.append(f'odd name {t}')
    print(('OK  ' if not iss else 'FIX ')+p['title'][:70], f'({len(p["variants"])} var)')
    for i in iss: print('    -',i)
