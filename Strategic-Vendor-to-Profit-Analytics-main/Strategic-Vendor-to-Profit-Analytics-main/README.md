# Strategic Vendor-to-Profit Analytics

Strategic Vendor-to-Profit Analytics is a vendor performance analysis project focused on turning raw purchasing, sales, and invoice data into a cleaner vendor summary for business insight.

## Project Structure

- `Analysis/` - Jupyter notebooks for exploratory data analysis and vendor performance review.
- `Dashboard/` - dashboard-related assets for reporting and visualization.
- `Dataset/` - source dataset files, including `vendor_sales_summary.csv`.
- `Documentation/` - project documentation.
- `ETL Scripts/` - scripts used to transform and load data, including `get_vendor_summary.py`.

## What The Project Does

- Combines purchase, sales, and freight data into a vendor-level summary.
- Cleans the output by normalizing columns and filling missing values.
- Adds profitability metrics such as gross profit, profit margin, stock turnover, and sales-to-purchase ratio.
- Supports analysis through notebooks and downstream dashboarding.

## ETL Workflow

The main ETL script is `ETL Scripts/get_vendor_summary.py`.

It:

1. Reads vendor-related tables from a SQLite database.
2. Aggregates purchase, sales, and freight data.
3. Cleans and enriches the merged summary.
4. Writes the final results back to `vendor_sales_summary`.

## Getting Started

### Requirements

- Python 3.x
- `pandas`
- `sqlite3` (included with Python)
- Jupyter Notebook or VS Code notebooks

### Run the ETL Script

```bash
python "ETL Scripts/get_vendor_summary.py"
```

This creates or updates a local SQLite database named `inventory.db` and writes the processed vendor summary table.

### Explore the Analysis

Open the notebooks in `Analysis/` to review the exploratory analysis and vendor performance findings.

## Notes

- The repository includes a project license in `LICENSE`.
- If you regenerate the summary data, make sure the SQLite database and source tables are available before running the ETL script.