class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        l,r = 0,len(people)-1
        counter = 0
        while l <= r:
            s = people[l] + people[r]
            if l == r:
                counter +=1
                l+=1
            elif people[l] > limit:
                counter += 1
                l+=1
            elif people[r] > limit:
                counter +=1
                r-=1
            elif s  > limit:
                counter+=1
                r-=1
            else:
                counter+=1
                l+=1
                r-=1
        return counter