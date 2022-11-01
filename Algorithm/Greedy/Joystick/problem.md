# 문제
문자열이 주어지면 해당 문자를 만들기 위해서 조작해야하는 조이스틱의 수

조이스틱 이동에 따라 발생할 수 있는 경우의 수

▲ - 다음 알파벳<br>
▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)<br>
◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)<br>
▶ - 커서를 오른쪽으로 이동 (마지막 위치에서 오른쪽으로 이동하면 첫 번째 문자에 커서)

'A*목표 문자열' 이 주어졌을 때 목표 문자열을 만들기 위한 최소 조이스틱 조작 횟수는?

# 해결방안

탐욕 알고리즘으로 접근!!
1. 선택 절차 : 현재 상태에서의 최적의 해답을 선택한다.
> 현재 위치에서 가장 근처에 A가 아닌 지점을 찾는다.
2. 적절성 검사 : 선택된 해가 문제의 조건을 만족하는지 검사한다.
> A가 아닌 문자열을 찾아 이를 원하는 문자로 만들어야하기 때문에 <br>
> 이때 조이스틱 조작은 A로 부터 내려가는것이 빠른지 올라가는게 빠른지 검사한다.
3. 해답 검사 : 원래의 문제가 해결되었는지 검사하고, 해결되지 않는다면 선택 절차로 돌아가 위의 과정을 반복한다.
> 검사되어서 조작 또는 유지한 글자들의 수가 목표 문자열과 같다면 종료 시킨다.

# Pseudo code
```python
def solution(name):
    name_len = len(name)
    name_list = list(name)
    tag = name_list.count('A')
    index = 0
    answer = 0
    while tag < name_len :
        if name_list[index] != "A":
            
            target_ascii = ord(name_list[index])
            origin_ascii = ord("A")
            neg_move = abs(origin_ascii - target_ascii)
            pos_move = abs(target_ascii - origin_ascii)
            tag += 1
            answer += min(neg_move, pos_move)
            
            right_move = 0
            right_index = 0
            left_move = 0
            left_index = 0
            for i in range(index + 1, name_len) :
                if name_list[i] != 'A' :
                    right_index = i
                    break
                else :
                    right_move += 1
            
            for i in range(index, index - name_len, -1):
                if name_list[i] != 'A' :
                    left_index = i
                    break
                else :
                    left_move += 1
            if right_move < left_move : 
                index = right_index
                answer += right_move
            else :
                index = left_index
                answer += left_move
    return answer
```
