def solution(sizes):
    wide = [max(s) for s in sizes] # 큰 값을 wide에
    height = [min(s) for s in sizes] # 작은 값을 height에
    final_w, final_h = max(wide), max(height)  
    return final_w * final_h