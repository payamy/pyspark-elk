FROM docker.io/bitnami/spark:3.3.2

USER root
RUN adduser --disabled-password spark
RUN mkdir -p /nltk_data
RUN chown spark:spark -R /nltk_data && \
    chown spark:spark -R /opt
USER spark

RUN pip install -U pandas==2.1.1 && \
    pip install -U nltk==3.8.1 && \
    pip install -U pyarrow==13.0.0

RUN pip install -U elasticsearch==8.10.0
