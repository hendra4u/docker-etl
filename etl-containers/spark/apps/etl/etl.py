from pyspark.sql import SparkSession

# 1. Connect
spark = SparkSession.builder.appName("SimpleETL").getOrCreate()
print("Spark Master URL:", spark.sparkContext.master)
print("Spark Application Name:", spark.sparkContext.appName)
print("Spark Version:", spark.version)

# 2. Extract
df = spark.read.json("examples/src/main/resources/people.json")
print(f"Data Extract !!")
df.show()

# 3. Transform# Select people older than 21
print(f"Transform# Select people older than 21!!")
df.filter(df['age'] > 21).show()
df_transformed = df.filter(df["age"] > 21).select("name", "age")

# 4. Load 
# Write data on filesystem
#df_transformed.write.format("CSV").mode("overwrite").options(header=True).save("/opt/spark-data/output/")
#print(f"Data succesfully loaded to filesystem !!")

def load(type: str, target: str):
    
    # Write data on mysql database with table name
    if type=="JDBC":
         df_transformed.write.format("JDBC").mode("overwrite").options(url='jdbc:mysql://localhost/world',\
             dbtable=target,driver='com.mysql.cj.jdbc.Driver',user='root',password='root').save()
         print(f"Data succesfully loaded to MySQL Database !!")
    
    if type=="CSV":
        # Write data on filesystem
        df_transformed.write.format("CSV").mode("overwrite").options(header=True).save(target)
        print(f"Data succesfully loaded to filesystem !!")
        
load("CSV","/opt/spark-data/output/")

spark.stop()