# usage: review.py handle expected.html "subtitle" "seo title" "seo desc" baseline.json
import json,re,html,sys,subprocess,random,time
H,HF,SUB,ST,SD,BL=sys.argv[1:7]
def get(u,tries=6):
    for i in range(tries):
        r=subprocess.run(['curl','-s','-L',u+('&' if '?' in u else '?')+'x=%d'%random.randint(1,10**9)],capture_output=True,text=True).stdout
        if 'Verifying your connection' not in r: return r
        time.sleep(3)
    return r
def code(u):
    for i in range(4):
        c=subprocess.run(['curl','-s','-o','/dev/null','-w','%{http_code}','-L',u],capture_output=True,text=True).stdout
        if c=='200': return c
        time.sleep(2)
    return c
p=json.loads(get(f'https://www.anchortex.com/products/{H}.json'))['product']
pg=html.unescape(get(f'https://www.anchortex.com/products/{H}'))
b=json.load(open(BL))['product']
issues=[];ok=[]
def chk(cond,good,bad): (ok if cond else issues).append(good if cond else bad)
tag=re.search(r'<title>(.*?)</title>',pg,re.S).group(1).strip()
meta=re.search(r'name="description" content="(.*?)"',pg).group(1)
norm=lambda s: re.sub(r'\s+',' ',html.unescape(s)).replace('> <','><').strip()
body=p['body_html']
chk(norm(open(HF).read())==norm(body),'description matches','DESCRIPTION differs from expected HTML')
chk(tag==ST,'SEO title ok','SEO title is "%s"'%tag)
chk(50<=len(tag)<=65,'SEO title length %d'%len(tag),'SEO title length %d (need 50-65)'%len(tag))
chk(meta==SD,'meta description ok','meta description is "%s"'%meta)
chk(140<=len(meta)<=160,'meta length %d'%len(meta),'meta length %d (need 140-160)'%len(meta))
chk(SUB in pg,'subtitle showing','SUBTITLE not found on page')
chk('—' not in body+p['title']+tag+meta,'no em dashes','EM DASH found')
chk(p['title'].count('–')==1,'H1 en dash ok','H1 en dash count %d'%p['title'].count('–'))
chk('<h2>' in body and '<h1' not in body,'H2s ok','heading tags wrong')
links=re.findall(r'href="([^"]+)"',body)
chk(all('/collections/' in l for l in links),'links collections only','link to non-collection: %s'%[l for l in links if '/collections/' not in l])
bad=[l for l in links if code(l)!='200']
chk(not bad,'%d links load'%len(links),'BROKEN links %s'%bad)
chk(p['handle']==b['handle'],'URL unchanged','URL CHANGED to %s'%p['handle'])
bv={v['id']:v for v in b['variants']}
for v in p['variants']:
    o=bv.get(v['id'])
    if not o: issues.append('new variant %s'%v['title']); continue
    if v['sku']!=o['sku']: issues.append('SKU changed %s -> %s'%(o['sku'],v['sku']))
    if v['price']!=o['price'] or v['compare_at_price']!=o['compare_at_price']: issues.append('PRICE changed on %s'%v['sku'])
    if v['grams'] in (0,115666): issues.append('weight not set on %s (%s)'%(v['sku'],v['grams']))
    if re.search(r'Standard Bed|- ATN301$|\w- ',v['title']): issues.append('variant name looks old: %s'%v['title'])
if len(p['variants'])!=len(b['variants']): issues.append('variant count %d vs %d'%(len(p['variants']),len(b['variants'])))
skus=[v['sku'] for v in p['variants']]
dup={s for s in skus if skus.count(s)>1}
if dup: issues.append('duplicate SKU %s'%dup)
bi=[i['id'] for i in b['images']]; li=[i['id'] for i in p['images']]
chk(set(bi)<=set(li),'all %d images kept'%len(li),'IMAGES removed: %d of %d'%(len(set(bi)-set(li)),len(bi)))
names=[i['src'].split('/')[-1].split('?')[0] for i in p['images']]
typo=[n for n in names if re.search(r'Sabd|ATN150.*Storage',n,re.I)]
if typo: issues.append('image file names to fix: %s'%typo)
print('PRODUCT',p['title'])
for v in p['variants']: print('  ',v['title'],'|',v['sku'],'|',v['price'],'|',v['weight'],v['weight_unit'])
print('OK:',', '.join(ok))
print('ISSUES:' if issues else 'ISSUES: none'); [print('  -',i) for i in issues]
