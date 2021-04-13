def solution(clothes):
    
    answer = 1 # 0은 곱할 수 없지...
    
    c = {}
    for x,y in clothes:
        if y in c.keys():
            c[y].append(x)
        else:
            c[y] = [x]

    for x in c.values(): 
        answer *= (len(x)+1) # 입지 않은 경우 추가 1, 경우의 수... 곱의 법칙...
    
    return answer-1
  
  
  # dictionary 변수 선언 >>> d = {}
  # key, value 삽입     >>> d[k] = 'v' 
  # 특정 키값이 dictionary에 존재하는지 찾기 >>> k in d
  # dictionary의 key값들 출력   >>> d.keys()
  # dictionary의 value값들 출력 >>> d.values()
  # 출력시 list로 리턴됨
  # 리스트에 요소 추가      >>> d.append()
  # 경우의 수 - 곱의 법칙(두 사건이 모두 일어나야 할 때 사용)
  # 사건 A가 일어나는 경우의 수가 a가지
  # 사건 B가 일어나는 경우의 수가 b가지
  # 사건 A와 사건 B가 동시에 일어날 경우의 수 axb가지
