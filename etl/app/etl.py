from utils.spark import session as spark, schema
from utils.functions import lyrics_cleaner

from pyspark.sql.window import Window
from elasticsearch import Elasticsearch

import pyspark.sql.functions as f
import os


es_node = 'elasticsearch'
es_port = '9200'
es_index = 'artists_words'
es = Elasticsearch(hosts=[f"http://{es_node}:{es_port}"])


if __name__ == '__main__':

    es.options(ignore_status=[400, 404]).indices.delete(index=es_index)
    es.options(ignore_status=[400]).indices.create(index=es_index)

    target_path = os.path.dirname(__file__)

    df = spark \
        .read \
        .schema(schema) \
        .option("header", "true") \
        .option("multiLine", "true") \
        .option("escape", "\"") \
        .option("delimiter", ",") \
        .csv(f'{target_path}/data/spotify_millsongdata.csv')

    window = Window.partitionBy(f.col('artist')).orderBy(f.col('count').desc())

    df.withColumn('cleaned_lyrics', lyrics_cleaner(f.col('text'))) \
        .withColumn('tokens', f.split(f.col('cleaned_lyrics'), ' ')) \
        .select(
            f.col('artist'),
            f.explode(f.col('tokens')).alias('word'),
        ) \
        .groupby(
            f.col('artist'),
            f.col('word'),
        ).count() \
        .withColumn('rank', f.rank().over(window)) \
        .filter(f.col('rank') <= 5) \
        .withColumn('word_count_pair', f.struct(f.col('word'), f.col('count'))) \
        .groupby(f.col('artist')) \
        .agg(f.array_sort(f.collect_list(f.col('word_count_pair'))).alias('top_words')) \
        .write \
        .format("es") \
        .option("es.resource", es_index) \
        .option("es.nodes", es_node) \
        .option("es.port", es_port) \
        .save()
