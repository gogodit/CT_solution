def solution(n):
    cty = [1,2,4]
    answer = "" # 문자열로 숫자를 붙여나갈것임

    while n > 0:
        n -= 1 # 배열은 0부터 시작이기에 1을 빼준다.
        answer = n[n%3] + answer
        # 3진수로 바꾸기 위해 나머지 구함
        n //= 3 # 남은 수들은 몫으로 다시 구함

    return answer
