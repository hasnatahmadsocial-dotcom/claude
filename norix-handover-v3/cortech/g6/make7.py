import json,sys
exec(open('mc7.py').read().split("if __name__")[0])
ids=open('ids7.txt').read().split()
for i,(d,t) in enumerate(zip(P,ids)):
    R,txt=build(t,content(d))
    json.dump(R,open(f'req7/{i}.json','w'),ensure_ascii=False,separators=(',',':'))
    print(i,t,len(R),len(json.dumps(R,ensure_ascii=False)))
