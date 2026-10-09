# Review of Contains Duplicate
Answer these three questions in your own words:

Data structure: Which data structure would you use, and why?

Algorithm: Describe the steps you'd follow to solve the problem.

Complexity: What are the expected time and auxiliary space complexities?

Don't worry about making the explanation sound polished yet. I want to check what you can recall independently before we move on.


1. seen=set(), due to it's nature of not allowing duplicates 
2. I would cycle through each value in nums and compare it to the values in seen and if there was a match I would return true if not I would add the value to seen, if all values have been cycled through then return false 
3. the expected Time complexity would depend on the num of values in nums so O(n), 
    the expected space complexity would also depend on the number of values in nums until a duplicate were reached so O(n), 
    a way to trade the time complexity would be to sort the nums array and compare each value to it's previous and that would bring the time complexity to O(n log n)

## Day 2 — Retrieval review

1. Data structure — Correct

A set is a good choice because you need to check whether a value has appeared before. Membership checks take O(1) expected time on average.

2. Algorithm — Correct

Iterate through nums, check each value against seen, return True if it's already present, and otherwise add it. If the loop finishes, return False.

One useful detail: returning True early means you may not need to inspect the rest of the array.

3. Complexity — Mostly correct

Hash set: O(n) expected time and O(n) auxiliary space in the worst case.

Sorting alternative: O(n log n) overall time, followed by a linear scan that doesn't change the overall complexity.

The key refinement: the worst-case space complexity is O(n) even if a duplicate is found early, because the algorithm could encounter almost every element before finding one. If a duplicate occurs immediately, it may use much less space.

One correction to your wording: sorting doesn't refine the time complexity here; it trades the expected O(n) time of the hash-set approach for O(n log n) time, while avoiding a separate hash set. Python's sorting implementation can still use auxiliary memory.

### Your interview-ready explanation

Here's how you could communicate the same reasoning in an interview:

“I'll iterate through the array while maintaining a hash set of values I've already seen. 
For each number, I'll check whether it's in the set. If it is, I'll immediately return True; 
otherwise, I'll add it to the set. If I finish the loop without finding a duplicate, I'll return False. 
This takes O(n) expected time and O(n) auxiliary space in the worst case. A

lternatively, I could sort the array and compare adjacent elements, 
giving O(n log n) time, but that modifies the input if I sort it in place.”

You don't need to memorize those exact words. The goal is to be able to explain the reasoning naturally.

# 