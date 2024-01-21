import argparse
import os
from time import time
import pandas as pd
from sqlalchemy import create_engine
import warnings

warnings.simplefilter(action="ignore", category=FutureWarning)


def format_date(df):
    df = df.apply(
        lambda col: pd.to_datetime(col, errors="ignore")
        if col.dtypes == object
        else col,
        axis=0,
    )
    return df


def ingest_data(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url

    # csv_name = "output.csv"
    # csv_zip_name = csv_name + ".gz"

    file_name = os.path.basename(url)
    print(f"Filename: {file_name}")
    # download the csv
    if url.endswith(".gz"):
        print("Found gz file")
        os.system(f"wget {url} -O {file_name}")
        os.system(f"gzip -d {file_name}")
        file_name = ".".join(file_name.split(".")[0:-1])
        # file_name = file_name.split(".")[0]
        # print(f"New file_name, {file_name}")

    else:
        os.system(f"wget {url} -O {file_name}")

    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")

    print(f"Trying to read {file_name}")
    df_iter = pd.read_csv(file_name, iterator=True, chunksize=100000)

    df = next(df_iter)
    df = format_date(df)

    df.head(n=0).to_sql(name=table_name, con=engine, if_exists="replace")

    while True:
        try:
            t_start = time()
            df.to_sql(table_name, con=engine, if_exists="append")
            t_end = time()
            df = next(df_iter)
            df = format_date(df)
            print(
                f"Inserted another chunk %.3f seconds ({t_end - t_start})"
                % (t_end - t_start)
            )
        except StopIteration:
            print("Reached end")
            break


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Download and ingest csv data to postgres"
    )

    # user
    # password
    # host
    # port
    # db
    # table-name
    # url

    parser.add_argument("--user", help="username for postgres")
    parser.add_argument("--password", help="password for postgres")
    parser.add_argument("--host", help="host for postgres")
    parser.add_argument("--port", help="port for postgres")
    parser.add_argument("--db", help="database name for postgres")
    parser.add_argument(
        "--table_name",
        help="name of the table where we will write the results to in postgres",
    )
    parser.add_argument("--url", help="url of the csv file")

    args = parser.parse_args()

    ingest_data(args)
