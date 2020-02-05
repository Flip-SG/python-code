# Memory Usage Test: Function x Generator

This test will compare memory usage when run or the same program with Functions that use Lists
with 100,000 values and Generators with 100,000 values.

To perform the test we will use the Fibonacci sequence.
The Fibonacci Sequence consists of a succession of numbers, such that, defining the first two numbers of the sequence
  as 0 and 1, the following numbers will be obtained by adding their two predecessors.
Therefore, the numbers are: 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181 ...

While the Function uses 1,120 MB of memory, the Generator uses only 690 MB of memory, showing that Generators have a better performance when compared to the Functions.

Generators have several advantages over functions
conventional:
- Lazy Evaluation: generators are only processed when it is really
necessary, thus saving processing resources.
- Reduce the need to create lists.
- They allow you to work with unlimited sequences of elements.
