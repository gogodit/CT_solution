def solution(numbers):

    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)

    return str(int(' '.join(numbers)))
  
  ## x*3: sort 시 문자열 비교는 ascii값으로 되어 사전과 같이 비교.
  ## [14, 6, 12] -> 141414, 666, 121212 
