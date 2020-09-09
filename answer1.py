res = []
str  = 'aabbcc'
temp = []
def is_palindrome(s, start, end):
    if len(s) >1:
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True


def findPalindrome(s, res, temp, start):

    if start == len(s) and len(s)>1:
        res.append(temp)
    else:
        for i in range(start, len(s)):
            if(is_palindrome(s, start, i)):
                findPalindrome(s, res, temp+[s[start:i +1]], i +1)
    return res

print(findPalindrome(str, res,temp , 0))

