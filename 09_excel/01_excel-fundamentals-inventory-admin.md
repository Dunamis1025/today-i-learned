# Excel Fundamentals for Inventory & Admin Roles

**Date:** 2026-11-22
**Context:** 1-hour hands-on practice session, built around a mock inventory dataset styled after an IT distribution company (similar structure to the systems used in Inventory Planner / Purchasing Officer roles I'm applying for).

## Why I did this

I've been applying for Inventory Planner / Product Administrator / Purchasing Officer roles that list Excel as a core skill (SUMIFS, VLOOKUP, filtering, pivot-style reporting). I had theoretical familiarity but no real hands-on muscle memory, so I built a practice workbook with a 30-row mock inventory table (SKU, Product Name, Category, Warehouse, Qty_On_Hand, Reorder_Level, Qty_On_Order, Unit_Cost, Supplier, Last_Stock_Check) and worked through realistic reporting tasks.

## Core concepts learned

### 1. Cross-sheet references (`SheetName!Range`)

To pull data from a different tab than the one you're working in, you prefix the range with the sheet name and an exclamation mark:

```
=SUM(Inventory_Data!E2:E31)
```

The `!` is just a separator between "which sheet" and "which cells" — conceptually like a building number and a unit number in an address. If you're referencing cells on the *same* sheet you're currently on, you don't need the prefix at all.

### 2. `SUM` — basic aggregation

```
=SUM(Inventory_Data!E2:E31)
```
Adds every value in the range. No conditions — just a total (e.g., total units on hand across all SKUs).

### 3. `SUMIF` — conditional aggregation (single condition)

```
=SUMIF(Inventory_Data!D2:D31, "VIC-Oakleigh DC", Inventory_Data!E2:E31)
```

Three arguments, in this order:
1. **Range to check the condition against** (Warehouse column)
2. **The condition itself** (must match exactly)
3. **Range to actually sum** (Qty_On_Hand column)

Mental model: "scan column D for rows that match the condition, then sum only the corresponding rows in column E."

### 4. `SUMIFS` — conditional aggregation (multiple conditions)

```
=SUMIFS(Inventory_Data!H2:H31, Inventory_Data!D2:D31, "VIC-Oakleigh DC", Inventory_Data!I2:I31, "ASUS AU")
```

Important gotcha: **the argument order is different from `SUMIF`.** In `SUMIFS`, the sum range comes *first*, then pairs of (criteria range, criteria) repeated for as many conditions as needed. This came up when I wanted to answer a realistic manager request: "What's the total unit cost of ASUS AU stock specifically in the VIC-Oakleigh DC warehouse?" — a two-condition (AND) query that plain `SUMIF` can't handle.

### 5. `COUNTIF` — conditional counting

```
=COUNTIF(Inventory_Data!I2:I31, "HP Direct")
```

Same logic as `SUMIF` but without a "sum range" — it just counts how many rows match the condition, rather than summing a related column.

### 6. `SUMPRODUCT` for comparing two columns row-by-row

```
=SUMPRODUCT((Inventory_Data!E2:E31 < Inventory_Data!F2:F31)*1)
```

This was the hardest one to parse. Breaking it into steps:
1. `E2:E31 < F2:F31` compares Qty_On_Hand against Reorder_Level **row by row**, producing an array of `TRUE`/`FALSE` values (one per row) — not a single result.
2. `*1` coerces each `TRUE`/`FALSE` into `1`/`0`. This is a type-conversion trick, not a logical comparison — distinct from something like an XNOR gate (which compares two values for equality); here we're just converting one boolean result into a number.
3. `SUMPRODUCT` adds up all those 1s and 0s, which is equivalent to counting how many rows satisfied the condition.

Net effect: counts how many SKUs currently have stock below their reorder level — i.e., how many items need reordering. This is the kind of row-by-row comparison that a single-column `COUNTIF` can't do, because the condition depends on *two different columns in the same row* rather than a fixed value.

### 7. `IF` — conditional display value, applied across a column

```
=IF(E2 < F2, "Yes", "No")
```

Structure: `IF(condition, value_if_true, value_if_false)`. Entered in one cell (e.g., K2), then extended down the full column by double-clicking the fill handle (the small square at the bottom-right corner of the selected cell) — this auto-fills the formula down while automatically adjusting the relative references (E2/F2 → E3/F3 → E4/F4, etc.). Produced a "Reorder_Needed?" column that flags Yes/No per SKU.

### 8. `VLOOKUP` and `INDEX`/`MATCH` — looking up a value by key

```
=VLOOKUP(B5, Inventory_Data!A:J, 8, FALSE)      ' looks up Unit_Cost (8th column)
=INDEX(Inventory_Data!H:H, MATCH(B5, Inventory_Data!A:A, 0))   ' same result, different approach
```

`VLOOKUP` is simpler to write but less flexible (can only look left-to-right, breaks if columns are inserted). `INDEX`/`MATCH` is the more robust modern equivalent and is considered the safer habit for real workbooks.

### 9. Sort and Filter (UI features, not formulas)

- **Sort:** `Data` tab → `Sort` → choose column + order (e.g., Qty_On_Hand, Smallest to Largest). Reversible with Ctrl+Z.
- **Filter:** `Data` tab → `Filter` → adds dropdown arrows to each header → check only the values you want visible (e.g., Category = "Networking"). This *hides* non-matching rows rather than deleting data; toggling Filter off restores the full view.

## Practical takeaway

The real skill isn't memorizing exact syntax — it's being able to translate a plain-language request (e.g., "tell me the total value of ASUS stock in the Oakleigh warehouse") into the right formula structure, and knowing *which* function fits which shape of problem:

| Need | Function |
|---|---|
| Total everything | `SUM` |
| Total, one condition | `SUMIF` |
| Total, multiple conditions | `SUMIFS` |
| Count, one condition | `COUNTIF` |
| Count based on comparing two columns per row | `SUMPRODUCT` with a boolean array |
| Flag/categorize each row | `IF` (+ fill handle to extend down a column) |
| Look up a value by a key elsewhere in the sheet | `VLOOKUP` / `INDEX`+`MATCH` |
| Reorder or temporarily narrow down what's visible | Sort / Filter (no formula needed) |

## Security note (practical, not just theoretical)

While practicing, I realized that in a real job I can't paste actual company data into an external AI tool to get help writing formulas — only the *structure* (column names, what I'm trying to calculate) is safe to describe externally, never real figures, customer names, or supplier pricing, unless the company has an approved/enterprise AI tool for that purpose.
