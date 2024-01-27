import re

def solution(file_names):
    answer = []
    
    #대소문자 구분없는 문자열 정렬
    #아스키코드 65~90 영문 대문자
    #아스키코드 97~122 영문 소문자
    
    #같다면, int 숫자 정렬
    #아스키코드 48~57 숫자 0~9
    
    #같다면, 입력순 정렬
    #인덱스가 작은것부터

    filt = re.compile(r'([a-zA-Z\-\n\s.]+)([0-9]{0,5})(.*)')
    files = []
    for file_name in file_names:
        files.extend(filt.findall(file_name))
    files.sort(key=lambda x: (x[0].lower(), int(x[1])))
    answer = [''.join(i) for i in files]
    return answer
        