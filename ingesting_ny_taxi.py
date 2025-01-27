import pandas as pd
from sqlalchemy import create_engine

# df = pd.read_csv('green_tripdata_2019-10.csv', nrows=100)

engine = create_engine('postgresql://postgres:postgres@localhost:5432/ny_taxi')

# print(pd.io.sql.get_schema(df, name='green_taxi_data', con=engine))

df_iter = pd.read_csv('green_tripdata_2019-10.csv', iterator=True, chunksize=100000)
df = next(df_iter)

df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)

df.head(n=0).to_sql(name='green_taxi_data', con=engine, if_exists='replace')

while True:

    df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
    df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)

    df.to_sql(name='green_taxi_data', con=engine, if_exists='append')
    
    df = next(df_iter) 
    print('inserted another chunk...')
