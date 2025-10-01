import pandas as pd
from datetime import datetime

def scrap(url: str, beg: datetime, end: datetime):
    """
    Scraps the FAS-USDA web page.

    Args
    ------
    url: str - FAS-USDA web-page to the respective commodity;
    beg: datetime64 - The start date of time series
    end: datetime64 - The end date of time series

    Returns
    ------
    pd.DataFrame(): dataframe with columns...
        Week Ending: datetime64 - End of the exports week;
        Weekly Exports: int - Current market-year weekly exports;
        Accumulated Exports: int - Current market-year accumulated exports;
        Net Sales: int - Current market-year weekly net sales;
        Outstanding sales: int - Current market-year weekly outstanding sales;
        Net Sales NMY: int - Next market-year net sales;
        Outstanding Sales NMY: int - Next-market year outstanding sales.
    """

    df = pd.read_html(url)[0] # Read the table at FAS-USDA historical data
    df.columns  = df.iloc[1] + ' ' + df.iloc[2]                             # Changing the columns headers names
    df = df.iloc[4:].dropna().reset_index(drop=True)
    df.columns = list(df.columns[:-2]) + [colName + ' NMY' for colName in df.columns[-2:]]
    df['Week Ending'] = pd.to_datetime(df['Week Ending'])
    df = df[
          (df['Week Ending'] <= end) 
        & (df['Week Ending'] >= beg)
        ]

    return df.reset_index(drop = True)

def exportsMarketYearFlag(df: pd.DataFrame):
    """
    Creates a market-year flag for each week ending.

    Args
    ------
    df: pd.DataFrame - Export Sales dataframe

    Returns
    ------
    str: market-year flag
    """
    for i in range(0, len(df)):
        if df.loc[i, 'Weekly Exports'] == df.loc[i, 'Accumulated Exports']: # If accumulates exports, and weekly exports have the same value, it's the markets-year first week.
            year = df.loc[i, 'Week Ending'].year
            df.loc[i, 'Market Year'] =f'{year}\{str(int(year[-2:]) + 1)}'
        else: pass
    return df.fillna(method = 'ffill').dropna()

def exportSalesHist(commCode: str, beg: datetime, end: datetime):
    """
    Uses the scrap() and exportsMarketYearFlag() functions to 

    Args
    ------
    commCode: str - Commodity code...
        Soybeans: h801,
        Corn: h401,
        Soybean cake and meal: h901,
        Soybean oil: h902,
        Wheat: h107;
    beg: datetime64 - The start date of time series;
    end: datetime64 - The end date of time series.

    Returns
    ------
    pd.DataFrame(): dataframe with columns...
        Week Ending: datetime64 - End of the exports week;
        Weekly Exports: int - Current market-year weekly exports;
        Accumulated Exports: int - Current market-year accumulated exports;
        Net Sales: int - Current market-year weekly net sales;
        Outstanding sales: int - Current market-year weekly outstanding sales;
        Net Sales NMY: int - Next market-year net sales;
        Outstanding Sales NMY: int - Next-market year outstanding sales;
        Market Year: str - Current market-year identification.
    """
    url = f"https://apps.fas.usda.gov/export-sales/{commCode}.htm"
    return exportsMarketYearFlag(scrap(url, beg, end))