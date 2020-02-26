# Parallel Processing: Multiprocessing vs. Threading

The programs will perform 50,000,000 operations while performing a countdown task, recording the start and end times. Thus, it will be possible to compare the time spent to perform the same task by a program that uses a single thread, by one that uses multiple threads and by another that uses multiple processes.

The results obtained in this test were as follows:
- single thread spent 7.1907 seconds;
- multiple threads spent 7.6726 seconds;
- multiple processes spent 4.0796 seconds;

Thus evidencing a superior performance in the program that used multiple processes. This is how GIL works parallel processing in Python.

Multiprocessing outshines threading in cases where the program is CPU intensive and doesn't have to do any IO, network or user interaction. But, in case the program has to wait for an user interaction, which is the biggest bottleneck. Using multiprocessing won't make the program any faster.

"Sooner or later, every data science project faces an inevitable challenge: speed. Working with larger data sets leads to slower processing thereof, so you'll eventually have to think about optimizing your algorithm's run time." [FloydHub Blog](https://blog.floydhub.com/multiprocessing-vs-threading-in-python-what-every-data-scientist-needs-to-know/)
