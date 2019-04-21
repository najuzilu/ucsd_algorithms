## Greedy Algorithms Quiz ##

1. You work as a freelancer and have a pool of 10 projects to work on. For each project you know how much money you will get for completing the project. You can complete any 3 projects this month. You want to select such projects that you will get the most money by completing them. What are the safe moves in this problem? (Mark all that apply.)  
**Answer**:
* Take the project with the highest payment for completion, complete it and remove it from the pool of projects.
* If there are more than 3 projects in the pool, remove the project with the lowest payment for completion, don't work on this project. In the other case, remove the first project from the pool and work on this project.

2. In the previous problem, what is the subproblem you need to solve after you've made a safe move?  
**Answer**: Choose projects with highest payment to work on from the pool of projects which now contains only 9 projects.

3. You need to find an integer 23 <= x <= 73 with the largest product of digits. You use a greedy strategy: first, determine the largest possible first digit (tens) of x, then determine the largest possible second digit (ones) of x (among all the numbers in the range from 23 to 73 whose first digit is equal to the digit selected at the first step). Will this greedy strategy work correctly?  
**Answer**: No

## Fractional Knapsack Quiz ##

1. You have a knapsack of capacity 10kg and three items. First item has weight 20kg and value 20, second item has weight 5kg and value 10. Third item has weight 4 kg and value 20. You want to maximize the total value of the fractions of items that fit into your knapsack. What is the safe move?  
**Answer**: Take the whole third item.

2. What is the next safe move in the previous problem?  
**Answer**: Take the whole second item.

3. What is the last move?  
**Answer**: Take 1 kg of the first item.