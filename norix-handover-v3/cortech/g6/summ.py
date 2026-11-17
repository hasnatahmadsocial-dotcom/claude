import json,re,sys,html
for line in open(sys.argv[1]):
    h,u=line.split(); s=u.rstrip('/').split('/')[-1]
    p=json.load(open(f'live/{h}.json'))['product']
    pg=open(f'page/{h}.html',encoding='utf-8',errors='ignore').read()
    t=re.search(r'<title>(.*?)</title>',pg,re.S); md=re.search(r'<meta name="description" content="([^"]*)"',pg)
    sub=re.search(r'class="product-subtitle__new mpn"[^>]*>(.*?)</p>',pg,re.S)
    print('='*100); print('HANDLE',h,'| id',p['id']); print('TITLE',p['title']); print('SUB',sub.group(1).strip() if sub else None)
    print('SEO T',html.unescape(t.group(1).strip()) if t else None); print('SEO D',html.unescape(md.group(1)) if md else None)
    print('TAGS',p['tags']); print('OPTIONS',[(o['name'],o['values']) for o in p['options']])
    for v in p['variants']: print('  V',v['position'],repr(v['title']),v['sku'],v['price'],v['compare_at_price'],v['weight'],v['weight_unit'])
    for i in p['images']: print('  IMG',i['position'],i['src'].split('/')[-1].split('?')[0],i['width'],i['height'],'|',i.get('alt'))
    body=re.sub(r'<[^>]+>','\n',p['body_html']); body=re.sub(r'\n\s*\n+','\n',html.unescape(body)).strip()
    print('BODY:\n'+body)
    links=re.findall(r'href="([^"]+)"',p['body_html']); print('BODY LINKS',links)
    c=open(f'site/{s}.html',encoding='utf-8',errors='ignore').read()
    pdfs=sorted(set(re.findall(r'https://cortechusa\.com/wp-content/uploads/[^"\' )]+\.pdf',c)))
    print('CORTECH PDFs',pdfs)
    imgs=sorted(set(x for x in re.findall(r'https://cortechusa\.com/wp-content/uploads/[^"\' )]+\.(?:jpg|jpeg|png|webp)',c) if not re.search(r'-\d+x\d+\.',x)))
    print('CORTECH IMGS',imgs)
