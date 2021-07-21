/* https://programmers.co.kr/learn/courses/30/lessons/12981 */

def solution(n, words):
    answer = [0,0]
    a = 1

    # 순서에 맞춰 돌아가는 반복문
    for i in range(1, len(words)):
        w = words[i] # 현재 단어
        a %= n

        # 마지막 문자 추출  words[i-1][:-1]
        # 첫 문자 추출     w[0]

        # 이전 문자와 현재 문자의 연결이 안됨, 이미 나온 단어
        if (words[i-1][-1] != w[0]) or (w in words[0:i]):
            answer = [a+1, 1+i//n]

            return answer
        a += 1

    return answer
