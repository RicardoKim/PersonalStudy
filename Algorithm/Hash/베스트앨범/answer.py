from collections import defaultdict

def solution(genres, plays):
    genre_index_dict = defaultdict(list)
    genre_count_dict = defaultdict(int)
    for index, genre in enumerate(genres):
        genre_index_dict[genre].append(index)
        genre_count_dict[genre] += plays[index]
    sorted_genres = sorted(genre_count_dict.items(),reverse=True, key = lambda item: item[1])
    answer = []
    for genre in sorted_genres:
        index_list = genre_index_dict[genre[0]]
        if len(index_list) == 1 :
            answer.append(index_list[0])
        else :
            play_list = []
            for index in index_list :
                play_list.append(plays[index])
            sorted_play_list = sorted(play_list, reverse = True)
            first_large_play = sorted_play_list[0]
            second_large_play = sorted_play_list[1]
            #플레이 수가 중복일 때
            if first_large_play == second_large_play : 
                tag = 0
                # 번호가 작은 애들을 먼저 넣게 하기 위해서
                for index, play in enumerate(play_list) : 
                    if play == first_large_play :
                        answer.append(index_list[index])
                        tag += 1
                        if tag == 2 :
                            break
            # 플레이 수가 중복이 아닐 때
            else : 
                answer.append(index_list[play_list.index(first_large_play)])
                answer.append(index_list[play_list.index(second_large_play)])
    return answer