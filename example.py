import time

def slow_function():
    time.sleep(1)

def fast_function():
    pass

def main():
    for _ in range(10):
        slow_function()
        fast_function()

if __name__ == "__main__":
    main()