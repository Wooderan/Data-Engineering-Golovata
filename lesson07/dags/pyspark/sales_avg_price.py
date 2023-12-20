import argparse
from pyspark.sql import SparkSession, functions as f, types as t


def _parse_args():
    """
    Parses command-line arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--sales-csv',
        required=True,
    )
    parser.add_argument(
        '--res-dir',
        required=True,
    )

    parser.add_argument(
        '--month',
        required=True,
        type=int
    )

    args = parser.parse_args()

    print("CLI args:", args)

    sales_csv = args.sales_csv
    res_dir = args.res_dir
    month = args.month

    return sales_csv, res_dir, month


def main(sales_csv: str, res_dir: str, month: int):
    """
    Create and run Pyspark job
    """
    spark = SparkSession.builder.getOrCreate()

    sales_df = spark.read.schema(
        "client STRING, purchase_date DATE, product STRING, price INTEGER"
    ).csv(sales_csv, header=True, inferSchema=False)

    avg_sales_price_df = sales_df.filter(
        f.month('purchase_date') == month
    ).groupBy(
        'product'
    ).agg(
        f.round(
            f.avg('price').alias('avg_price')
        )
    ).orderBy('product')

    # uncomment for debug:
    # avg_sales_price_df.show()

    # NB: use overwrite mode for idempotency:
    avg_sales_price_df.write.json(res_dir, mode='overwrite')

    spark.stop()


if __name__ == '__main__':
    sales_csv, res_dir, month = _parse_args()
    main(
        sales_csv=sales_csv,
        res_dir=res_dir,
        month=month,
    )
