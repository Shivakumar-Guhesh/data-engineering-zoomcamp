-- Creating external table referring to gcs path
CREATE OR REPLACE EXTERNAL TABLE `dtc-de-course-411907.trips_data_all.yellow_tripdata`
OPTIONS (
  format = 'parquet',
  uris = ['gs://data_zoomcamp_bucket/yellow/yellow_tripdata_2019-*.parquet', 'gs://data_zoomcamp_bucket/yellow/yellow_tripdata_2020-*.parquet']
);

-- Creating external table referring to gcs path
CREATE OR REPLACE EXTERNAL TABLE `dtc-de-course-411907.trips_data_all.green_tripdata`
OPTIONS (
  format = 'parquet',
  uris = ['gs://data_zoomcamp_bucket/green/green_tripdata_2019-*.parquet', 'gs://data_zoomcamp_bucket/green/green_tripdata_2020-*.parquet']
);

-- Creating external table referring to gcs path
CREATE OR REPLACE EXTERNAL TABLE `dtc-de-course-411907.trips_data_all.fhv_tripdata`
OPTIONS (
  format = 'parquet',
  uris = ['gs://data_zoomcamp_bucket/fhv/fhv_tripdata_2019-*.parquet']
);