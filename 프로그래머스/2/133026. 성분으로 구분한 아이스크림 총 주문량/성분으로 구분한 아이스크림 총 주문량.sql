# SELECT F.FLAVOR, I.INGREDIENT_TYPE, F.TOTAL_ORDER FROM FIRST_HALF F, ICECREAM_INFO I
# WHERE F.FLAVOR = I.FLAVOR

SELECT I.INGREDIENT_TYPE, SUM(F.TOTAL_ORDER) AS TOTAL_ORDER FROM FIRST_HALF F, ICECREAM_INFO I
WHERE F.FLAVOR = I.FLAVOR
GROUP BY INGREDIENT_TYPE
ORDER BY SUM(F.TOTAL_ORDER)
