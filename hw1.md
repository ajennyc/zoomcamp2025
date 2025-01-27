# 1. 

      docker build -t testing .

      docker run -it --rm --name running-testing testing bash

      pip --version


**Answer:** pip 24.3.1

# 2. 

Since we wish to configure pgAdmin to connect to Postgres inside the docker network we need to use internal service name (db) and internal port 5432. 


**Answer:** db:5432

# 3.

During the period of October 1st 2019 (inclusive) and November 1st 2019 (exclusive), how many trips, respectively, happened:

- Up to 1 mile
- In between 1 (exclusive) and 3 miles (inclusive),
- In between 3 (exclusive) and 7 miles (inclusive),
- In between 7 (exclusive) and 10 miles (inclusive),
- Over 10 miles

```sql
SELECT
    COUNT(*) AS trip_count
FROM
    green_taxi_data
WHERE
    lpep_dropoff_datetime >= '2019-10-01' AND
    lpep_dropoff_datetime < '2019-11-01'
    AND trip_distance <= 1
    -- AND trip_distance > 1 AND trip_distance <= 3
    -- AND trip_distance > 3 AND trip_distance <= 7
    -- AND trip_distance > 7 AND trip_distance <= 10
    -- AND trip_distance > 10
```

**Answer:** 104,802; 198,924; 109,603; 27,678; 35,189

# 4. 

```sql
SELECT
	trip_distance,
	lpep_pickup_datetime
FROM
    green_taxi_data
WHERE 
	lpep_pickup_datetime = '2019-10-11' OR
	lpep_pickup_datetime = '2019-10-24' OR
	lpep_pickup_datetime = '2019-10-26' OR
	lpep_pickup_datetime = '2019-10-31'
```

**Answer:** 2019-10-11

# 5.

```sql
SELECT 
    "PULocationID", 
    SUM(total_amount) AS total_amount_sum
FROM 
    green_taxi_data
WHERE 
    lpep_pickup_datetime::date = '2019-10-18'
GROUP BY 
    "PULocationID"
HAVING 
    SUM(total_amount) > 13000
ORDER BY 
    total_amount_sum DESC
LIMIT 3;
```

**Answer:** East Harlem North, East Harlem South, Morningside Heights

# 6.

```sql
SELECT 
    "DOLocationID",
	MAX(tip_amount)
FROM 
    green_taxi_data
WHERE 
    lpep_pickup_datetime::date BETWEEN '2019-10-01' AND '2019-11-01'
	AND
	"PULocationID" = 74
GROUP BY("DOLocationID")
ORDER BY (MAX(tip_amount)) DESC
```

**Answer:** 132 which corresponds to "JFK Airport"

# 7.

**Answer:** terraform init, terraform apply -auto-approve, terraform destroy

terraform init, terraform run -auto-approve, terraform destroy




