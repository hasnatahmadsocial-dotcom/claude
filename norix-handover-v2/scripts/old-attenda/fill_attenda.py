import openpyxl,re,copy,sys
f='Worksheet_Norix_weights_dimensions.xlsx'
wb=openpyxl.load_workbook(f);ws=wb['Sheet1']
M={'ATN101':(110,84,40,15.5),'ATN101B':(115,84,40,15.5),'ATN103':(110,84,40,15.5),
'ATN120':(80,79,31,15),'ATN123':(80,79,31,15),'ATN150':(85,80,32,15),'ATN153':(85,80,32,15),
'ATN130':(140,78,32,22.6),'ATN133':(140,78,32,22.6),
'ATN140':(125,92.8,38.5,25.4),'ATN140H':(125,92.8,38.5,25.4),'ATN145':(138,92.8,38.5,30.4),'ATN145H':(138,92.8,38.5,30.4),
'ATN250':(30,22,22,23.3),'ATN255':(33,22,22,24),'ATN301':(50,27,13.8,53.5),'ATN310':(22,31,13,21),
'ATN401':(69,27,13.8,68),'ATN500':(9.5,16.5,16.5,16),'ATN601':(48,35.6,23.7,30.1),
'ATN625':(65,35.5,23.7,24.8),'ATN620':(45,35.5,23.7,23.8),'ATN621':(45,35.5,23.7,23.8),
'ATN700':(63,30,18,42),'ATN750':(76,30,18,42.8),'ATN800':(75,26,24,78.4),'ATN801':(80,26,25.5,78.4)}
BYSKU={'N700186-03':(108,84,40,15.5),'N700304':(31,18,17,36)}
n=0
for r in ws.iter_rows(min_row=2):
    h=str(r[0].value or '')
    if 'attenda' not in h: continue
    sku=str(r[8].value or '').strip(); opt=str(r[5].value or '')
    m=re.match(r'(ATN\d+[A-Z]?)',opt)
    vals=BYSKU.get(sku) or M[m.group(1)]
    row=r[0].row
    for j,v in enumerate(vals):
        c=ws.cell(row=row,column=14+j); src=ws.cell(row=row,column=13)
        c.value=v
        if src.has_style: c._style=copy.copy(src._style)
        c.number_format='General'
    n+=1; print(row,sku,opt[:30],vals)
print('rows',n)
wb.save(f)
