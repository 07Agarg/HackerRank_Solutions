SELECT CASE WHEN P IS NULL THEN concat(N,' Root')
            WHEN N IN (SELECT DISTINCT B.P FROM BST AS B) THEN concat(N, ' Inner')
            ELSE concat(N, ' Leaf')
        END 
FROM BST
ORDER BY N;     