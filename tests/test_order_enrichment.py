from pyspark.sql.functions import col


def test_order_enriched_exists(spark):
    assert spark.catalog.tableExists("pei_assignment.order_enriched")


def test_row_count_preserved(spark):
    raw_df = spark.table("pei_assignment.orders_raw")
    enriched_df = spark.table("pei_assignment.order_enriched")

    assert raw_df.count() == enriched_df.count()


def test_profit_not_null(spark):
    df = spark.table("pei_assignment.order_enriched")

    assert df.filter(col("profit").isNull()).count() == 0


def test_customer_name_not_null(spark):
    df = spark.table("pei_assignment.order_enriched")

    assert df.filter(col("customer_name").isNull()).count() == 0


def test_category_not_null(spark):
    df = spark.table("pei_assignment.order_enriched")

    assert df.filter(col("category").isNull()).count() == 0


def test_sub_category_not_null(spark):
    df = spark.table("pei_assignment.order_enriched")

    assert df.filter(col("sub_category").isNull()).count() == 0

def test_profit_not_null(spark):
    df = spark.table("workspace.pei_assignment.order_enriched")

    assert df.filter("profit IS NULL").count() == 0

def test_customer_name_has_no_special_characters(spark):
    df = spark.table("workspace.pei_assignment.order_enriched")

    invalid = df.filter(
        col("customer_name").rlike("[^A-Za-z ]")
    )

    assert invalid.count() == 0