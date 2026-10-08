class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carStat = sorted(zip(position, speed), reverse=True)
        stack = []
        for car in carStat:
            currcar_time = (target - car[0]) / car[1]
            if not stack or stack[-1] < currcar_time:
                stack.append(currcar_time)
        return len(stack)