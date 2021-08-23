# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do 

T = int(input())

for t in range(1, T + 1):

    num = int(input())
    sum = 1
    
    for i in range(2, num+1):
        if i%2 == 0:
            sum -= i
        else:
            sum += i

    print("#{} {}".format(t,sum))
    
