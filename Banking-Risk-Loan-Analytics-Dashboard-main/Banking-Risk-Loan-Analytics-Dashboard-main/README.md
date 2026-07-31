# Banking Risk & Loan Analytics Dashboard (Power BI)

## Project Overview

This project focuses on risk analytics in banking and financial services, using Power BI to create interactive dashboards that help banks assess loan repayment likelihood and minimize financial loss. It analyzes client profiles, cleans data, calculates KPIs for loans, deposits, and risk, and visualizes insights for actionable decision-making.

### Core Problem Statement
Develop a basic understanding of risk analytics in banking and financial services and understand how data is used to minimise the risk of losing money while lending to customers.

### Solution
The dashboard enables banks to make data-driven decisions on loan approvals by instantly assessing the applicant’s profile against key risk indicators and financial history. It helps determine if an applicant is likely to repay a loan, thereby mitigating lending risk.

---

## Dashboard Key Features & Views

The dashboard is structured into multiple pages, offering a 360-degree view of the bank's client portfolio and financial status:

| Dashboard View | Primary Focus | Key Metrics |
| :--- | :--- | :--- |
| **Home / Summary** | High-level performance snapshot and critical risk exposure metrics. | Total Clients, Total Loan, Total Deposit, Total Fees. |
| **Loan Analysis** | Deep dive into lending activities and borrower risk profiles. | Bank Loan by Income Band, Business Lending Volume, Credit Card Balance trends. |
| **Deposit Analysis** | Insights into client liquidity and funding sources. | Total Deposit, Savings Account balances, Foreign Currency Amounts. |
| **Summary Dashboard** | A concise, executive-level summary of performance over time. | Engagement Length, Processing Fees, and key ratios. |

## 📊 Dashboard Visualizations

Here are screenshots of the main dashboard views, showcasing the Power BI design and key insights:

### 1. Home Dashboard

This is the entry point to the report, providing navigation and an immediate, high-level overview of total clients, key monetary figures, and global distribution.

<img width="1203" height="663" alt="Home" src="https://github.com/user-attachments/assets/a164f9a6-d193-456b-b65a-f084e01fea42" />

### 2. Loan Analysis Dashboard

This page focuses on loan distribution, risk segmentation by income band and lending activities. It is crucial for the primary goal of minimizing lending risk.

<img width="1176" height="654" alt="Loan Analysis" src="https://github.com/user-attachments/assets/83ded882-bf07-4d07-81cf-b9eba7374ae2" />

### 3. Deposit Analysis Dashboard

This view provides an overview of funding sources, including total deposits and distribution across different account types.

<img width="1167" height="649" alt="Deposit Analysis" src="https://github.com/user-attachments/assets/60426b50-78e0-4d11-9962-a1ba2bf1b65e" />


### 4. Summary Dashboard

A high-level view providing executive insights into client engagement, overall financial performance and key metrics over time.

<img width="1659" height="913" alt="Summary" src="https://github.com/user-attachments/assets/b1dc7d57-3da1-497b-a0b9-559c8a302610" />



---

## Technical Stack & Data Model

* **Primary Tool:** Microsoft Power BI Desktop
* **Modeling Language:** Data Analysis Expressions (DAX)
* **Source Data:** Multiple interlinked tables including `Banking Relationship`, `Client-Banking`, `Gender`, `Investment Advisor`, and `Period`.

### Data Preparation Highlights

* **Income Band Creation:** Categorized clients into **Low** (`< 100,000`) and **Mid** (`< 300,000`) income bands to segment risk profiles.
* **Engagement Timeframe:** Calculated the duration (in `Engagment Days`) a client has been associated with the bank since their joining date.
* **Processing Fees:** Introduced a calculated column for processing fees based on the `Fee Structure` column.

### Key Performance Indicators (KPIs)

| Metric | Calculation / Definition |
| :--- | :--- |
| **Total Loan** | Sum of Bank Loan, Business Lending, and Credit Cards Balance. |
| **Total Deposit** | Sum of all client accounts: Bank Deposit, Savings, Foreign Currency, and Checking Accounts. |
| **Total Fees** | Total amount charged for account setup and maintenance. |

## Future Enhancements

* **Investor Profiling:** Segmenting investors to understand the total loan amount across specific investor types.
* **Market Strategy:** Analyzing which type of banks (e.g., private) have more clients to help other banks build strategies to increase their client base.
* **Geographical Risk:** Providing insights about which nationality has the highest bank loans to assess foreign market exposure.

## How to Use

1.  **Download:** Ensure you have **Power BI Desktop** installed.
2.  **Clone:** Clone this repository to your local machine.
3.  **Open:** Open the `Banking Dashboard.pbix` file directly with Power BI Desktop.
4.  **Explore:** Interact with the slicers and filters to generate customized risk and performance reports.

---
*Created by Utkarsh Jha*

***

