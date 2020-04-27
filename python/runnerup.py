#Outputs runner-up score from input.

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sorted_arr = sorted(arr)
    
    for i in range((len(sorted_arr)-1), 0, -1):
        if sorted_arr[i]==sorted_arr[i-1]:
            pass
        else:
            print (sorted_arr[i-1])
            break
