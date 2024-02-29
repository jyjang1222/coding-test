SELECT O.PRODUCT_ID, P.PRODUCT_NAME, SUM(P.PRICE*O.AMOUNT) AS TOTAL_SALES
  FROM FOOD_PRODUCT P, FOOD_ORDER O
WHERE P.PRODUCT_ID = O.PRODUCT_ID
  AND YEAR(O.PRODUCE_DATE)=2022 AND MONTH(O.PRODUCE_DATE)=5
GROUP BY PRODUCT_ID
ORDER BY SUM(P.PRICE*O.AMOUNT) DESC, PRODUCT_ID
