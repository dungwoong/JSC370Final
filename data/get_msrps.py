import pandas as pd
import time

def get_tbl(make, model, year):
    # it is a miracle that this works.
    url = f"https://www.motortrend.com/cars/{make.replace(' ', '-')}/{model.replace(' ', '-')}/{year}/"
    dfs = pd.read_html(url)
    return dfs[0]
    
def get_msrp_from_tbl(tbl):
    # Columns will be listed like 'market price' 'clean retail price' etc.
    if 'price' in tbl.columns[0].lower():
        item = tbl.iloc[0, 0]
    elif 'price' in tbl.columns[2].lower():
        item = tbl.iloc[0, 2]
    elif 'price' in tbl.columns[1].lower():
        item = tbl.iloc[0, 1]
    return item
	
def get_msrp(make, model, year):
	tbl = get_tbl(str(make).lower(), str(model).lower(), str(year).lower())
	return get_msrp_from_tbl(tbl)
    
def run(csvpath='brands2.csv'):
    df = pd.read_csv(csvpath)
    maxlen = len(df)
    for idx in df.index:
        try:
            row = df.iloc[idx, :]
            brand = row['brand']
            model = row['model']
            year = row['model_year']
            if not pd.isnull(row["MSRP"]):
                print(f"ALREADY DONE {year} {brand} {model}")    
                continue
            msrp = get_msrp(brand, model, year)
            df.loc[idx, 'MSRP'] = msrp
            df.to_csv(csvpath, index=False)
            print(f"{idx}/{maxlen}: {year} {brand} {model}: {msrp}$")
            time.sleep(2)
        except Exception as e:
            print(f"\n\n an exception occurred for {year} {brand} {model}:\n {str(e)}\n\n")
            time.sleep(2)
         
if __name__ == "__main__":
    run()