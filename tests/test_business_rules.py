from pyspark.sql.functions import col, sum as spark_sum


def test_gold_customer_summary_exists(spark):
    assert spark.catalog.tableExists("pei_assignment.gold_customer_summary")


def test_gold_category_summary_exists(spark):
    assert spark.catalog.tableExists("pei_assignment.gold_category_summary")


def test_gold_state_summary_exists(spark):
    assert spark.catalog.tableExists("pei_assignment.gold_state_summary")


def test_gold_yearly_summary_exists(spark):
    assert spark.catalog.tableExists("pei_assignment.gold_yearly_summary")


def test_gold_customer_summary_not_empty(spark):
    df = spark.table("pei_assignment.gold_customer_summary")

    assert df.count() > 0


def test_gold_category_summary_not_empty(spark):
    df = spark.table("pei_assignment.gold_category_summary")

    assert df.count() > 0


def test_gold_state_summary_not_empty(spark):
    df = spark.table("pei_assignment.gold_state_summary")

    assert df.count() > 0


def test_gold_yearly_summary_not_empty(spark):
    df = spark.table("pei_assignment.gold_yearly_summary")

    assert df.count() > 0


def test_category_sales_positive(spark):
    df = spark.table("pei_assignment.gold_category_summary")

    total_sales = df.agg(
        spark_sum("total_sales")
    ).collect()[0][0]

    assert total_sales > 0


def test_category_profit_positive(spark):
    df = spark.table("pei_assignment.gold_category_summary")

    total_profit = df.agg(
        spark_sum("total_profit")
    ).collect()[0][0]

    assert total_profit > 0


def test_category_quantity_positive(spark):
    df = spark.table("pei_assignment.gold_category_summary")

    total_quantity = df.agg(
        spark_sum("total_quantity")
    ).collect()[0][0]

    assert total_quantity > 0


def test_category_has_expected_values(spark):
    df = spark.table("pei_assignment.gold_category_summary")

    categories = {
        row["category"]
        for row in df.select("category").collect()
        if row["category"] is not None
    }

    expected_categories = {
        "Technology",
        "Furniture",
        "Office Supplies"
    }

    assert expected_categories.issubset(categories)
    
def test_product_id_unique(spark):
    df = spark.table("pei_assignment.product_enriched")

    duplicates = (
        df.groupBy("product_id")
          .count()
          .filter(col("count") > 1)
    )

    assert duplicates.count() == 0