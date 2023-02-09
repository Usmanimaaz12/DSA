class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        dct, ans = defaultdict(set), 0

        for idea in ideas:                  # <-- construct the dict w/ 
            dct[idea[0]].add(idea[1:])      #     w/ initial:{suffixes} and sort
                                            #     the items to get a list of 
        d = sorted(dct.items())             #     tuples to help do the counting

        for init1, suff1 in d:              # <-- evaluate the number for each pair 
            for init2, suff2 in d:          #     of initials
                if init2 >= init1: break

                c = len(suff1&suff2)        # <-- determine the count of suffixes in 
                ans += ((len(suff1)-c)*     #     common, and subtract that count
                        (len(suff2)-c))     #     from the count of each suffix  
                                            #     count before multiplying.

        return ans * 2                      # <-- finally, return the sum times 2.