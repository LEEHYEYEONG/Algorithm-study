'''
Head는 숫자가 아닌 문자, 최소한 한 글자 이상
NUMBER는 한 글자에서 최대 다섯 글자 사이의 연속된 숫자, 앞 쪽에 0이 올 수 있음, 0 이상 99999 사이의 숫자, 00000이나 0101 등 가능
Tail은 나머지 숫자가 다시 나타날수도 있고 아무것도 없을 수도 있음
1. Head 부분을 기준 사전 순으로 정렬 -> 대소문자 구분 X
2. Number의 숫자 순으로 정렬 9 < 10 < 0011 < 012 < 014 순으로 정렬된다. 011 = 11
3. 두 파일의 Head 부분과 Number의 숫자도 같을 경우, 입력에 주어진 순서를 유지
'''
import re

def solution(files):
    answer = []
    num = []
    temp = []
    
    for file in files:
        head, number, tail = re.match(r'(\D+)(\d{1,5})([a-z-. ]*)', file.lower()).groups()
        temp.append((head, number, tail, file))
        
    temp = sorted(temp,key = lambda x : int(x[1]))
    temp = sorted(temp,key = lambda x : x[0])
    
    for i in range(len(temp)):
        num.append(temp[i][3])
        
    return num