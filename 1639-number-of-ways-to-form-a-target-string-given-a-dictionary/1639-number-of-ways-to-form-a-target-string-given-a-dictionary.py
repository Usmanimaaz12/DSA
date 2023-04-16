class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        W = zip(*words)
        # Count the occurrences of characters in each word using Counter
        word_counts = [Counter(word) for word in W]
        
        # number of ways to form target from words starting at index i and j
        @cache
        def dp(i, j):
            # if i reaches to end of target, return 1 as valid
            # if j reaches to end of words[0], return 0 as no more characters can be made
            if i == len(target):
                return 1
            elif j == len(words[0]):
                return 0
            
            else:
                # number of ways to form the target without using current character in words[j]
                without_cur = dp(i, j + 1)
                
                # number of ways to form the target with using current character in words[j]
                with_cur = dp(i + 1, j + 1) * word_counts[j][target[i]]
                
                return (without_cur + with_cur) % int(1e9 + 7)
        
        return dp(0, 0)
