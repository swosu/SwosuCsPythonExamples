import sys

sys.setrecursionlimit(3000)  # Be careful! Don’t go too high.


def potato_computer(depth=1):
    return potato_computer(depth * 2)

if __name__ == "__main__":
    potato_computer()


