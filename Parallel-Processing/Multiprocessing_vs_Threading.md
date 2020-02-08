


### Process
A process is an instance of a computer program being executed. Each process has its own memory space it uses to store the instructions being run, as well as any data it needs to store and access to execute.

### Threads
Threads are components of a process, which can run parallely. There can be multiple threads in a process, and they share the same memory space, i.e. the memory space of the parent process. This would mean the code to be executed as well as all the variables declared in the program would be shared by all threads.

### Technical details
- All the threads of a process live in the same memory space, whereas processes have their separate memory space.
- Threads are more lightweight and have lower overhead compared to processes. Spawning processes is a bit slower than spawning threads.
- Sharing objects between threads is easier, as they share the same memory space. To achieve the same between process, we have to use some kind of IPC (inter-process communication) model, typically provided by the OS.

### Pitfalls of Parallel Computing

Introducing parallelism to a program is not always a positive-sum game; there are some pitfalls to be aware of. The most important ones are as follows.
- **Race Condition**: As we already discussed, threads have a shared memory space, and therefore they can have access to shared variables. A race condition occurs when multiple threads try to change the same variable simultaneously. The thread scheduler can arbitrarily swap between threads, so we have no way of knowing the order in which the threads will try to change the data. This can result in incorrect behavior in either of the threads, particularly if the threads decide to do something based on the value of the variable. To prevent this from happening, a mutual exclusion (or mutex) lock can be placed around the piece of the code that modifies the variable so that only one thread can write to the variable at a time.
- **Starvation**: Starvation occurs when a thread is denied access to a particular resource for longer periods of time, and as a result, the overall program slows down. This can happen as an unintended side effect of a poorly designed thread-scheduling algorithm.
- **Deadlock**: Overusing mutex locks also has a downside - it can introduce deadlocks in the program. A deadlock is a state when a thread is waiting for another thread to release a lock, but that other thread needs a resource to finish that the first thread is holding onto. This way, both of the threads come to a standstill and the program halts. Deadlock can be thought of as an extreme case of starvation. To avoid this, we have to be careful not to introduce too many locks that are interdependent.
- **Livelock** : Livelock is when threads keep running in a loop but don’t make any progress. This also arises out of poor design and improper use of mutex locks.
