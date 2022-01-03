result = SumOfPeak(arr)

def isPeak(arr,n,num,i,j):
    if(i>=0 and arr[i]>num):
        return False
    if(j<n and arr[j]>num):
        return False
    return True
def SumOfPeak(arr):
    sum=0
    for i in range(n):
        if(isPeak(arr,n,arr[i],i-1,i+1)):
            sum+=arr[i]
    return sum