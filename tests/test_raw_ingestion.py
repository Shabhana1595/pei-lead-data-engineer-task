from pyspark.sql.functions import col


def test_customer_raw_exists(spark):
    assert spark.catalog.tableExists("pei_assignment.customer_raw")


def test_customer_raw_not_empty(spark):
    df = spark.table("pei_assignment.customer_raw")
    assert df.count() > 0

def test_customer_raw_schema(spark):
    df = spark.table("pei_assignment.customer_raw")

    expected_columns = {
        "customer_id",
        "customer_name",
        "email",
        "phone",
        "address",
        "segment",
        "country",
        "city",
        "state",
        "postal_code",
        "region"
    }

    actual_columns = set(df.columns)

    assert expected_columns == actual_columns

df = spark.table("pei_assignment.customer_raw")

print(df.columns)
df.printSchema()
