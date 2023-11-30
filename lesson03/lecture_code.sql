CREATE TABLE raw (
  client VARCHAR(50),
  purchase_date VARCHAR(50),
  product VARCHAR(50),
  price VARCHAR(50))
;
CREATE TABLE sales (
  client VARCHAR(50),
  purchase_date DATE,
  product VARCHAR(50),
  price INT
)
;
INSERT INTO sales
SELECT
  client,
  purchase_date::DATE,
  product,
  rtrim(price, 'USD')::INT
FROM raw
;

-- Window function count usage example
SELECT
  client,
  COUNT(client) OVER (PARTITION BY client) AS sales_count
FROM sales
;

-- compare to the same operation using GROUP BY
SELECT
  client,
  COUNT(*) AS sales_count
FROM sales
GROUP BY client
;

-- LAG example
SELECT
  client,
  purchase_date,
  LAG(purchase_date) OVER (PARTITION BY client ORDER BY purchase_date) AS previous_purchase_date
FROM sales
;
