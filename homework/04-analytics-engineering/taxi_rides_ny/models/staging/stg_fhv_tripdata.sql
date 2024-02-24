with source as (select * from {{ source("staging", "fhv_tripdata") }})

select
    {{ dbt_utils.generate_surrogate_key(["dispatching_base_num", "pickup_datetime"]) }}
    as tripid,
    dispatching_base_num,
    cast(pickup_datetime as timestamp) as pickup_datetime,
    cast(dropoff_datetime as timestamp) as dropoff_datetime,
    -- pickup_datetime,
    -- dropoff_datetime,
    {{ dbt.safe_cast("pulocationid", api.Column.translate_type("integer")) }}
    as pickup_locationid,
    {{ dbt.safe_cast("dolocationid", api.Column.translate_type("integer")) }}
    as dropoff_locationid,
    {{ dbt.safe_cast("SR_Flag", api.Column.translate_type("integer")) }} as sr_flag,
    -- pulocationid,
    -- dolocationid,
    -- sr_flag,
    affiliated_base_number
from source
where
    EXTRACT(YEAR FROM cast(pickup_datetime as timestamp) ) = 2019
    

-- dbt build --select <model_name> --vars '{'is_test_run': 'false'}'
{% if var("is_test_run", default=true) %} limit 100 {% endif %}
