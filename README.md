# Export Sales - USDA | Historical weekly data 🌽

Python library to import **Exports and Sales weekly historical data** directly from the **FAS-USDA** (Foreign Agricultural Service - United States Department of Agriculture) web page.

## Features

- 📊 Scrapes USDA Export Sales tables for commodities like **soybeans, corn, wheat, soybean meal, soybean oil**.  
- ⏳ Filters data by start and end dates.  
- 📅 Flags each row with the correct **Market Year** (e.g., `2023/24`).  
- 🔄 Automatically cleans and formats the data into a `pandas.DataFrame`.  

---

## Installation
The library is intended to be used by importing a file or installing directly from a Git repository, as it appears to be a local script or private library.

```bash
pip install git+https://github.com/luizel-fx/exportSalesUSDA
```

## Usage
The library's core functionality is encapsulated in the exportSalesHist function. This function scrapes the relevant USDA web page, processes the data, and filters it by the specified date range.

The exportSalesHist function fetches, processes, and returns the historical weekly export sales data for a specified commodity within a given time frame.

### Arguments
| Parameter | Type | Description |
| :--- | :--- | :--- |
| `commCode` | `str` | The **FAS-USDA commodity code** for the desired product. |
| `beg` | `datetime` | The **start date** of the time series (inclusive). |
| `end` | `datetime` | The **end date** of the time series (inclusive). |

### Commodity codes
| Commodity | Code |
| :--- | :--- |
| **Soybeans** | `'h801'` |
| **Corn** | `'h401'` |
| **Soybean cake and meal** | `'h901'` |
| **Soybean oil** | `'h902'` |
| **Wheat** | `'h107'` |

### Returns
A pandas.DataFrame containing the weekly export sales data with the following columns:
| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| **Week Ending** | `datetime64` | The end date of the exports week. |
| **Weekly Exports** | `int` | Current market-year weekly exports (metric tons). |
| **Accumulated Exports** | `int` | Current market-year accumulated exports (metric tons). |
| **Net Sales** | `int` | Current market-year weekly net sales (metric tons). |
| **Outstanding sales** | `int` | Current market-year weekly outstanding sales (metric tons). |
| **Net Sales NMY** | `int` | **Next Market Year** weekly net sales (metric tons). |
| **Outstanding Sales NMY** | `int` | **Next Market Year** weekly outstanding sales (metric tons). |
| **Market Year** | `str` | The current market-year identification (e.g., `'2023/24'`). |

### Exemple
```python
from exportSales_USDA import exportSalesHist 
from datetime import datetime

# Define the date range for data retrieval
beg = datetime(2023, 9, 1) # Start of the period
end = datetime(2024, 8, 31) # End of the period

# Fetch historical data for Soybeans ('h801')
soybeansExports = exportSalesHist('h801', beg, end)

# Print the first few rows of the resulting DataFrame
print(soybeansExports.head())
```

## Data Source
All data is scraped directly from the historical data tables provided by the USDA Foreign Agricultural Service (FAS) at the respective commodity pages, for example: https://apps.fas.usda.gov/export-sales.

## License
MIT License. Free to use and modify.
