# https://cryosleep.tistory.com/10

def pick (n , arr , k):
    if k == 0:
        print(arr)
        return
    
    lastIndex = len(arr) - k - 1

    smalleat = 0

    for i in range(smalleat , n):
        arr[lastIndex + 1] = i
        pick(n , arr , k-1)


number = 5
mx = 3
arr = [0 for i in range(mx)]
pick(number, arr , mx)

