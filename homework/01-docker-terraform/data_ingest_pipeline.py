import pandas as pd
from sqlalchemy import create_engine

# from time import time

file_name = input("Enter file name (relative path) :")
user_name = input("Enter user_name :")
password = input("Enter password :")
host = input("Enter hostname :")
port = input("Enter port :")
db_name = input("Enter db name :")
table_name = input("Enter table name :")

# start_time = time()

df = pd.read_csv(file_name)

engine = create_engine(
    f"postgresql://{user_name}:{password}@{host}:{port}/{table_name}"
)

df.head(n=0).to_sql(name=table_name, con=engine, if_exists="replace")

# end_time = time()

# print(f"Created {table_name}. Took {end_time-start_time}.")
