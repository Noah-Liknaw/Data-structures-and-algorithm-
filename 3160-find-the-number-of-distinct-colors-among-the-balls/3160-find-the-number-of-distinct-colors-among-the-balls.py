class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_color = {}      
        color_count = {}     
        result = []

        for x, y in queries:
            if x in ball_color:
                old_color = ball_color[x]
                color_count[old_color] -= 1
                if color_count[old_color] == 0:
                    del color_count[old_color]

            ball_color[x] = y
            color_count[y] = color_count.get(y, 0) + 1

            result.append(len(color_count))

        return result