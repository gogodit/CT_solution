
# 다음에 다시...
def solution(phone_book):
    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]): 
        # zip함수에 길이가 같은 리스트를 넣어 병렬 비교 및 반환
        if p2.startswith(p1):  # startswith(시작하는문자, 시작지점)
            return False
    return True
