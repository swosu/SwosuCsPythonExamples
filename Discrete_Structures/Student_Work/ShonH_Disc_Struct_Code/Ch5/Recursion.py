import sys
 # optional: raise limit for testing

def potato_computer(depth=0):
    try:
        # keep calling until Python raises RecursionError
        return potato_computer(depth + 1)
    except RecursionError:
        print(f"Potato computer has reached its limit at depth {depth}!")
        return depth

if __name__ == "__main__":
    potato_computer()
