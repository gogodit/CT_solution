def solution(citations):
    citations = sorted(citations)  # 정렬하여 작은 수부터 비교
    n = len(citations)             #list 길이 구하기

    for i in range (n):
        if citations[i] >= n - i : # 접근법은 비슷했음, n은 발표한 논문 수, h는 논문이 인용된 수, 
                                   # 논문이 인용된 횟수(h번 이상) >= 인용된 논문의 개수(h개 == h번)
            return n - i           # h의 최댓값을 리턴
    return 0                       # ?
