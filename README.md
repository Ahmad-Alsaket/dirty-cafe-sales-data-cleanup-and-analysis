# Dirty Cafe Sales: Data Cleanup and Analysis

A data-cleaning practice project in Python and pandas. It takes a deliberately messy cafe sales dataset and turns it into clean, correctly typed data ready for analysis.

## Dataset

The script expects the **"Cafe Sales - Dirty Data for Cleaning Training"** dataset from Kaggle, saved as:

```
data/dirty_cafe_sales.csv
```

The CSV isn't included in this repo. Download it from Kaggle and put it in a `data/` folder next to the script.

Columns: `Transaction ID`, `Item`, `Quantity`, `Price Per Unit`, `Total Spent`, `Payment Method`, `Location`, `Transaction Date`.

The data is dirty on purpose: it has missing values, placeholder strings such as `ERROR` and `UNKNOWN`, and numbers and dates stored as text.

## What the script does

`cafesales_analysis.py` runs these steps in order:

1. **Load:** reads the CSV.
2. **Summarize:** prints the first rows, the dtypes, the shape, and value counts for each column.
3. **Standardize missing values:** replaces `ERROR` and `UNKNOWN` with `NaN`.
4. **Report missing values:** prints the number of `NaN`s in each column.
5. **Trim strings:** strips extra whitespace from text columns.
6. **Check duplicates:** reports fully duplicated rows and duplicated transaction IDs. None were found.
7. **Fix dtypes:** converts `Quantity`, `Price Per Unit` and `Total Spent` to numbers, and `Transaction Date` to datetime. Values that can't be converted become `NaN`.
8. **Handle missing values:**
   - Drops rows with no `Transaction ID`, `Item` or `Transaction Date`.
   - Fills a missing `Total Spent` with `Quantity × Price Per Unit` where both are known. Rows where they aren't known keep `NaN` on purpose, rather than getting an invented total.
   - Fills missing `Quantity` and `Price Per Unit` with the column mean.
9. **Normalize:** adds `Total Spent Normalized` using max scaling (`x / x_max`), so values fall in [0, 1].

## Usage

```bash
pip install pandas numpy
python cafesales_analysis.py
```

## Possible improvements

- Recover missing `Quantity` or `Price Per Unit` from the other two values (`Total / Price`, `Total / Quantity`), or look up the price from `Item`, before falling back to an average.
- Use the median instead of the mean for `Quantity`, so filled values stay whole numbers.
- Clean up the missing `Payment Method` and `Location` values.
- Add analysis and visualizations on the cleaned data.
