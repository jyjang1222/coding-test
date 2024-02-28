# SELECT PRODUCT_ID FROM PRODUCT

SELECT P.PRODUCT_CODE, (SUM(S.SALES_AMOUNT) * P.PRICE) AS SALES
FROM PRODUCT P, OFFLINE_SALE S
WHERE P.PRODUCT_ID = S.PRODUCT_ID
GROUP BY P.PRODUCT_ID
ORDER BY (SUM(S.SALES_AMOUNT) * P.PRICE) DESC, PRODUCT_CODE

# SELECT PRODUCT_ID, SUM(SALES_AMOUNT) FROM OFFLINE_SALE
# GROUP BY PRODUCT_ID