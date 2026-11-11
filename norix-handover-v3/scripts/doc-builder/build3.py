import re
U16=lambda s: len(s.encode('utf-16-le'))//2
LINKC={'color':{'rgbColor':{'red':0.06666667,'green':0.33333334,'blue':0.8}}}
def parse(md):
    out='';bold=[];links=[];i=0
    tok=re.compile(r'\*\*(.+?)\*\*|\[([^\]]+)\]\(([^)]+)\)')
    for m in tok.finditer(md):
        out+=md[i:m.start()]
        if m.group(1) is not None:
            s=U16(out); out+=m.group(1); bold.append((s,U16(out)))
        else:
            s=U16(out); out+=m.group(2); links.append((s,U16(out),m.group(3)))
        i=m.end()
    out+=md[i:]
    return out,bold,links
def build(tab,items,start=1):
    text='';paras=[];bolds=[];links=[]
    for kind,md in items:
        t,b,l=parse(md)
        assert '\n' not in t
        s=start+U16(text); text+=t+'\n'; e=start+U16(text)
        paras.append((kind,s,e))
        bolds+=[(s+a,s+c) for a,c in b]; links+=[(s+a,s+c,u) for a,c,u in l]
    R=[{'insertText':{'text':text,'location':{'index':start,'tabId':tab}}}]
    R.append({'updateTextStyle':{'range':{'startIndex':start,'endIndex':start+U16(text),'tabId':tab},'textStyle':{},'fields':'bold,link,underline,foregroundColor'}})
    sty={'h1':'HEADING_1','h2':'HEADING_2','h3':'HEADING_3'}
    for k,s,e in paras:
        if k in sty: R.append({'updateParagraphStyle':{'range':{'startIndex':s,'endIndex':e,'tabId':tab},'paragraphStyle':{'namedStyleType':sty.get(k,'NORMAL_TEXT')},'fields':'namedStyleType'}})
    # bullet groups
    i=0
    while i<len(paras):
        k=paras[i][0]
        if k in('b1','n1'):
            j=i
            while j+1<len(paras) and paras[j+1][0]==k: j+=1
            R.append({'createParagraphBullets':{'range':{'startIndex':paras[i][1],'endIndex':paras[j][2]-1,'tabId':tab},'bulletPreset':'BULLET_DISC_CIRCLE_SQUARE' if k=='b1' else 'NUMBERED_DECIMAL_ALPHA_ROMAN'}})
            i=j+1
        else: i+=1
    for s,e in bolds: R.append({'updateTextStyle':{'range':{'startIndex':s,'endIndex':e,'tabId':tab},'textStyle':{'bold':True},'fields':'bold'}})
    for s,e,u in links: R.append({'updateTextStyle':{'range':{'startIndex':s,'endIndex':e,'tabId':tab},'textStyle':{'link':{'url':u},'underline':True,'foregroundColor':LINKC},'fields':'link,underline,foregroundColor'}})
    return R,text
