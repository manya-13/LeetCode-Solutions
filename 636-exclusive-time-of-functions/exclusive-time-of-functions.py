class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
       
        result = [0] * n

        call_stack = []
        prev_ts = 0

        for log in logs:
            log_id, call_type, timestamp = log.split(':')
            log_id = int(log_id)
            timestamp = int(timestamp)
            if call_type == "start":
                if call_stack:
                    result[call_stack[-1]] += timestamp - prev_ts
                call_stack.append(log_id)
                prev_ts = timestamp 
            else:
                result[call_stack.pop()] += timestamp - prev_ts + 1
                prev_ts = timestamp + 1
        return result
                
                



