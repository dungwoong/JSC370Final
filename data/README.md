# Dataset

## kijiji_data_fullset.csv

Sourced from: [https://github.com/Pyligent/Car_ETL_PROJECT](https://github.com/Pyligent/Car_ETL_PROJECT)

Records are Kijiji car listings in the Greater Toronto Area, scraped in 2019.

Columns of interest:

 - brand: Brand of the car(eg. Honda)
 - model: model(eg. Honda Civic --> model=Civic)
 - model_year: year of the model(eg. 2001 Honda Civic --> year=2001)
 - list_price: listing price on kijiji
 - color: color of the car
 - condition: new/used
 - body_type: eg. truck, sedan, SUV
 - wheel_config: eg. RWD, AWD, etc.
 - transmission: manual/automatic/other transmission
 - fuel_type: fuel type used by the car
 - mileage: mileage
 - dealer_address: address of the listing
 
## brands.csv

Retail prices/fair market prices of the cars listed in the dataset above, scraped from MotorTrend.com in 2023.

Scraped by me using [this script](get_msrps.py)

_although the script was originally meant to collect MSRPs, I decided to collect market price data instead_

Columns:

 - brand
 - model
 - model_year
 - Price: market price/clean retail price
  - A reasonable asking price by a dealership for a fully reconditioned vehicle(clean history, no defects, minimal wear)
  - I believe these prices are in USD.