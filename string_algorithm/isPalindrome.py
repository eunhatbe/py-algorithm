import re

def isPalindrome(s: str) -> bool:
    s = s.lower()
    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]','',s)

    return s == s[::-1]

str1 = "MOOOM"
str2 = "Hello"

if isPalindrome(str1):
    print("True")
else:
    print("False")