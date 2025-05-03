def solution(brown, yellow):
    result = set()
    n = brown + yellow
    for i in range(3, n+1):
        # i가 n의 약수일 때
        if n % i ==0:
            result.add((max(i, n//i), min(i, n//i))) # [wide, height]
    # print(result)
    # print(len(result))
    answer = []
    for w, h in result:
        if (w-2)*(h-2) == yellow:
            return [w,h]
            
