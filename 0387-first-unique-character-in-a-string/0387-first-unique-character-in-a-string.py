class Solution:
    def firstUniqChar(self, s: str) -> int:
         count = defaultdict(int)
         q = deque()

         for i, c in enumerate(s):
             count[c] += 1
             q.append((c, i))

         while q:
             char, idx = q.popleft()
             if count[char] == 1:
                 return idx

         return -1