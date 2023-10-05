from pyspark.sql.functions import pandas_udf
from pyspark.sql.types import StringType

import pandas as pd
import re


@pandas_udf(StringType())
def lyrics_cleaner(lyrics: pd.Series) -> pd.Series:

    from nltk.corpus import stopwords
    import nltk

    try:
        nltk.download('stopwords')
    except FileExistsError:
        pass

    try:
        nltk.download('punkt')
    except FileExistsError:
        pass

    try:
        nltk.download('wordnet')
    except FileExistsError:
        pass

    lyrics = lyrics.apply(lambda x: re.sub("[^A-Za-z]+", " ", str(x)))
    lyrics = lyrics.apply(lambda x: str(x).lower())
    lyrics = lyrics.apply(lambda x: " ".join([w for w in nltk.word_tokenize(x)
                                              if not w.lower() in stopwords.words("english")]))
    return lyrics

