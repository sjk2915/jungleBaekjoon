import sys

brackets = sys.stdin.readline().strip()

stack = []
answer = 0
for bracket in brackets:
    # 괄호 열기
    if bracket == '(':
        stack.append(['(', 0])
    elif bracket == '[':
        stack.append(['[', 0])
    # 괄호 닫기
    else:
        # 닫는데 연적이 없는 경우
        if not stack:
            answer = 0
            break
        else:
            # 괄호 검증 및 값 연산
            open_bracket, value = stack.pop()
            value = 1 if value == 0 else value
            if bracket == ')':
                if open_bracket != '(':
                    answer = 0
                    break
                value *= 2
            elif bracket == ']':
                if open_bracket != '[':
                    answer = 0
                    break
                value *= 3
            # 연산된 값 입력
            if stack:
                stack[-1][1] += value
            else:
                answer += value

print(answer)