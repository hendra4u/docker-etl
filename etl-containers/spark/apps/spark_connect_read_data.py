from pyspark.sql import SparkSession

def main():
    # Initialize Spark session
    spark = SparkSession.builder \
        .appName("Spark Connect Read Data") \
        .getOrCreate()

    # Show Spark master and worker information
    print("Spark Master URL:", spark.sparkContext.master)
    print("Spark Application Name:", spark.sparkContext.appName)
    print("Spark Version:", spark.version)
    print("Spark Executor Memory:", spark.sparkContext.getConf().get("spark.executor.memory"))
    print("Spark Executor Cores:", spark.sparkContext.getConf().get("spark.executor.cores"))
    print("Spark Worker:", spark.sparkContext.ggetExecutorStorageStatus())

    # Stop the Spark session
    spark.stop()
    print("Spark Stop Di sini")

if __name__ == "__main__":
    main()