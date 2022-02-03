from math import log10
def isPalindrome(num:int):
    digits = int(log10(num))
    tmp = num
    newnum = 0
    while (tmp != 0):
        newnum += (tmp%10)*(10**(digits))
        digits-=1
        tmp = tmp//10
    if num == newnum:
        return True
    return False
if __name__ == '__main__':
    num = int(input("num: "))
    print(isPalindrome(num))