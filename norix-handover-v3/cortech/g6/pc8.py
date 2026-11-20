# Cortech: last 3 tabs (Nov 20). Written straight into the MAIN Cortech doc (Zeemal).
# Loaded after pc6.py / pc7.py (uses their constants). Checks: python3 -I mc8.py
P=[]
def add(**k): P.append(k)

# 1. HookMax HM + HookMax+ HMP combined (Andrew, HM tab: "Rewrite, combine HM and HMP into 1 product.
#    Use HM - keep this url, use C601082-01, -02". H1 = his text. "HMP was deleted and redirected".)
add(tab='HM / HMP - Cortech HookMax Wall Hooks (Combined)',
 short='HM / HMP: Cortech Ligature Resistant Wall Hooks (Combined)',
 handle='cortech-hm-ligature-resistant-hookmax-wall-hook',src=[HOOKC+'hookmax/',HOOKC+'hookmax-plus/'],
 specs=[('HM',CU+'HookMax-Spec-Sheet.pdf'),('HMP',CU+'HookMax-Plus-Spec-Sheet.pdf')],
 h1='Cortech Ligature Resistant Wall Hooks – HookMax / HookMax+ / HM / HMP',
 cur_h1='Cortech Ligature Resistant HookMax Wall Hook - HM',
 sub='Flexible Wall Hooks That Bend and Release at a Maximum 10 or 20 lb Load, Sold in Packs of 5',
 cur_sub='Cortech USA HM Hookmax Anti-Ligature Hooks',
 intro=['The **Cortech Ligature Resistant Wall Hooks** hold clothing and towels in resident rooms, bathrooms, and common areas of behavioral healthcare and correctional facilities. The HookMax releases at a maximum load of 10 lbs and the HookMax+ at 20 lbs: the hook bends, the item or ligature slides off, and the hook returns to its shape.',
  'Both hooks have a PC/ABS core with a flexible TPU outer piece that helps prevent injury, and they release in all directions, so they can be placed close to furniture and doors. They come in five colors and are sold in packs of 5.'],
 bullets=['**Models:** HookMax (HM) releases at a maximum 10 lb load; HookMax+ (HMP) releases at a maximum 20 lb load',
  '**Material:** PC/ABS core with a flexible TPU outer piece',
  '**Dimensions:** 1.24”W×0.85”D×2.05”H (each hook)',
  '**Release:** Releases in all directions (360°), then returns to its shape',
  '**Testing:** Load release tests with a string release the HookMax at a maximum of 10 lbs and the HookMax+ at a maximum of 20 lbs',
  '**Mounting:** Mount to a flat surface so the hook fits tightly against the wall',
  '**Care:** Resistant to alcohol and most detergents',
  '**Colors:** White, Gray, Black, Beige, or Magenta',
  '**Packaging:** Sold in packs of 5. Price is per pack',
  '**Warranty:** 3-year warranty for the intended use; full warranty against manufacturing defects',
  '**Country of Manufacture:** Designed and produced in Sweden'],
 models=['**HM – HookMax, 5 Pack:** HMWH - White, HMGY - Gray, HMBK - Black, HMBE - Beige, HMMG - Magenta',
  '**HMP – HookMax+, 5 Pack:** HMPWH - White, HMPGY - Gray, HMPBK - Black, HMPBE - Beige, HMPMG - Magenta'],
 install=[],
 apps=apps('The HookMax and HookMax+ suit rooms where residents need a place to hang clothing and towels without creating a ligature point.',
  ['Resident rooms and bathrooms in behavioral healthcare facilities and psychiatric hospitals','Cells and common areas in correctional facilities and jails','Residential treatment centers and shelters'],HOOK_COLL),
 series=HOOK_SERIES,
 mt='Cortech Ligature Resistant Wall Hooks - HM / HMP at Anchortex',
 md='Shop Cortech HookMax and HookMax+ ligature resistant wall hooks, flexible hooks that bend and release at a 10 or 20 lb load so ligatures slide off. Packs of 5.',
 notes=['Combined page: as you asked, this tab combines the HookMax (HM) and HookMax+ (HMP) on the HM page and keeps its address. The HMP page was deleted and redirected (your note).',
  'H1: I used your wording.',
  'Variants: you gave two SKUs, so there are two variants: "HM - Pack of 5" (C601082-01) and "HMP - Pack of 5" (C601082-02), both at the current price of $196.80 (compare-at $246.00), since the two pages had the same price. You also said yes to color variants. Five colors for each hook would make 10 variants and need 10 SKUs, so for now I listed the colors and Cortech part numbers under Available Models. Would you like 10 color variants? If so, please give the SKUs.',
  'Weight and size: the Cortech spec sheets do not give a weight, so both variants stay at 5 lbs. As you asked, the worksheet size is for a pack of 5, not one hook: I used 7”L×3”W×2”H as an estimate. Please correct it if you know the box size.',
  'Testing: the HookMax spec sheet says the test used a string, shoelace, or rope made from bedsheets; the HookMax+ spec sheet says a string in vertical and horizontal directions. I kept one shorter line for both.',
  'Mounting: the Cortech spec sheets say to mount the hook to a flat surface for a tight fit, but do not say how it attaches (screws or adhesive), so I left that out.',
  'I fixed the typo "jailsg" in the Applications list.',
  'Product images: the HM page has one image (HookMax). The HookMax+ photo was on the deleted HMP page. Would you like me to add a HookMax+ photo from the Cortech spec sheet?'])
