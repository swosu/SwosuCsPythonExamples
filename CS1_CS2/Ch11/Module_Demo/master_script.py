import funcs
import script1
import script2

print("\n=== Master Script Demo ===")
print("We can call funcs directly, or rely on script1 and script2 to use it indirectly.\n")

# Direct calls
print("Direct call results:")
a = funcs.fct()
b = funcs.sq()
print(f"funcs.fct() returned {a}")
print(f"funcs.sq() returned {b}")
print(f"Combined (fct * sq): {a * b}")
print()

# Indirect calls
print("Indirect call results:")
print("script1.py and script2.py both use funcs.py under the hood.\n")
import importlib

print("Re-running script1 via importlib:")
importlib.reload(script1)
print("\nRe-running script2 via importlib:")
importlib.reload(script2)

print("\n=== End of Master Script ===")
