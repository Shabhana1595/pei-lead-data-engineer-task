from pyspark.sql.functions import sum as spark_sum


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

def test_total_profit_matches(spark):
    order_df = spark.table("pei_assignment.order_enriched")
    gold_df = spark.table("pei_assignment.gold_customer_summary")

    order_profit = (
        order_df
        .agg(spark_sum("profit"))
        .collect()[0][0]
    )

    gold_profit = (
        gold_df
        .agg(spark_sum("total_profit"))
        .collect()[0][0]
    )

    assert round(order_profit, 2) == round(gold_profit, 2)
def test_year_exists(spark):
    df = spark.table("pei_assignment.gold_yearly_summary")

    assert df.count() > 0