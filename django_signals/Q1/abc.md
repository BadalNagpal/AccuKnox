By default, Django signals are executed synchronously. When a signal is sent, it is handled immediately by the connected receiver functions, meaning the execution flow waits for the signal handler to complete before moving on.

The Files provided demonstrate this behavior.
