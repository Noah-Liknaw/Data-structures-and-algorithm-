class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        queue = deque((i, tickets[i]) for i in range(n))
        time = 0

        while queue:
            i, t = queue.popleft()
            t -= 1
            time += 1

            if t > 0:
                queue.append((i, t))
            if i == k and t == 0:
                break

        return time