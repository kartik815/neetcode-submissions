class Solution:
        def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
            arr2 = list(map(lambda y: y - x, arr))

            arr2_sorted = sorted(arr2,key=abs)
            return list(sorted(map(lambda y: y+x, arr2_sorted[:k])))

            # n = len(arr)
            # if k == n:
            #     return arr   

            # index = 0
            # net_val = arr[-1]-arr[0] 
            # for i in range(len(arr)-k+1):
            #     l = arr[i]
            #     r = arr[i+k-1]

            #     if(r-l) <= net_val:
            #         net_val = r-l
            #         index = i
                
            # return arr[index:index+k]




                                        