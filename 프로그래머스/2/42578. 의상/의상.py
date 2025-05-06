def solution(clothes):
    answer = [] # 옷 종류별 개수
    result = 1
    clothes_type = set()
    for i in range(len(clothes)):
        clothes_type.add(clothes[i][1])
    # print(clothes_type) #	{'headgear', 'eyewear'}
    for j in clothes_type:
        cnt = 0 # 옷 종류마다 초기화
        for i in range(len(clothes)):
            if clothes[i][1] == j:
                cnt += 1
        answer.append(cnt) # 옷 종류마다 더해줘야 하니까
    print(answer)
    for i in answer:
        result *= (i+1)
    return result - 1