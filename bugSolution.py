def function_with_closed_file(filename):
    try:
        with open(filename, 'r') as f:
            # ... some code that processes the file ...
            # The file is automatically closed when exiting the 'with' block
            return something
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return None