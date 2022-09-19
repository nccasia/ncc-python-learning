## Parallel computers

 - Multiprocessor/multicore: several processors work on data stored in shared memory
 - Cluster: several processor/memory units work together by exchanging data over a network
 - Co-processor: a general-purpose processor delegates specific tasks to a special-purpose processor (GPU)

## Parallel Programming

 - Decomposition of the complete task into independent subtasks and the data flow between them.
 - Distribution of the subtasks over the processors minimizing the total execution time.
 - For clusters: distribution of the data over the nodes minimizing the communication time.
 - For multiprocessors: optimization of the memory access patterns minimizing waiting times.
 - Synchronization of the individual processes.

## Thread and Process: Differences
 - A process is an instance of a running program.
 - Process may contain one or more threads, but a thread cannot contain a process.
 - Process has a self-contained execution environment. It has its own memory space.
 - Application running on your computer may be a set of cooperating processes.
 - Process don't share its memory, communication between processes implies data serialization.
 - A thread is made of and exist within a process; every process has at least one thread
 - Multiple threads in a process share resources, which helps in efficient communication between threads.
 - Threads can be concurrent on a multi-core system, with every core executing the separate threads simultaneously.


## The Global Interpreter Lock (GIL)
 - The Python interpreter is not thread safe.
 - A few critical internal data structures may only be accessed by one thread at a time
 - Access to them is protected by the GIL.
 - Attempts at removing the GIL from Python have failed until now. The main difficulty is maintaining the C API for extension modules.
 - Multiprocessing avoids the GIL by having separate processes which each have an independent copy of the interpreter data structures.
 - The price to pay: serialization of tasks, arguments, and results.


