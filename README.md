# Unclosed File Handle Bug

This repository demonstrates a common but often overlooked bug in Python: unclosed file handles.  Failure to close files properly can lead to resource exhaustion and potential data corruption.  This example showcases the problem and provides a solution.

## Bug Description

The `bug.py` file contains a function that opens a file for reading but fails to close it.  This is problematic because operating systems typically have a limited number of file handles available, and leaving them open can eventually deplete these resources.  In addition, the data in the file might not be fully flushed to disk.

## Solution

The `bugSolution.py` file shows the corrected code, using a `with` statement to ensure the file is automatically closed, even if exceptions occur.