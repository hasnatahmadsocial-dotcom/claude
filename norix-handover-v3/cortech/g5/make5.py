import json,sys
exec(open('mc5.py').read().split("if __name__")[0])
ids=open('ids5.txt').read().split()
for i,(d,t) in enumerate(zip(P,ids)):
    R,txt=build(t,content(d))
    json.dump(R,open(f'req/{i}.json','w'),ensure_ascii=False,separators=(',',':'))
    print(i,t,len(R),len(json.dumps(R,ensure_ascii=False)))
