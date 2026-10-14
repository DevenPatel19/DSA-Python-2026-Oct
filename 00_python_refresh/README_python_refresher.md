# Your daily practice routine
Minutes 0–3: Active recall
Predict the behavior of a method or explain how it works before coding.


Minutes 3–10: Implement
Work through one or two TODOs without looking up a solution.


Minutes 10–15: Test and debug
Run the file in VS Code, inspect failures, and try edge cases.


Minutes 15–20: Explain
Explain why the method works, when you'd use it, and its complexity when relevant.

# Python Refresher Supplement — October 13, 2026

This package fills the 12 existing Python refresher files with gentle exercises. It is a supplement to DSA practice, not a new DSA day.

## How to use it (15–20 minutes per day)

1. Choose one file and read only its docstring/instructions.
2. Predict behavior or outline the approach before coding.
3. Implement the TODOs without viewing a solution.
4. Run the file in VS Code's terminal: `python filename.py`.
5. Use failing tests to guide debugging. Ask for Hint 1 before asking for a full solution.
6. Explain the data structure choice and complexity out loud.
7. Record: independent / needed hint / needed solution, tests passed, and one thing to revisit.

## Weakness-based starting point

Begin with `array_methods.py` because it directly checks common list-method distinctions. Then sample one exercise from dictionaries, sets, and strings. Use the results to choose the next file. Do not try to complete all 12 files in one sitting.

Suggested progression:
- Session A: `array_methods.py` (append vs extend, copying, sorting)
- Session B: `dictionary_methods.py` (frequency maps; anagram connection)
- Session C: `set_operations.py` (membership and set algebra; Contains Duplicate connection)
- Session D: `string_operations.py` (normalization and character processing)
- Session E: `stack_operations.py` and `stacks.py`
- Session F: `queue_operations.py` and `queues.py`
- Later: `arrays.py`, `dictionaries.py`, `sets.py`, `strings.py`, then revisit the hardest files.

## Test behavior

The files intentionally contain `NotImplementedError` placeholders. The tests are expected to fail until you implement the exercises. Solutions are not included in this package.

## Naming

The existing filenames are preserved exactly:
`arrays.py`, `array_methods.py`, `dictionaries.py`, `dictionary_methods.py`, `sets.py`, `set_operations.py`, `strings.py`, `string_operations.py`, `stacks.py`, `stack_operations.py`, `queues.py`, `queue_operations.py`.


## Diagnostic

### Your diagnostic summary
Topic	|Assessment	| Next step
append() vs. extend()	|	Improving, but nested-list behavior needs reinforcement	|	Practice short traces
pop() and indexes	|	Mostly solid	|	Brief review
Dictionary .get() and frequency counts	|	Good	|	Apply to interview problems
Dictionary membership	|	Needs reinforcement	|	Distinguish keys from list contents
Set membership and duplicate detection	|	Good	|	Continue into problem patterns
Set operators (&, -, \|)	|	Understood with explanation	|	Recall again later
String slicing and immutability	|	Good after a hint	|	Light review
Queue and stack operations	|	Good with guidance	|	Practice independent tracing

Recommended focus for your next 15–20-minute refresher: list mutation and return values, followed by dictionary membership. We'll use small prediction exercises first, then connect those skills to Blind 75 patterns such as Contains Duplicate and Valid Anagram. We'll keep this as a supplement to your existing DSA schedule, not a new DSA day.