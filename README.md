This code simulates the BB84 protocol in Python.

The code has support for:

-Custom basis angles (not applicable to BB84)

-Viewing stats

-Averaging the key length to verify the expectation value of key length (N/2)

-Eve the eavesdropper

This code is semi-heuristic and is not optimal. It is entirely for demonstartion purposes and cannot be used to implement BB84 properly. Function names are a little verbose and functions could pass to each other, however I wanted it to be as readable as possible for non-programmers.

testfile.py <- This program runs the code as many times as the user requires with a user specified number of transmission bits. It then simulates BB84 and returns the average final key length. For `eve = True` the output is ~25% of the initial length and for `eve = False` the output is ~50% of the initial length.

There is no input sanitisation as it is unnecessary in this application.
