import json,sys,re,html,openpyxl,datetime
ws=openpyxl.load_workbook('ws3/w3.xlsx').worksheets[0]
for h in sys.argv[1:]:
    p=json.load(open(f'nx3/live/{h}.json'))['product']
    print('#####',h); print('TITLE:',p['title'])
    b=re.sub(r'<[^>]+>','\n',p['body_html'] or ''); b=html.unescape(re.sub(r'\n\s*\n+','\n',b)).strip()
    print('BODY:',b.replace('\n',' | ')[:2500])
    print('OPTIONS:',[(o['name'],o['values']) for o in p['options']])
    for v in p['variants']: print('  V',v['position'],repr(v['title']),v['sku'],v['price'],v['grams'],'g')
    for i in p['images']: print('  IMG',i['position'],i['src'].split('/')[-1].split('?')[0])
    for r in ws.iter_rows(min_row=2):
        if r[0].value==h: print('  WS',r[0].row,[c.value for c in r[1:13]])
