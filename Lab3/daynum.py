def dayname(n:int):
    if(n == 1):
        return "Monday"
    if(n == 2):
        return "Tuesday"
    if(n == 3):
        return "Wednesday"
    if(n == 4):
        return "Thursday"
        return "Thursday"
    if(n == 5):
        return "Friday"
    if(n == 6):
        return "Saturday"
    if(n == 7):
        return "Sunday"

if __name__ == '__main__':
    n = int(input("day num: "))
    print(dayname(n))