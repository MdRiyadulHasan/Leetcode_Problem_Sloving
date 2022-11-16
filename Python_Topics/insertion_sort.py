def insertion_sort(A):
    n=len(A)
    for i in range(1,n):
        temp = A[i]
        j = i-1
        while j>=0 and A[j]>temp:
            A[j+1]=A[j]
            j=j-1
        A[j+1]=temp
    return A


if __name__ =='__main__':
    A = [2,5,7,43,31,26,15,22,1,3,30,4,12,35]
    ans = insertion_sort(A)
    print('after sorting')
    print(ans)