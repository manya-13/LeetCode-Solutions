class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        answer = [0] * len(temperatures)
        stack = []
        
        for i in range(len(temperatures)):
            curr_temperature = temperatures[i]
            while stack and curr_temperature > stack[-1][0]:
                temp, idx = stack.pop()
                k = i - idx
                answer[idx] = k
            stack.append((curr_temperature, i))

        return answer