import sys,re
for f in sys.argv[1:]:
    print('########',f)
    seen=set()
    for l in open(f,errors='ignore'):
        l=re.sub(r'\s+',' ',l).strip()
        if not l or l in seen or re.search(r'Toll Free|Plaza|Tel:|www\.cortech|subject to|All Rights|Contribute to a Safe',l): continue
        seen.add(l); print(l)
