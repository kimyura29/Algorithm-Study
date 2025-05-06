from collections import defaultdict
def solution(genres, plays):
    genre_play = defaultdict(int)
    genre_play_idx = defaultdict(list)
    
    # 1. 장르별 총 재생수와 노래 리스트 정리
    for idx, (g, p) in enumerate(zip(genres, plays)):
        genre_play[g] += p # 장르별 play수 기록
        genre_play_idx[g].append(((p, idx))) # 장르별 play수, idx
    # print(genre_play) {'classic': 1450, 'pop': 3100})
    # print(genre_play_idx) {'classic': [(500, 0), (150, 2), (800, 3)], 'pop': [(600, 1), (2500, 4)]})
    
    # 2. 장르별 총 재생수 내림차순 정렬
    sorted_g_p = sorted(genre_play.keys(), key = lambda x: genre_play[x], reverse= True) # 내림차순
    
    answer = []
    # 장르마다
    for g in sorted_g_p:
        # 각 장르의 노래를 재생 수 기준으로 내림차순 정렬(재생 수 같으면 고유번호 낮은 순 정렬)
        songs = sorted(genre_play_idx[g], key = lambda x: (-x[0], x[1]))
        answer += [idx for _, idx in songs[:2]]

    return answer