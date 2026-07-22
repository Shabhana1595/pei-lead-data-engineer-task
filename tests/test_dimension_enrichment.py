from pyspark.sql.functions import col


def test_customer_enriched_exists(spark):
    assert spark.catalog.tableExists("pei_assignment.customer_enriched")


def test_product_enriched_exists(spark):
    assert spark.catalog.tableExists("pei_assignment.product_enriched")


def test_customer_enriched_not_empty(spark):
    df = spark.table("pei_assignment.customer_enriched")

    assert df.count() > 0


def test_product_enriched_not_empty(spark):
    df = spark.table("pei_assignment.product_enriched")

    assert df.count() > 0


def test_customer_id_not_null(spark):
    df = spark.table("pei_assignment.customer_enriched")

    assert df.filter(col("customer_id").isNull()).count() == 0


def test_customer_name_not_null(spark):
    df = spark.table("pei_assignment.customer_enriched")

    assert df.filter(col("customer_name").isNull()).count() == 0


def test_product_id_not_null(spark):
    df = spark.table("pei_assignment.product_enriched")

    assert df.filter(col("product_id").isNull()).count() == 0


def test_category_not_null(spark):
    df = spark.table("pei_assignment.product_enriched")

    assert df.filter(col("category").isNull()).count() == 0


def test_sub_category_not_null(spark):
    df = spark.table("pei_assignment.product_enriched")

    assert df.filter(col("sub_category").isNull()).count() == 0

def test_customer_id_unique(spark):
    df = spark.table("pei_assignment.customer_enriched")

    duplicates = (
        df.groupBy("customer_id")
          .count()
          .filter(col("count") > 1)
    )

    assert duplicates.count() == 0

def test_product_id_unique(spark):
    df = spark.table("pei_assignment.product_enriched")

    duplicates = (
        df.groupBy("product_id")
          .count()
          .filter(col("count") > 1)
    )

    assert duplicates.count() == 0