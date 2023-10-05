# PySpark-ELK-FastAPI Project

This project consists of three main parts:

### ETL
The ETL Program written in PySpark reads data from a CSV file consisting of song lyrics and extracts top 5 words used by artists in their songs. the result will be loaded to the database. Spark cluster is deployed using "standalone" mode. Also, the unit test is written using Python "unittest" module. 

### NoSQL database
Elasticsearch has been used as the sink database of the ETL App.

### Backend App
The backend application is written in FastAPI. The app is responsible for authentication users with JWT, and responding to users queries to the Elasticsearch database.
