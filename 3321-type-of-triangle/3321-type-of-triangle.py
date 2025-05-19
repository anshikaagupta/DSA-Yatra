class Solution:
    def triangleType(self, a: List[int]) -> str:
        return ('none','equilateral','isosceles','scalene')[(max(a)<min(a)+median(a))*len({*a})]      