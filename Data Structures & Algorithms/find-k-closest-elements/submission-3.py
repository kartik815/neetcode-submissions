class Solution:
        def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
            arr2 = list(map(lambda y: y - x, arr))

            arr2_sorted = sorted(arr2,key=abs)
            return list(sorted(map(lambda y: y+x, arr2_sorted[:k])))
                               
                                        