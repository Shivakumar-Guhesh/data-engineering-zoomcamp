import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    data = pd.DataFrame()

    base_url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green'
    files = ['green_tripdata_2020-10.csv.gz','green_tripdata_2020-11.csv.gz','green_tripdata_2020-12.csv.gz']
    for file in files:
        url = f'{base_url}/{file}'
        print(url)
    
        taxi_dtypes = {
            'VendorID': 'Int64',
            'store_and_fwd_flag': 'str',
            'RatecodeID': 'Int64',
            'PULocationID': 'Int64',
            'DOLocationID': 'Int64',
            'passenger_count': 'Int64',
            'trip_distance': 'float64',
            'fare_amount': 'float64',
            'extra': 'float64',
            'mta_tax': 'float64',
            'tip_amount': 'float64',
            'tolls_amount': 'float64',
            'ehail_fee': 'float64',
            'improvement_surcharge': 'float64',
            'total_amount': 'float64',
            'payment_type': 'float64',
            'trip_type': 'float64',
            'congestion_surcharge': 'float64'
        }
        # pd.read_csv(url, sep=",",compression="gzip",dtype=taxi_dtypes,parse_dates=parse_dates)
        df =  pd.read_csv(url, sep=',', compression='gzip',dtype=taxi_dtypes)
        # print(df)
        data = pd.concat([data, df], ignore_index=True)
        print(data.size)
    # response = requests.get(url)

    # return pd.read_csv(io.StringIO(response.text), sep=',')
    return data

# @test
# def test_output(output, *args) -> None:
#     """
#     Template code for testing the output of the block.
#     """
#     assert output is not None, 'The output is undefined'
# https://github.com/DataTalksClub/nyc-tlc-data/releases/tag/green/download
# https://github.com/DataTalksClub/nyc-tlc-data/releases/tag/green/download/green_tripdata_2020-10.csv.gz
# https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-10.csv.gz