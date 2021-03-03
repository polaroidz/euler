#!/usr/bin/env python
# coding: utf-8

import pyspark

from pyspark.sql import SparkSession
from pyspark.sql import functions as F

sql = SparkSession.builder     
  .master("local") \   
  .appName("euler 22") \    
  .getOrCreate()

df = sql.read \    
  .format("text") \
  .load("./p022_names.txt")


df = df.withColumn("value", F.split("value", ","))
df = df.withColumn("value", F.explode_outer("value"))
df = df.withColumn("value", F.regexp_extract("value", '"(.*)"', 1))

df.registerTempTable("names")

df = sql.sql("""
select
    `value` as name,
    row_number() over (order by `value` asc) as rn
from names
order by name asc
""")
df.show(10)


from pyspark.sql.types import IntegerType

def udf_name_value_impl(s):
    s = list(s)
    s = map(lambda e: ord(e) - 64, s)
    s = sum(s)
    
    return s

udf_name_value = F.udf(udf_name_value_impl, IntegerType())

df = df.withColumn("name_value", udf_name_value("name"))

df = df.withColumn("score", df["rn"] * df["name_value"])

df.groupBy().sum("score").show()
