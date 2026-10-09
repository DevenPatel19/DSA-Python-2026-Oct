# Contains Duplicate
Completed Problems
2026-10-08 — Contains Duplicate
Primary Approach

Hash Set.

Iterate through nums
        ↓
Is num already in seen?
    ↓           ↓
   Yes          No
    ↓            ↓
 return True   add to set
                   ↓
              continue
Complexity

Time: O(n) expected

Space: O(n)

Alternative Approach

Sort the array and compare adjacent values.

Time: O(n log n)

Space: Depends on sorting implementation.

Key Lessons
Use a set when the problem asks whether something has been seen.
Set membership is O(1) on average.
Sorting can expose relationships between neighboring elements.
= is assignment; == is comparison.
list.sort() modifies the list in place.
sorted() returns a sorted result.
range(1, len(nums)) allows comparison with nums[i - 1].
return exits the function immediately.

## Interview Explanation

"I'll iterate through the array while maintaining a hash set of values I've already seen. For each value, I'll check whether it's already in the set. If it is, I know there's a duplicate and can immediately return True; otherwise, I'll add it to the set. If I finish the iteration without finding a duplicate, I'll return False."

## Review Schedule
Problem	Initial	| 1 Day	| 1 Week	| 1 Month
Contains Duplicate	| ✅ 10/08	| ⬜ 10/09	| ⬜ 10/15	| ⬜ 11/08

### Current Weaknesses / Things to Remember
 - Distinguish when a set is sufficient vs when a frequency dict is needed.
 - Be precise when explaining complexity.
 - Avoid relying on memorized solutions.
 - Practice explaining solutions aloud.
 - Watch Python syntax/control-flow while rebuilding coding fluency.

 ### Next Session
Before New Material

Redo Contains Duplicate from memory without looking at the previous solution.

Then answer:

1.  Why does a set work here?
2.  Why is membership lookup efficient?
3. Why is the space O(n)?
4. What is the sorting alternative?
5. Why is the sorting solution O(n log n)?