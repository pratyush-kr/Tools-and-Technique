def sort(arr, comp):
    n = len(arr)
    sorted = False
    comps = n-1
    while(sorted == False):
        sorted = True
        for i in range(0, comps):
            if comp(arr[i+1], arr[i]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sorted = False
        comps -= 1
    return arr
if __name__ == '__main__':
    arr = [int(x) for x in input("Array: ").split(' ')]
    print(f'Unsorted array = {arr}')
    comp = lambda a, b: a<b
    arr = sort(arr, comp)
    print(f'Sorted array = {arr}')
