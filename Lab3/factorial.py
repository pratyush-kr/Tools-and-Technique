def fact(num:int):
    if num == 1:
        return 1
    return num*fact(num-1)

if __name__ == '__main__':
    nums = [1, 6, 7, 5, 8, 12, 10]
    for num in nums:
        print(f'{num}! = {fact(num)}')