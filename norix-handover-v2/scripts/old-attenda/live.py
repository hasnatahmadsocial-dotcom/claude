import json,re,html,sys,subprocess,difflib,random
H,HTMLF,SUB=sys.argv[1],sys.argv[2],sys.argv[3]
def get(u): return subprocess.run(['curl','-s',u+('&' if '?' in u else '?')+'x=%d'%random.randint(1,10**9)],capture_output=True,text=True).stdout
p=json.loads(get(f'https://www.anchortex.com/products/{H}.json'))['product']; h=get(f'https://www.anchortex.com/products/{H}')
js=json.loads(get(f'https://www.anchortex.com/products/{H}.js'))
print('TITLE',p['title'])
print('TAG',html.unescape(re.search(r'<title>(.*?)</title>',h,re.S).group(1).strip()))
m=re.search(r'name="description" content="(.*?)"',h); print('META',html.unescape(m.group(1)))
print('SUB', SUB in html.unescape(h))
def norm(s): return re.sub(r'\s+',' ',html.unescape(s)).replace('> <','><').strip()
want=norm(open(HTMLF).read()); got=norm(p['body_html'])
print('BODY MATCH',want==got)
if want!=got:
    a=[x.strip() for x in re.sub(r'<[^>]+>','\n',want).split('\n') if x.strip()]; b=[x.strip() for x in re.sub(r'<[^>]+>','\n',got).split('\n') if x.strip()]
    for l in difflib.unified_diff(a,b,lineterm='',n=0): print(l)
    print('links same',sorted(re.findall(r'href="([^"]+)"',want))==sorted(re.findall(r'href="([^"]+)"',got)), 'tags', re.findall(r'<(h\d|ul|li)',want)==re.findall(r'<(h\d|ul|li)',got))
print('handle',p['handle'],'options',[(o['name'],o['values']) for o in p['options']])
for v,j in zip(p['variants'],js['variants']): print(v['position'],v['title'],v['sku'],v['price'],v['compare_at_price'],v['weight'],v['weight_unit'],'avail',j['available'])
for i in p['images']: print(i['position'],i['src'].split('/')[-1].split('?')[0])
