def hello_world():
    print("Hello World!")
    raise RuntimeError("boom")

if __name__ == "__main__":
    hello_world()
