/* https://programmers.co.kr/learn/courses/30/lessons/59042 */

SELECT OUTS.ANIMAL_ID, OUTS.NAME
FROM ANIMAL_OUTS OUTS
LEFT OUTER JOIN ANIMAL_INS INS
ON OUTS.ANIMAL_ID = INS.ANIMAL_ID
WHERE INS.ANIMAL_ID IS NULL
ORDER BY OUTS.ANIMAL_ID;

/* 
OUTER JOIN (외부 조인)
-> 조인하는 여러테이블에서 한 쪽에는 데이터가 있고, 
  한 쪽에는 데이터가 없는 경우, 
  데이터가 있는 쪽 테이블의 내용을 모두 출력하는 것
  즉, 조건에 맞지 않아도 해당하는 행을 출력하고 싶을 때 사용할 수 있다
  
  
  SELECT 검색할 컬럼

  FROM 테이블명 LEFT OUTER JOIN 테이블명2

  ON 테이블.컬럼명 = 테이블2.컬럼명;
*/
