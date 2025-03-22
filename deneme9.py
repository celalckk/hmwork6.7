def titleToNumber(A):
    result = 0 
    for char in A:
        result = result * 26 + (ord(char) - ord("A")+1)
    return result

print(titleToNumber("A"))
print(titleToNumber("AB"))



def convertToTitle(A):
    result = ""
    while A -+ 1:
          result = chr(A % 26 + ord("A")) + result 
          A //=26
          return result 
print(convertToTitle(1))
print(convertToTitle(28))