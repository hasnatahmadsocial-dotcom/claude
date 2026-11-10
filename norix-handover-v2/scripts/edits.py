import json,sys
doc=json.load(open(sys.argv[1]))['content']
U=lambda s: len(s.encode('utf-16-le'))//2
E={
't.bhoihpluhjif':[
 ('Four versions cover','floor-mounted and free-standing installations, with or without mounting holes.','floor-mount and free-standing installations, with or without a bottom closure panel.'),
 ('ATN101 – Standard Bed:','Standard Bed:','Floor-Mount Bed:'),
 ('ATN101 – Standard Bed:','Floor-mount bed with mounting holes,','Mounting holes,'),
 ('ATN101B – Free-Standing Bed:','Free-Standing Bed:','Floor-Mount Bed with Bottom Closure:'),
 ('ATN101B – Free-Standing Bed:','Fully enclosed bottom,','Mounting holes, fully enclosed bottom,'),
 ('ATN103 – Standard Bed, No Mounting Holes:','Standard Bed, No Mounting Holes:','Free-Standing Bed:'),
 ('ATN103 – Standard Bed, No Mounting Holes:',': 110 lbs',': No mounting holes, 110 lbs'),
 ('ATN103B – Free-Standing Bed, No Mounting Holes:','Free-Standing Bed, No Mounting Holes:','Free-Standing Bed with Bottom Closure:'),
 ('ATN103B – Free-Standing Bed, No Mounting Holes:','Fully enclosed bottom,','No mounting holes, fully enclosed bottom,'),
 ('Variants: two variants are named','two variants are named "ATN101B" (SKUs N700186-04 and N700186-03). Per the Norix spec sheet, the fourth version should be ATN103B, the free-standing bed with no mounting holes. Can you confirm and rename N700186-03?',
  'I updated the model list to match your new variant names. SKU N700186-04 is still named "ATN101B - Free-Standing Bed with Bottom Closure." The free-standing bed with a bottom closure is the ATN103B (108 lbs), so it should be "ATN103B - Free-Standing Bed with Bottom Closure." The spec sheet calls the ATN101B "free-standing," but it has mounting holes, so "Floor-Mount" fits.'),
],
't.g9egfs3e2ylq':[
 ('It bolts securely to the floor','It bolts securely to the floor,','It comes in floor-mount and free-standing versions,'),
 ('ATN120 – Space-Saver Bed:','Space-Saver Bed:','Floor-Mount Bed:'),
 ('ATN123 – Space-Saver Bed, No Mounting Holes:','Space-Saver Bed, No Mounting Holes:','Free-Standing Bed:'),
 ('ATN123 – Space-Saver Bed, No Mounting Holes:','ATN120, 80 lbs','ATN120, no mounting holes, 80 lbs'),
 ('ATN150 – Space-Saver Bed:','Space-Saver Bed:','Floor-Mount Bed:'),
 ('ATN153 – Space-Saver Bed, No Mounting Holes:','Space-Saver Bed, No Mounting Holes:','Free-Standing Bed:'),
 ('ATN153 – Space-Saver Bed, No Mounting Holes:','ATN150, 85 lbs','ATN150, no mounting holes, 85 lbs'),
 ('ATN130 – Space-Saver Bed with Storage:','Space-Saver Bed with Storage:','Floor-Mount Bed with Storage:'),
 ('ATN133 – Space-Saver Bed with Storage, No Mounting Holes:','Space-Saver Bed with Storage, No Mounting Holes:','Free-Standing Bed with Storage:'),
 ('ATN133 – Space-Saver Bed with Storage, No Mounting Holes:','ATN130, 140 lbs','ATN130, no mounting holes, 140 lbs'),
 ('Tamper-Resistant Glides: Optional','Optional for the ATN120, ATN150, and ATN130','Optional for the floor-mount models (ATN120, ATN150, and ATN130)'),
 ('Variant names: the ATN130','the ATN130 and ATN133 variants are named "Standard Bed (32Wx78L)," but the ATN130 is the bed with storage. Would you like the ATN130 variant renamed "ATN130 - Bed with Storage (32Wx78L)"?',
  'I updated the model list to match your new variant names (Floor-Mount Bed, Free-Standing Bed, and Bed with Storage).'),
],
't.rhqzebjztcyi':[
 ('is missing a space before the dash','The variant name "ATN145- 18” High" is missing a space before the dash.','Variant name: "ATN145 - 18” High" now has the space before the dash.'),
],
't.c8eiokwbz5lq':[
 ('Variant: the variant on this page','the variant on this page is named "ATN301," which is the three shelf unit. It should be renamed "ATN320."','the variant is now named "ATN320." It was "ATN301," which is the three shelf unit.'),
],
't.0':[
 ('Platform Bed: two variants','two variants are named "ATN101B." SKU N700186-03 looks like it should be ATN103B.','SKU N700186-04 is still named "ATN101B." By the new variant names it should be ATN103B.'),
 ('Space-Saver Bed: the ATN130','the ATN130 and ATN133 variants are named "Standard Bed," but the ATN130 is the bed with storage.','fixed with the new variant names.'),
 ('Two Shelf Storage Unit: the variant','the variant is named "ATN301," and the current description says "3-compartment."','the variant is now named "ATN320." The current description still says "3-compartment," which the new description fixes.'),
],
}
out={}
for t in doc['tabs']:
    tid=t['tabProperties']['tabId']
    if tid not in E: continue
    paras=[]
    for el in t['documentTab']['body']['content']:
        p=el.get('paragraph')
        if not p: continue
        runs=[(r['startIndex'],r['textRun']) for r in p['elements'] if 'textRun' in r]
        txt=''.join(tr['content'] for _,tr in runs)
        paras.append((el['startIndex'],txt,runs))
    ops=[]
    for anchor,old,new in E[tid]:
        m=[p for p in paras if anchor in p[1]]
        assert len(m)==1,(tid,anchor,len(m))
        st,txt,runs=m[0]
        assert txt.count(old)==1,(tid,old)
        # minimal diff
        a=0
        while a<min(len(old),len(new)) and old[a]==new[a]: a+=1
        b=0
        while b<min(len(old),len(new))-a and old[-1-b]==new[-1-b]: b+=1
        pos=txt.index(old)+a
        dels=old[a:len(old)-b]; ins=new[a:len(new)-b]
        s=st+U(txt[:pos]); e=s+U(dels)
        # style of preceding char vs deleted
        def style_at(i):
            for rs,tr in runs:
                if rs<=i<rs+U(tr['content']): return tr.get('textStyle',{})
        pre=style_at(s-1); cur=style_at(s)
        flag='' if (pre or {}).get('bold')==(cur or {}).get('bold') and 'link' not in (pre or {}) else ' !!STYLE'
        print(tid,s,e,repr(dels[:50]),'->',repr(ins[:60]),flag)
        ops.append((s,e,ins))
    ops.sort(key=lambda x:-x[0])
    # check overlap
    for i in range(len(ops)-1): assert ops[i+1][1]<=ops[i][0]
    req=[]
    for s,e,ins in ops:
        if e>s: req.append({'deleteContentRange':{'range':{'startIndex':s,'endIndex':e,'tabId':tid}}})
        if ins: req.append({'insertText':{'text':ins,'location':{'index':s,'tabId':tid}}})
    out[tid]=req
allreq=[r for tid in E for r in out[tid]]
json.dump(allreq,open(sys.argv[2],'w'),ensure_ascii=False)
print(len(allreq),'requests; rev',doc['revisionId'][:20])
