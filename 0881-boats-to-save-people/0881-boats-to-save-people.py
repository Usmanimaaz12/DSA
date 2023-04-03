class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        low = 0
        high = len(people)-1
        boats = 0
        while low <= high:
            # given that it can carry atmost two people at a time
            if people[low] + people[high] <= limit:
                low += 1
                high -= 1
            else:
                high -= 1
            boats += 1
        return boats