
### Multiprocessing and Threading
Fundamentally, multiprocessing and threading are two ways to achieve parallel computing, using processes and threads, respectively, as the processing agents.

#### Process
A process is an instance of a computer program being executed. Each process has its own memory space it uses to store the instructions being run, as well as any data it needs to store and access to execute.

#### Threads
Threads are components of a process, which can run parallely. There can be multiple threads in a process, and they share the same memory space, i.e. the memory space of the parent process. This would mean the code to be executed as well as all the variables declared in the program would be shared by all threads.

#### Technical details
- All the threads of a process live in the same memory space, whereas processes have their separate memory space.
- Threads are more lightweight and have lower overhead compared to processes. Spawning processes is a bit slower than spawning threads.
- Sharing objects between threads is easier, as they share the same memory space. To achieve the same between process, we have to use some kind of IPC (inter-process communication) model, typically provided by the OS.

#### Pitfalls of Parallel Computing
Introducing parallelism to a program is not always a positive-sum game; there are some pitfalls to be aware of. The most important ones are as follows.
- **Race Condition**: As we already discussed, threads have a shared memory space, and therefore they can have access to shared variables. A race condition occurs when multiple threads try to change the same variable simultaneously. The thread scheduler can arbitrarily swap between threads, so we have no way of knowing the order in which the threads will try to change the data. This can result in incorrect behavior in either of the threads, particularly if the threads decide to do something based on the value of the variable. To prevent this from happening, a mutual exclusion (or mutex) lock can be placed around the piece of the code that modifies the variable so that only one thread can write to the variable at a time.
- **Starvation**: Starvation occurs when a thread is denied access to a particular resource for longer periods of time, and as a result, the overall program slows down. This can happen as an unintended side effect of a poorly designed thread-scheduling algorithm.
- **Deadlock**: Overusing mutex locks also has a downside - it can introduce deadlocks in the program. A deadlock is a state when a thread is waiting for another thread to release a lock, but that other thread needs a resource to finish that the first thread is holding onto. This way, both of the threads come to a standstill and the program halts. Deadlock can be thought of as an extreme case of starvation. To avoid this, we have to be careful not to introduce too many locks that are interdependent.
- **Livelock** : Livelock is when threads keep running in a loop but don’t make any progress. This also arises out of poor design and improper use of mutex locks.

### Multiprocessing and Threading in Python
#### The Global Interpreter Lock
When it comes to Python, there are some oddities to keep in mind. We know that threads share the same memory space, so special precautions must be taken so that two threads don’t write to the same memory location. The CPython interpreter handles this using a mechanism called GIL, or the Global Interpreter Lock.
From the Python wiki:

    In CPython, the global interpreter lock, or GIL, is a mutex that protects access to Python objects, preventing 
    multiple threads from executing Python bytecodes at once. This lock is necessary mainly because CPython's memory 
    management is not thread-safe.

The GIL gets its job done, but at a cost. It effectively serializes the instructions at the interpreter level. How this works is as follows: for any thread to perform any function, it must acquire a global lock. Only a single thread can acquire that lock at a time, which means the interpreter ultimately runs the instructions serially. This design makes memory management thread-safe, but as a consequence, it can’t utilize multiple CPU cores at all. In single-core CPUs, which is what the designers had in mind while developing CPython, it’s not much of a problem. But this global lock ends up being a bottleneck if you’re using multi-core CPUs.

This bottleneck, however, becomes irrelevant if your program has a more severe bottleneck elsewhere, for example in network, IO, or user interaction. In those cases, threading is an entirely effective method of parallelization. But for programs that are CPU bound, threading ends up making the program slower.

#### Use Cases for Threading
GUI programs use threading all the time to make applications responsive. For example, in a text editing program, one thread can take care of recording the user inputs, another can be responsible for displaying the text, a third can do spell-checking, and so on. Here, the program has to wait for user interaction, which is the biggest bottleneck. Using multiprocessing won’t make the program any faster.
Another use case for threading is programs that are IO bound or network bound, such as web-scrapers. In this case, multiple threads can take care of scraping multiple webpages in parallel. The threads have to download the webpages from the Internet, and that will be the biggest bottleneck, so threading is a perfect solution here. Web servers, being network bound, work similarly; with them, multiprocessing doesn’t have any edge over threading. Another relevant example is Tensorflow, which uses a thread pool to transform data in parallel.

#### Use Cases for Multiprocessing
Multiprocessing outshines threading in cases where the program is CPU intensive and doesn’t have to do any IO or user interaction. For example, any program that just crunches numbers will see a massive speedup from multiprocessing; in fact, threading will probably slow it down. An interesting real world example is Pytorch Dataloader, which uses multiple subprocesses to load the data into GPU.

#### Parallelization in Python
Python offers two libraries - multiprocessing and threading- for the eponymous parallelization methods. Despite the fundamental difference between them, the two libraries offer a very similar API (as of Python 3.7).
