import re,sys,html
t=html.unescape(re.sub(r'<[^>]+>','\n',re.sub(r'(?s)<(script|style|nav|header|footer)[^>]*>.*?</\1>','',open(sys.argv[1],errors='ignore').read())))
L=[l.strip() for l in t.splitlines() if l.strip()];t=' | '.join(L)
a=t.find('Choose an option'); a=t.rfind('|',0,max(a-400,0)) if a>0 else 0
b=t.find('Have any questions'); print('TOP:',t[max(a,0):b][:900])
i=t.find('| Description |',t.find('Items that pair well'));j=t.find('Similar Items',i)
print('DESC:',t[i:j])
m=re.findall(r'https://cortechusa.com/wp-content/uploads/[^"\' ]+\.pdf',open(sys.argv[1],errors='ignore').read())
print('PDFS:',sorted(set(m)))
