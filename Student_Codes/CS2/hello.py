import sys

print('hello')



class HelloWorld:

    @staticmethod
    def main(args: list[str]) -> None:
        sys.stdout.write("Hello World\n")


if __name__ == "__main__":
    HelloWorld.main(sys.argv)
