import os
from pyspark.sql import SparkSession
from dotenv import load_dotenv

load_dotenv()

def get_spark_session(app_name="ETL_Project"):
    spark = (
        SparkSession.builder
        .appName(app_name)
        .config("spark.jars", "../drivers/mssql-jdbc-12.4.2.jre11.jar")
        .getOrCreate()
    )
    return spark

def get_jdbc_params():
    return {
        "url": os.getenv("DB_URL"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "driver": os.getenv("DB_DRIVER")
    }
