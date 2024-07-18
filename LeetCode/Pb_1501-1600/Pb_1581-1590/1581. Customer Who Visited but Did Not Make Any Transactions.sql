SELECT
    customer_id,
    count(*) AS count_no_trans
FROM
    Visits
WHERE
    visit_id NOT IN (
        SELECT
            DISTINCT visit_id
        FROM
            Transactions
    )
GROUP BY
    customer_id
ORDER BY
    count_no_trans DESC