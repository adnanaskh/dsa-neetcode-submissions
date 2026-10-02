class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        n = len(position)

        rel = list(zip(position, speed))

        

        for pos, spd in sorted(rel)[::-1]:
            stack.append((target-pos)/spd)
            
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

        
