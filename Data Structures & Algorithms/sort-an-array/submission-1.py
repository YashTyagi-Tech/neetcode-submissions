class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        b=[-1]*len(nums)
        def mergeSort(arr,l,r):
            if l<r:
                mid=(l+r)//2
                mergeSort(arr,l,mid)
                mergeSort(arr,mid+1,r)
                merge(arr,l,mid,r)
        def merge(arr,l,mid,r):
            i=l
            j=mid+1
            k=l
            while(i<=mid and j<=r):
                if arr[i]<arr[j]:
                    b[k]=arr[i]
                    i+=1
                else:
                    b[k]=arr[j]
                    j+=1
                k+=1
            if(i>mid):
                while(j<=r):
                    b[k]=arr[j]
                    j+=1
                    k+=1
            if(j>r):
                while(i<=mid):
                    b[k]=arr[i]
                    i+=1
                    k+=1
            for k in range(l,r+1):
                arr[k]=b[k]
        mergeSort(nums,0,len(nums)-1)
        return nums





         
        