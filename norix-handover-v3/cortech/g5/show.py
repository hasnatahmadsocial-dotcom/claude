import json,re,sys,html
h=sys.argv[1]
p=json.load(open(f'live/{h}.json'))['product']
pg=open(f'page/{h}.html',errors='ignore').read()
m=re.search(r'product-subtitle__new[^>]*>(.*?)</',pg,re.S)
print('TITLE:',p['title']);print('SUB:',m and html.unescape(m.group(1)).strip())
print('TAGS:',p['tags'][:200])
print('OPTS:',[(o['name'],o['values']) for o in p['options']])
for v in p['variants']: print(' V',v['position'],repr(v['title']),v['sku'],v['price'],v.get('compare_at_price'),v['weight'],v['weight_unit'])
print('IMGS:',[i['src'].split('/')[-1].split('?')[0] for i in p['images']])
b=re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' | ',p['body_html']))); b=re.sub(r'( \| )+',' | ',b)
print('BODY:',b[:2500])
