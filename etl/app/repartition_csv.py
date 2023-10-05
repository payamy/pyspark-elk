from utils.spark import session as spark, schema
import os


if __name__ == '__main__':

    target_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

    df = spark \
        .read \
        .schema(schema) \
        .option("header", "true") \
        .option("multiLine", "true") \
        .option("escape", "\"") \
        .option("delimiter", ",") \
        .csv(f'{target_path}/data/spotify_millsongdata.csv')

    df.show()
    df.count()

    df.repartition(100) \
        .write \
        .option("multiLine", "true") \
        .option("escape", "\"") \
        .option("delimiter", ",") \
        .csv(
            path=f'{target_path}/app/data/spotify_millsongdata.csv',
            mode='overwrite',
            header=True
        )
