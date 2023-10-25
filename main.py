import cProfile
import example

if __name__ == "__main__":
    cProfile.run("example.main()", sort="time")

