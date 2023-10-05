import unittest
import pyspark.sql.functions as f

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType

from utils.functions import lyrics_cleaner


class SparkUnitTest(unittest.TestCase):

    spark = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.spark = (SparkSession
                     .builder
                     .master("local[1]")
                     .appName("Unit-tests")
                     .getOrCreate())

    @classmethod
    def tearDownClass(cls) -> None:
        cls.spark.stop()

    def test_lyrics_cleaner_udf(self):
        data = [('Eminem', 'Hi my name is!'), ('Coldplay', 'Turn in, to something beautiful')]
        schema = StructType([
            StructField('artist', StringType(), True),
            StructField('lyrics', StringType(), True),
        ])
        test_df = self.spark.createDataFrame(data=data, schema=schema)
        test_df = test_df.withColumn('cleaned_lyrics', lyrics_cleaner(f.col('lyrics')))

        output_list = test_df.collect()
        first_result = output_list[0]['cleaned_lyrics']
        second_result = output_list[1]['cleaned_lyrics']

        self.assertEqual(first_result, "hi name")
        self.assertEqual(second_result, "turn something beautiful")
