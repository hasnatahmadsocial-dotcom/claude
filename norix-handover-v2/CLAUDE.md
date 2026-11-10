# Anchortex Norix PDP SEO Project (handover v2, Nov 10, 2026)

Read this whole file before doing anything. It replaces the older handover.

## Who and what
- I am Zeemal, a freelancer. The client is Andrew at Anchortex (anchortex.com, a Shopify store).
- The job is SEO rewrites of Norix product pages (PDPs).
- Workflow:
  1. Draft each product in a Google Doc tab.
  2. Andrew comments in the doc.
  3. I move approved pages into Shopify one product at a time.
  4. I say "check live" and you run the full review on the live page.
- I work mostly from my phone. Keep replies short and direct. Don't recap.
- Mark every passing item with ✅ and every problem with ⚠️. I want to see the green ones too.
- Don't make mistakes. Count carefully (I once caught "21 products" when there were 20). When you're unsure, check the spec sheet, the price list, and the live store before answering.
- When I ask "is this 100% right?", re-verify against the spec sheet AND the price list, then show a table.

## How Andrew comments (important)
- Andrew does NOT use Google Docs margin comments. He types inline:
  - Highlighted text (backgroundColor) = his additions, answers, or instructions.
  - Strikethrough = his deletions.
- Detect his comments as text runs with a background highlight or strikethrough (see scripts/cmp2.py, which marks them [HL ...] and [STRIKE ...]).
- To see what's new since your last read, diff the doc against doc-snapshot/doc_snapshot.json.
- Some comments "apply to everything". When he gives a rule on one tab, apply it to all similar products.
- Andrew prefers to set prices in bulk via his spreadsheet. Asking about prices in the doc is slow for him.

## Google Doc
- Original doc: "Norix PDP SEO Project", https://docs.google.com/document/d/15xqsq7FILOKO2A3vmjtQ08xCHRLj_XBT8YplTS5T4os/edit
- I may give you a COPY of this doc under another Google account. A copy has a different doc ID, and tab IDs may change.
  - Always read the doc first.
  - Find tabs by TITLE.
  - doc-snapshot/doc_tabs.txt lists the 52 tabs in order, with titles and old IDs.
- The doc is huge (about 2.4 MB of JSON), so read_doc saves to a file. Parse it with Python.
- Indices are UTF-16.
- New tabs: use addDocumentTab, then insertText plus styling (scripts/doc-builder/build3.py does this).
- Tab format:
  - Tab title is "MPN - Name" (max 50 characters).
  - First line is an H1 "MPN: Name", followed by the Product URL, Manufacturer page and Spec sheet links.
  - HEADING_2 sections:
    - Recommended H1 and Subtitle
    - Revised Product Description
    - Meta Title and Description
    - Notes and Questions
  - On-page H2s are written as HEADING_3 with a "[H2] " prefix.
  - "Available Models and Options" and "Installation and Options" are bold paragraphs followed by bullets.
  - Notes are a numbered list.
  - The line "Headings marked [H2] should be set as H2 on the page." comes after the description heading.
- Doc notes must NOT say "I added this to the worksheet".

## Writing rules (always; includes every rule Andrew has given)
- No em dashes, ever. The en dash ( – ) is used ONLY:
  - in the H1, before the model numbers: "Norix Jupiter Cylinder Base Table with Round Top – CY3600 / CY4200 / CY4800"
  - in model bullet labels: "**CY3600 – 36” Round:**"
- Write like a person, not marketing filler. Don't use "Norix lists the..." phrasing.
- Links go to collections only, never to individual products (Andrew: don't over-emphasize single products).
  - Standard links:
    - /collections/bh-behavioral-healthcare-furniture
    - /collections/cd-correctional-furniture
    - /collections/norix-furniture
  - Ironman storage pages also use /collections/prison-and-detention-inmate-property-storage-solutions-garment-bags-boxes-storage-lockers
  - Stack-A-Bunk adds /collections/bh-shelter-transitional-housing (Andrew asked)
- Weights and dimensions come from the current Norix spec sheet. If the price list or the current page disagrees, use the spec sheet and say so in the Notes.
- Meta title: 50 to 65 characters, adding " at Anchortex" if it fits. Meta description: 140 to 160 characters.
- "About Norix Furniture" paragraph (Andrew added "police stations"; use it on every page):
  "Norix manufactures durable furniture for demanding environments, including behavioral healthcare facilities, psychiatric hospitals, police stations, correctional institutions, and residential treatment centers. Explore the full line of Norix Furniture at Anchortex."
- Tables:
  - "Plain Top", never "Solid Top": in text, bullets ("Plain Top Finishes:"), model lines, subtitles, meta, and variant names. Plain means "not game top". The DuoForm variant also keeps "Plain Top" (Andrew).
  - Game Top bullet starts with "Optional": "**Game Top:** Optional Titanium Evolve laminate…"
- Standard fractions where practical (1½”, 1¼”, 1¾”, 1⅝”, 2½”, ¼”, 8⅜”). Leave odd decimals (29.3”, 31.1”).
- No spaces in dimensions: 30”×72”, 6”×6”×¼”, 17”W×16”D. The leg protector is written "3” diameter, 6” high".
- "see Norix instructions", without "the".
- Use Norix model numbers (M44200 not M4-4200; O43048 not O4-3048). Andrew confirmed.
- Max-Master: remove the stainless steel seat list prices (e.g. "($780 list for a set of 6)").
- Molded X-Base Square: the "Laminate Top" bullet label, and Top Attachment comes below the DuoForm Top bullet.
- X-Base: "x-shaped base" (Andrew's wording) and his new subtitles.
- NEW table series sentence (Andrew, latest). Use on ALL table pages:
  "Norix tables are made for dayrooms, dining halls, classrooms, and visitation areas in correctional and behavioral healthcare facilities, where furniture is used hard every day. The range covers molded-base tables such as the Jupiter, Evvolve, and Molded X-Base; Laminate X-Base tables; and steel-base tables such as the Leg Style, Multi-Purpose, Max-Master, and Oasis."
  - OLD sentence (currently live on 18 table pages): "...The range covers molded-base tables such as the Jupiter and Molded X-Base, laminate X-Base tables, and steel-base tables such as the Leg Style, Multi-Purpose, Max-Master, and Oasis."
- Ironman series section: Andrew's version (see the Tank Box tab). For Stack-A-Bunk it also has the line "**Temporary Bunks:** Stack-A-Bunk stackable sleep surfaces for overcrowding and emergency bunking" (Andrew approved).
- Image rules:
  - No alt text.
  - Andrew allows more than 5 images ("Keep it").
  - Don't delete or replace images without his approval.

## Shopify rules
- Don't change URLs, SKUs, or prices unless Andrew approved it in the doc. Quote his note when you do.
- Prices are 80% of the Norix list price. Compare-at price = the Norix list price. Check compare-at too.
- Weights: replace the 255 lb placeholders with the real weight. Game top variants weigh the same as plain.
- VARIANT OPTIONS (we got burned on M63072):
  - Have Zeemal edit each variant's own page.
  - Change only the field that needs changing (e.g. the Type value "…Solid Top" → "…Plain Top").
  - Never type "Type / Options" together into one field.
  - Never delete option values in the "Edit options" box, because that deletes variants.
- Give SKUs with worksheet rows.

## What to give me for each product (the "Shopify set")
1. Short list of Andrew's changes applied, plus any ⚠️ questions first.
2. H1, Subtitle, SEO title (with length), SEO description (with length), each in its own code block.
3. Description HTML in one code block. Generate it with scripts/tab2html2.py from the doc tab, then apply Andrew's rules. Fix:
   - empty `<li></li>` left by struck bullets
   - double spaces left by struck words
   - Andrew's instruction text (e.g. "[remove 'the'…]")
4. Variant table: position, name (and what changes), SKU, weight (and price / compare-at if they change).
5. "Images: keep all N" (or what to add).
6. Worksheet block, tab-separated: `SKU	Weight	L	W	H` (Zeemal also accepts Weight L W H only), with Andrew's Row # range.
7. A ✅ / ⚠️ verification table: value vs spec sheet vs price list. Then: prices are 80% of list ✅, compare-at = list ✅.
8. "Don't change the URL, SKUs, prices…", then "Say "check live" when it's saved."

Save the HTML as shopify-html/<CODE>.html, because the review script compares against it.

## "check live" = full review, every time
```
python3 -I scripts/review.py <handle> shopify-html/X.html "<subtitle>" "<seo title>" "<seo desc>" baselines/.../<handle>.json
python3 -I scripts/sweep.py <handle>
curl -s "https://www.anchortex.com/products/<handle>.json?x=$RANDOM"   # options, compare_at_price, weights
```
- review.py checks:
  - description = HTML file
  - SEO title and description text and length
  - subtitle (in `<p class="product-subtitle__new mpn">`)
  - no em dashes, H1 en dash
  - H2s
  - collection-only links that load
  - URL, SKU and price unchanged vs baseline
  - weights not 255/0, old variant names, duplicate SKUs, all images kept
- sweep.py checks:
  - $0 price or compare-at
  - price = 80% of compare-at
  - 255 lb weights
  - duplicate SKUs
  - "Solid" in names
  - doubled variant names
- Also check the options structure in .json (Type / Options values). Expected SKU or price changes (Andrew-approved) show up as "changed" issues; say they're expected.
- If the store returns the "Verifying your connection" bot page, retry. Store data can lag a minute after saving.
- `bash scripts/check_all.sh` re-checks all 33 published products (scripts/registry.json has each product's handle, HTML, subtitle, SEO title and description, and baseline).
- Report: ✅ list of everything that passed, ⚠️ list of what's missing, with exact values to set.

## Status (verified live Nov 10, 2026: all 33 published pages match shopify-html/ and pass sweep)
- Attenda (13), DONE:
  - ATN601, ATN101/103, ATN120/130/150, ATN140/145, ATN250/255, ATN301, ATN310, ATN320, ATN401, ATN500, ATN620/621/625, ATN700/750, ATN800/801
- 11/3 batch (20), DONE:
  - Boulder: C212, C213
  - Jupiter: Round, Square
  - X-Base: Laminate Round, Laminate Square, Molded Round, Molded Square
  - Leg Style: Rectangle, Round, Square
  - Max-Master: M44200, M63072, M65400, M83096, M86000
  - Multi-Purpose: Rectangle, Round, Square
  - Oasis
- Changes made with Andrew's approval:
  - Jupiter CY4242-DF price $960 (compare-at $1,200)
  - Molded X-Base Round SKUs N700283-01..-04 (Andrew "yes")
  - Molded X-Base Square SKUs N700280-01..-05. ⚠️ Andrew did NOT answer the SKU question on that tab; we followed his Round answer.
  - Molded X-Base Square prices $1,400 / $1,629.60 / $1,520 / $1,749.60 / $1,360, compare-at $1,750 / $2,037 / $1,900 / $2,187 / $1,700 (Andrew "Correct")

## PENDING (in order)
1. **Stack-A-Bunk** (tab "B530-151 / B530-149 - Ironman Stack-A-Bunk", handle norix-stack-a-bunk-bed-platform). Apply Andrew's comments, then move to Shopify:
   - Applications: he added the bullet "Disaster relief shelters, Emergency shelters, mass care shelters, emergency night shelters, and transitional housing shelters" and asked "is this too many repeats of 'shelter'?". Suggested: "Disaster relief, emergency, mass care, night, and transitional housing shelters". There's also a stray ", in" he typed after "Overcrowding and emergency temporary bunking"; remove it.
   - The collection line becomes: "Explore Anchortex's Prison and Detention Furniture and Transitional Housing Furniture collections…". The link is /collections/bh-shelter-transitional-housing (returns 200). Reword "for more correctional furniture" to fit.
   - Variant renames (he said yes): "B530-151 - Standard, Twilight" and "B530-149 - Extra Large, Sand". ⚠️ His Worksheet_Norix_3 shows "B530-151 - Standard - Twilight" and "B530-149 - Extra Large - Sand", and the title "Norix Stack-A-Bunk Bed Platform - Space-Saving Platform Bed". Ask Zeemal which to use.
   - Weights: 30 / 36 lb (spec). The price list and page say 34 lb for the XL; spec sheet used.
   - Sizes: 32”W×75½”L and 32”W×82½”L, 8⅜” high.
   - Prices are already OK: $420.80 / $454.40, compare-at $526 / $568.
   - Worksheet rows 157 to 158.
2. **Evvolve Table** (tab "EV Series - Evvolve Table", handle norix-evvolve-table). Apply Andrew's comments, then move to Shopify:
   - Prices approved: 80% of list, compare-at = list (row order):
     - 36R 1120/1400, 36R Game 1440/1800
     - 42R 1280/1600, 42R Game 1600/2000
     - 48R 1440/1800, 48R Game 1760/2200
     - 36S 1200/1500, 36S Game 1520/1900
     - 42S 1360/1700, 42S Game 1680/2100
     - DuoForm 1000/1250
   - SKUs approved: N700284-01 … -11 in row order (worksheet rows 62 to 72).
   - The DuoForm variant keeps "Plain Top".
   - Add the Norix DuoForm photo (Andrew "yes").
   - Weights: 74 / 88 / 106 / 85 / 104 / 55 lb, height 31.1. Game = same as plain.
   - Use the NEW series sentence.
3. **Update the series sentence on the 18 published table pages** (Jupiter ×2, X-Base ×4, Leg Style ×3, Max-Master ×5, Multi-Purpose ×3, Oasis): old → new (see above). Also update shopify-html/*.html so review.py stays in sync. Andrew said "Yes" to adding Evvolve to all table pages.
4. **Double Pedestal** (tab "EV3696 / CY3696 - Double Pedestal Table"): NEW product, not on Anchortex.
   - Andrew will send the URL and SKUs. Create it in Shopify as a DRAFT product.
   - Proposed variants: "EV3696 - Evvolve Base" 196 lb, "CY3696 - Jupiter Base" 180 lb.
   - List $3,525 → price $2,820.
   - Open questions in the doc: bolt-down kit only for the Evvolve base; width 36” vs 30” (used 36”).
5. **Evvolve Jr.** (tab "EJ3600 / EJ3636 - Evvolve Jr. Table"): Andrew's latest note says "* Do not add Evvolve Jr. now - this is for children's facilities." ON HOLD. Zeemal hasn't decided whether to rename the tab "(On Hold)" or delete it. Ask; deleting needs confirmation.
6. **$0 prices waiting on Andrew** (not asked in the doc; Zeemal was to message him):
   - ATN320 (N700304): price 0, compare-at 1139 → suggest $911.20
   - ATN700 (N700305-01) and ATN750 (N700305-02): price and compare-at 0 → suggest $998.40 / $1,241.60, compare-at $1,248 / $1,552
7. Small typo: ATN101/103 variant N700186-04 is named "ATN103B- Free-Standing Bed with Bottom Closure". It's missing a space before the dash.
8. Tell Andrew about the new SKUs N700283-01..04 and N700280-01..05.
9. Earlier batch weights are STILL placeholders (checked live Nov 10):
   - Prodigy (currently 255): PRD100 130, PRD100B 130, PRD240 29, PRD600 50, PRD700 55, PRD801 200, PRD804 155, PRD802 168
   - DuraVision mirrors (currently 10/8): MFD 6.2 / 9.8; MHD 5.8 / 8.1 / 13.9; REC 6.8; RND 4.6; MQD 7.2 / 9.5
10. Andrew's Google Sheet for bulk pricing: https://docs.google.com/spreadsheets/d/1iLyzpRDqktrP3znzZ5suOaeadZkag7Qgxxa3OmxzSy4/edit. Zeemal wanted the Evvolve Norix list prices added: 1400, 1800, 1600, 2000, 1800, 2200, 1500, 1900, 1700, 2100, 1250, in row order EV3600 Plain … EV4242-DF. It needs a Google Sheets connector. Zeemal may have pasted them already; ask.

## Norix data quirks (already decided; spec sheet wins unless noted)
- Jupiter and Molded X-Base DuoForm heights: the spec gives inches (29.5” / 31.3”) but its cm matches the laminate height. Inches used.
- Leg Style Rectangle prices aren't readable in pricer.txt. Prices were left as they were (80% of compare-at).
- Multi-Purpose: 500 lb static load. The 30×60 is cheaper than the 24×60 in the Norix list ($1,646 vs $1,723). That's real.
- Oasis: no overall footprint given. The worksheet uses the top size 48/72 × 30, with H 34 (seat back).
- Max-Master worksheet L × W = overall footprint (76×76, 63×72, 88×88, 63×96, 94×94), H 31.8.
- The price list spells it "EVVOLVE" (double V). Evvolve tables are on pages 41 to 42; Evvolve Jr. and Double Pedestal are on page 43.
- ATN620: price list weights reversed. ATN320: depth cm typo. Several Attenda kg typos.

## Files in this folder
- data/
  - pricer.txt: Norix Price List April 2026 as text
  - brochure.txt, norix_design_guide.txt
  - spec-sheets/attenda, spec-sheets/tables-boulder (+ Tables_Guide_2026), spec-sheets/new-products (Stack-A-Bunk, Evvolve, DuoForm, Evvolve Jr, Double Pedestal)
  - worksheets/: Worksheet_Norix_1_with_Attenda.xlsx, Worksheet_Norix_2.xlsx (its "from original" tab has the variant renames), Worksheet_Norix_3.xlsx (the 11/3 rows have Date assigned 2026-03-11; has Andrew's Row # column)
  - norix-pages/: saved norix.com product pages
- shopify-html/: final published description HTML for every product (CODE.html), plus a few *_live.json snapshots
- baselines/: product JSON captured BEFORE we changed each product (for review.py)
- scripts/
  - review.py: full live review
  - sweep.py: price, weight, SKU and name sweep
  - check_all.sh: re-checks all 33 published products
  - registry.json: each published product's handle, HTML file, subtitle, SEO title, SEO description and baseline
  - cmp2.py: doc parser; use as `exec(open('scripts/cmp2.py').read().split('A=load')[0])`, then `load(docjson)` → {tabId: (title, lines with <b>, <a url>, [HL ], [STRIKE ])}
  - tab2html2.py: `python3 -I scripts/tab2html2.py <docjson> <tabId> shopify-html/X.html`; skips struck runs
  - doc-builder/: build3.py (markdown-ish → batchUpdate), p3.py / p4.py / p5.py (tab content), make3/4/5.py, verify3/4/5.py (re-read check)
  - old-attenda/: first-batch scripts
- doc-snapshot/
  - doc_snapshot.json: full doc JSON as of Nov 10, including Andrew's latest notes
  - doc_tabs.txt: tab order, titles and old IDs
  - andrew_notes_attenda.txt

## Tools you need
- Google Docs connector: read_doc and update_doc (batchUpdate).
- Google Sheets connector: for Andrew's pricing sheet.
- Python 3 with openpyxl, pdftotext, curl.
- Run Python that reads downloaded files with `python3 -I`.
