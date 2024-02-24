SELECT service_type,COUNT(*)  FROM `dtc-de-course-411907.prod.fact_trips` WHERE cast(pickup_datetime as datetime)> cast('2019-07-01 00:00:00' as datetime) AND cast(pickup_datetime as datetime)> cast('2019-07-31 00:00:00' as datetime) group by service_type;

SELECT COUNT(*)  FROM `dtc-de-course-411907.prod.fact_fhv_trips` WHERE cast(pickup_datetime as datetime)> cast('2019-07-01 00:00:00' as datetime) AND cast(pickup_datetime as datetime)> cast('2019-07-31 00:00:00' as datetime);

-- Yellow  31312941
-- Green    2911735
-- FHV      1694782
