OK_NAMES={'7600 - Shelf / Step','8600 - Shelf / Step 2.0'}  # Andrew approved Nov 13
OK_NAMES|={f'{h} Hinge / {m}' for h in ('Left','Right') for m in ('No Mirror','Steel Mirror','Polycarbonate Mirror')}  # ARC801 (Nov 24): one option 'Hinge and Mirror', values contain ' / '
# Evac/REX: REX has no compare-at (Rapid Extraction has no MSRP on our page); Evac+Chair price = 75% of compare-at (not 80%).
NO_CA={'rex-dcs-cf-multi-purpose-extraction-stretcher-for-correctional-facilities','rex-one-dcs-multi-purpose-extraction-stretcher-with-descent-control-system','rapid-extraction-rex-one-multi-purpose-extraction-stretcher'}
PCT75_PREFIX='evac-chair-'
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
        if ca==0:
            if h not in NO_CA: iss.append(f'compare-at $0 {v["sku"]} {t}')
        elif h.startswith(PCT75_PREFIX):
            if abs(pr-ca*0.75)>1: iss.append(f'price not 75% of compare-at {v["sku"]} {pr} vs {ca}')
        elif pr and abs(pr-ca*0.8)>0.01: iss.append(f'price not 80% of compare-at {v["sku"]} {pr} vs {ca}')
        if v['grams'] in (115666,0): iss.append(f'weight 255/0 {v["sku"]} {t}')
        if 'Solid' in t: iss.append(f'Solid in name {v["sku"]} {t}')
        if t.count(' / ')>=len(p['options']) and t not in OK_NAMES: iss.append(f'odd name {t}')
    print(('OK  ' if not iss else 'FIX ')+p['title'][:70], f'({len(p["variants"])} var)')
    for i in iss: print('    -',i)
