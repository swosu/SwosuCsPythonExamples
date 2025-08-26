f0 = float(input("Enter your key frequency:"))
f1 = float(f0*((2**(1/12))**1))
f2 = float(f0*((2**(1/12))**2))
f3 = float(f0*((2**(1/12))**3))
f4 = float(f0*((2**(1/12))**4))
print('{:.2f} {:.2f} {:.2f} {:.2f} {:.2f}'.format(f0,f1,f2,f3,f4))

