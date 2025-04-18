"""
Calculates the performance of a diet plan based on the calories consumed.

Given a list of calories burned each day and a set of performance criteria, the task is to calculate the 
total performance of a diet plan. The performance is calculated by summing the calories burned for days 
that meet certain conditions, such as being over a specific target or achieving a streak.

Args:
    calories (List[int]): A list representing the number of calories burned each day.
    k (int): A specific target number of calories for evaluating performance.
    lower (int): The lower bound for the calories to be considered for performance.
    upper (int): The upper bound for the calories to be considered for performance.

Returns:
    int: The total performance value of the diet plan.

More Detail:
You need to compute a score over the entire period using a sliding window of size k:
For each window of k days:
If the total calories in the window is less than lower, subtract 1 from your score.
If the total calories is greater than upper, add 1 to your score.
If the total is between lower and upper (inclusive), the score remains the same.
"""

import pytest

def diet_plan_performance(calories: list[int], k: int, lower: int, upper: int):
    score = 0
    for i in range(len(calories) - k + 1):
        left = i
        right = i + k
        current_days = calories[left: right]
        current_value = sum(current_days)
        # print(f"left {left}, right {right}, current_days {current_days}, current_value {current_value}, lower {lower}, upper {upper}")
        if current_value < lower:
            score -= 1
            # print(f"reducing score: {score}")
        elif current_value > upper:
            score += 1
            # print(f"increasing score: {score}")
    return score

@pytest.mark.parametrize("calories, k, lower, upper, expected", [
    ([1, 2, 3, 4, 5], 1, 3, 3, 0), 
    ([3, 2], 2, 0, 1, 1),                   # Window sum is 5 > upper → +1
    ([6, 5, 0, 0], 2, 1, 5, 0),              # Windows: [6,5]=11(+1), [5,0]=5(0), [0,0]=0(-1) → total = 0
    ([1, 2, 3, 4, 5, 6], 3, 6, 10, 2),       # Windows: [1,2,3]=6(0), [2,3,4]=9(0), [3,4,5]=12(+1), [4,5,6]=15(+1) → score=2
    ([10, 20, 30], 3, 15, 25, 1),            # One window: sum=60 → > upper → +1
    ([1,1,1,1,1], 2, 3, 4, -4),              # All windows < lower → -1 * 4 = -4
])
def test_diet_plan_performance(calories, k, lower, upper, expected):
    assert diet_plan_performance(calories, k, lower, upper) == expected

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, '-s']))
