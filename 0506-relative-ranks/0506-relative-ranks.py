class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        orderedScore = sorted(score, reverse=True) 

        for i in range(len(score)):
            score[i] = str(orderedScore.index(score[i])+1)

            if score[i] == '1':
                score[i]="Gold Medal"
            if score[i] == '2':
                score[i]="Silver Medal"
            if score[i] == '3':
                score[i]="Bronze Medal"
        
        return score
        
