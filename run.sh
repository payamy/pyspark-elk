# Building Spark Image
docker build -t artist-etl:0.0.1 ./etl/

# Building FastAPI App Image
docker build -t fastapi-search-backend:0.0.1 ./api/

# Running Containers
docker-compose -f docker-compose-etl.yml -f docker-compose-elk.yml -f docker-compose-backend.yml up -d &&

# Sleep 30 Seconds
sleep 30 &&

# Submitting Spark Repartitioning App
docker exec -it pyspark-elk_spark-master_1 sh -c "spark-submit --master spark://spark-master:7077 --executor-memory 1g --executor-cores 1 --packages org.elasticsearch:elasticsearch-spark-30_2.12:8.10.2 /etl/app/repartition_csv.py" &&

# Sleep 30 Seconds
sleep 30 &&

# Submitting Spark App
docker exec -it pyspark-elk_spark-master_1 sh -c "spark-submit --master spark://spark-master:7077 --executor-memory 1g --executor-cores 1 --packages org.elasticsearch:elasticsearch-spark-30_2.12:8.10.2 /etl/app/etl.py"