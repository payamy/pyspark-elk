from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType

session = SparkSession \
        .builder \
        .appName("ETL") \
        .getOrCreate()

schema = StructType([
    StructField('artist', StringType(), True),
    StructField('song', StringType(), True),
    StructField('link', StringType(), True),
    StructField('text', StringType(), True),
])
