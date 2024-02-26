SELECT ITEM_ID, ITEM_NAME FROM ITEM_INFO
WHERE ITEM_ID = ANY(SELECT DISTINCT ITEM_ID FROM ITEM_TREE WHERE PARENT_ITEM_ID IS NULL)
ORDER BY ITEM_ID ASC