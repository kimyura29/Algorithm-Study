# arr= [1,1,3,3,0,1,1]

def solution(arr):
    stack = []
    for i in range(len(arr)):
        if [arr[i]] != arr[i+1:i+2]:
            stack.append(arr[i])
    return stack