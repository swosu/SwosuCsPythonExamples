from Story import Story_class

if __name__ == "__main__":
   print('let it begin!')
   tale = Story_class(42)
   val = tale.getVal()
   print(val)
   tale.print_start()
