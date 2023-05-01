class Solution:
    def average(self, salary: List[int]) -> float:
        max_sal=100
        min_sal=10000000
        total_sum=0
        for sal in salary:
            total_sum+=sal
            if sal>max_sal:
                max_sal=sal
            if sal<min_sal:
                min_sal=sal
        total_sum-=(max_sal+min_sal)
        average=total_sum/(len(salary)-2)
        return average