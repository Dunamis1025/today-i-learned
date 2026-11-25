# 02 – Excel Stock Check: Finding Discrepancies and Deciding What to Reorder

**Date:** 2026-11-25
**Topic:** Excel for inventory and warehouse administration (workplace-style practice)
**Follows:** [`01_excel-fundamentals-inventory-admin.md`](01_excel-fundamentals-inventory-admin.md)
**Practice file:** `Excel_Real_Work_Practice_01_Stock_Check.xlsx`

---

## 1. Why I am studying this

Most of the stock, inventory and coordinator roles I am applying for expect everyday Excel: comparing system stock with physical counts, finding what needs reordering, and looking up product details. My current level is **basic Excel**, so this is the skill where a short period of focused practice can make the biggest difference to my job prospects.

At CHILL I worked with CartonCloud and handheld scanners and reported differences between physical and system stock to my manager. This practice builds on that real experience, so I can explain what I learn in an interview.

## 2. Where I was before this session (Practice 00)

The first practice workbook covered the fundamentals across three sheets:

| Sheet | What it covered |
|---|---|
| `Inventory_Data` | 30 products with SKU, stock quantity, reorder level and supplier |
| `Lookup_Practice` | Looking up product details with `VLOOKUP` and `INDEX/MATCH` |
| `Exercises` | `SUM`, `SUMIF`, `COUNTIF`, `SUMPRODUCT`, `IF`, sorting and filtering |

That gave me a good base. The limitation was that the exercises told me *which function to use* ("calculate a SUMIF"). At work nobody does that. A manager asks a **question**, and I have to decide which tool answers it.

## 3. The new approach: start from a work situation, not a formula

From this session on, each exercise starts from a realistic request, and I choose the Excel tools myself.

> **Scenario:** I have just joined the stock control team of an IT distribution company. In the morning my manager says:
>
> *"Yunho, we've just finished our stocktake. Could you check the discrepancies and let me know which items need reordering?"*

**What it means:** "The physical stock count is finished. Please compare what we counted with what the system says, find the differences, and tell me which products we need to order again."

**Useful vocabulary**

| Term | Meaning |
|---|---|
| Stocktake | Counting the physical stock in the warehouse |
| Discrepancy | A difference between system stock and counted stock |
| System quantity | The quantity recorded in the computer system |
| Counted quantity | The quantity actually counted on the shelf |
| Reorder level | The quantity at or below which we need to order more |
| SKU | Stock keeping unit: the unique code for a product |

## 4. The practice workbook

`Excel_Real_Work_Practice_01_Stock_Check.xlsx` has four sheets:

| Sheet | Purpose |
|---|---|
| `01_Stock_Check` | System quantity vs counted quantity for 12 products |
| `02_Your_Tasks` | Eight tasks from the manager to solve |
| `03_Lookups` | Find product name, supplier and price from a SKU |
| `04_Hints` | Hints to use only when stuck |

Layout of `01_Stock_Check`: SKU, System Qty, Counted Qty and Difference (the formula in `F2` refers to the System Qty in column D and the Counted Qty in column E).

| SKU | System Qty | Counted Qty | Difference |
|---|---|---|---|
| SW-100 | 36 | 34 | -2 |
| RT-110 | 14 | 14 | 0 |
| KB-120 | 42 | 45 | +3 |

## 5. Task 1 – Calculate the difference for every product

**Formula in `F2`:**

```excel
=E2-D2
```

**How to read it:** Difference = Counted quantity − System quantity.

- **Negative number** → the shelf has *fewer* items than the system says (a shortage).
  `SW-100`: system 36, counted 34, so the difference is **-2** (2 items missing).
- **Zero** → counts match. `RT-110`: 14 and 14.
- **Positive number** → the shelf has *more* items than the system says (an overage).
  `KB-120`: system 42, counted 45, so the difference is **+3**.

**Copying the formula down (fill handle):**
1. Click `F2`.
2. Drag the small square at the bottom-right corner of the cell down to `F13`.
3. Excel adjusts the row numbers automatically (`F3` becomes `=E3-D3`, and so on).

**Next question to answer:** how many products have a shortage (negative difference)?

> **Key point:** The goal is not to memorise a formula. The goal is to understand *why* I calculate it and what action follows when stock does not match.

## 6. What a discrepancy means in real work

When the count and the system disagree, the usual professional steps are:

1. Confirm the count is correct (recount if the difference is large).
2. Record the product, the quantities and the difference.
3. Report it to the manager (or the person responsible for stock adjustments).
4. Hand over clearly so the next shift knows the status.

This matches what I actually did at CHILL: I **recorded** differences, **reported** them to the manager and **handed over**. I did not investigate root causes, and I should not claim that in an interview.

## 7. Excel toolkit for stock control

Formulas below are written as generic examples. Adjust the ranges to the actual sheet.

| Question from the manager | Tool | Example |
|---|---|---|
| What is the difference between the system and the count? | Subtraction | `=E2-D2` |
| Which products have a shortage? | `IF` | `=IF(F2<0,"Shortage",IF(F2>0,"Overage","OK"))` |
| How many products have a shortage? | `COUNTIF` | `=COUNTIF(F2:F13,"<0")` |
| What is the total shortage? | `SUMIF` | `=SUMIF(F2:F13,"<0")` |
| Which items need reordering? | `IF` comparing stock with the reorder level | `=IF(E2<=ReorderLevel,"Reorder","OK")` |
| What is the stock value? | `SUMPRODUCT` | `=SUMPRODUCT(Qty_Range,Price_Range)` |
| What is the supplier of this SKU? | `VLOOKUP`, `INDEX/MATCH`, or `XLOOKUP` | `=XLOOKUP(SKU,SKU_Range,Supplier_Range)` |
| Show me only the problem items | Filter | Filter on the Difference column |
| Put the biggest shortages first | Sort | Sort the Difference column from smallest to largest |

**Lookup functions in short**

- `VLOOKUP`: finds a value in the first column of a table and returns something from a column to its right. Simple, but breaks if columns are inserted.
- `INDEX/MATCH`: more flexible; `MATCH` finds the row, `INDEX` returns the value.
- `XLOOKUP`: the modern replacement; it looks in one column and returns from another, with a clear "if not found" option. It is the next function on my list (available in current Microsoft 365 versions of Excel).

## 8. Plan for the next steps

Checklist (tick when done and understood well enough to explain):

- [ ] Task 1: fill the Difference formula down to row 13
- [ ] Count how many products have a shortage (`COUNTIF`)
- [ ] Flag each row with `IF` (Shortage / OK / Overage)
- [ ] Total shortage and total overage (`SUMIF`)
- [ ] Reorder decision: compare stock with the reorder level
- [ ] Look up product name, supplier and price from a SKU (`XLOOKUP`)
- [ ] Filter and sort to show only the problem items
- [ ] Finish the eight tasks in `02_Your_Tasks`
- [ ] Rebuild the same stock check on a blank sheet without the hints

## 9. Interview-ready explanation (English practice)

Short answers I can say aloud:

- *"I use Excel for basic stock checks. I compare the system quantity with the counted quantity, calculate the difference, and highlight the items that need attention."*
- *"When I find a difference, I record it and report it to my manager. I do not change stock records myself unless I am authorised."*
- *"I am practising `SUMIF`, `COUNTIF`, `IF` and lookups using realistic stocktake data, and I am learning `XLOOKUP`."*

**Be careful not to say:** that I am advanced in Excel, or that I investigated causes of stock differences at CHILL. My level is basic and improving, and my CHILL role was to record, report and hand over.

## 10. Daily study plan agreed today

| Block | Time | Focus |
|---|---|---|
| Excel practice | 45 min | Stock check workbook: filters, sorting, `SUMIF`, `COUNTIF`, `XLOOKUP`, system vs counted stock |
| English practice | 30 min | Australian English from TV dialogue; describe scenes in my own words, with a focus on natural speaking |

**Why Excel first:** the roles I am applying for (inventory records, stock planning, purchasing and logistics data, record tracking) use Excel often, and my Excel is the weaker skill, so a short period of practice gives the largest gain. English remains the more valuable long-term skill, especially real-time listening on the phone.

## 11. Status

- Practice 01 workbook created and opened.
- Task 1 explained (Difference formula and fill handle). Results to be checked next session.
- Remaining tasks listed in section 8.
