def function_with_unclosed_file(filename):
    f = open(filename, 'r')
    # ... some code that processes the file ...
    # The file is never closed here, which is a bug.  This can lead to resource leaks if many files are opened.  It can also lead to data corruption in some situations.
    return something