/* https://programmers.co.kr/learn/courses/30/lessons/59412 */

SELECT HOUR(DATETIME) HOUR, COUNT(DATETIME) COUNT
FROM ANIMAL_OUTS
GROUP BY HOUR(DATETIME)
HAVING HOUR >= 9 AND HOUR <= 19
ORDER BY HOUR


/* HOUR(DATETIME) : 시간만 추출하는 함수
   HAVING : 조건에 맞는 그룹 추출
   ORDER BY : 그룹 정렬
*/
