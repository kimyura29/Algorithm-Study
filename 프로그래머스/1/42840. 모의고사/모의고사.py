def solution(answers):
    n = len(answers)
    number_1 = [1,2,3,4,5]
    number_2 = [2,1,2,3,2,4,2,5]
    number_3 = [3,3,1,1,2,2,4,4,5,5]
    count = [0,0,0]
    number = [number_1, number_2, number_3]
    for i, ans in enumerate(answers):
        if ans == number_1[i%len(number_1)]:
            count[0] += 1
        if ans == number_2[i%len(number_2)]:
            count[1] += 1
        if ans == number_3[i%len(number_3)]:
            count[2] += 1

    max_count = max(count) # 가장 큰 값 저장
    result = [i+1 for i,v in enumerate(count) if v == max_count] # enumerate() : idx와 값
    return result