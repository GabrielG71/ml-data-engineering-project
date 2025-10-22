import os
from pyspark.sql import SparkSession
from dotenv import load_dotenv

load_dotenv()

def get_spark_session(app_name="ETL_Project"):
    print("🔹 Inicializando Spark com driver JDBC...")
    
    # Para sessões anteriores
    active_session = SparkSession.getActiveSession()
    if active_session:
        active_session.stop()
        print("🔄 Sessão anterior encerrada")
    
    # Caminho do driver
    driver_path = r"C:\Users\Gabriel\Documents\ml-data-engineering-project\driver\mssql-jdbc-13.2.1.jre11.jar"
    
    if not os.path.exists(driver_path):
        raise FileNotFoundError(f"❌ Driver não encontrado: {driver_path}")
    
    print(f"🔹 Driver configurado: {driver_path}")
    
    # CONFIGURA A VARIÁVEL DE AMBIENTE ANTES DE CRIAR A SESSÃO
    os.environ['PYSPARK_SUBMIT_ARGS'] = f'--driver-class-path "{driver_path}" --jars "{driver_path}" pyspark-shell'
    
    spark = (
        SparkSession.builder
        .appName(app_name)
        .master("local[*]")
        .config("spark.driver.memory", "2g")
        .config("spark.executor.memory", "2g")
        .config("spark.sql.legacy.timeParserPolicy", "LEGACY")
        .config("spark.driver.extraClassPath", driver_path)
        .config("spark.executor.extraClassPath", driver_path)
        .getOrCreate()
    )
    
    print("✅ Spark inicializado com sucesso!")
    print(f"✅ Spark Version: {spark.version}")
    print(f"✅ Spark UI: {spark.sparkContext.uiWebUrl}")
    
    return spark

def get_jdbc_params():
    return {
        "url": os.getenv("DB_URL"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver"
    }