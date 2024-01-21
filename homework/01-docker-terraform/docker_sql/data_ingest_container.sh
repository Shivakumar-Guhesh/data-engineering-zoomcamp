# URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz"

URL="https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv"

docker run -it \
  --network=pg-network \
  data_ingest:v001 \
    --user=root \
    --password=root \
    --host=pg-db \
    --port=5432 \
    --db=ny_taxi \
    --table_name=green_trip \
    --url=${URL} 
  