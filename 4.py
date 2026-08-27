from contextlib import contextmanager

@contextmanager
def my_context():
    print("Starting the context")
    yield
    print("Ending the context")

with my_context():
    print("Inside the context")