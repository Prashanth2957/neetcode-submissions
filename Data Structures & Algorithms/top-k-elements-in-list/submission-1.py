class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        D={}
        res=[]
        for num in nums:
            D[num]=D.get(num,0)+1
        res=sorted(D,key=D.get,reverse=True)
        return res[:k]       