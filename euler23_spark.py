import numpy as np
import sympy as sy

import pyspark

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import *

sql = SparkSession.builder \
    .master("local") \
    .appName("euler 23") \
    .getOrCreate()
    
d_impl = lambda n: sum(sy.divisors(n, proper=True))
d = F.udf(d_impl, IntegerType())

a = sql.range(12, 28123)
a = a.filter(d("id") > a["id"])

a.registerTempTable("table")

query = """ 
select
    t1.id + t2.id as n
from table t1
cross join table as t2
where t1.id + t2.id < 28123
"""

s = sql.sql(query)
s = s.distinct()

b = sql.range(1, 28123)
b = b.subtract(s)

b.groupBy().sum("id").show()
