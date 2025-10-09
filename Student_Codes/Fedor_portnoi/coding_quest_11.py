import math, random
from datetime import date, timedelta

class Artist:
    def __init__(self, name="unknown", birth_year=-1, death_year=-1):
        self.name=name; self.birth_year=birth_year; self.death_year=death_year
    def print_info(self):
        if self.birth_year>=0 and self.death_year>=0:
            print(f'Artist: {self.name} ({self.birth_year} to {self.death_year})')
        elif self.birth_year>=0:
            print(f'Artist: {self.name} ({self.birth_year} - present)')
        else:
            print(f'Artist: {self.name} (unknown)')

class Artwork:
    def __init__(self, title="unknown", year_created=-1, artist=None):
        self.title=title; self.year_created=year_created; self.artist=artist if artist else Artist()
    def print_info(self):
        self.artist.print_info(); print(f'Title: {self.title}, {self.year_created}')

def quadratic_formula(a,b,c):
    d=b*b-4*a*c
    x1=(-b+math.sqrt(d))/(2*a)
    x2=(-b-math.sqrt(d))/(2*a)
    return (x1,x2)

retries=0
def unique_random_ints(how_many,max_num,seed):
    global retries
    random.seed(seed)
    retries=0
    out=[]
    while len(out)<how_many:
        r=random.randint(0,max_num)
        if r in out: retries+=1
        else: out.append(r)
    return out

def read_date(s):
    y,m,d=map(int,s.split('-'))
    return date(y,m,d)

def compute_Nt(N0,t,T):
    return N0*math.exp((-0.693*t)/T)

def compute_T(N0,Nt,t):
    return (-0.693*t)/math.log(Nt/N0)

def print_number(n,prefix):
    if float(int(n))==n: print(f'{prefix}{n:.0f}')
    else: print(f'{prefix}{n:.2f}')

def bar(x,scale=1):
    n=max(0,int(x/scale))
    return "█"*n

print("=== MODULES SHOWCASE ===")

print("\n-- Artwork Labels --")
art1=Artwork("Three Musicians",1921,Artist("Pablo Picasso",1881,1973))
art2=Artwork("Distant Muses",2000,Artist("Brice Marden",1938,-1))
art3=Artwork("Balloon Girl",2002,Artist("Banksy",-1,-1))
for a in (art1,art2,art3): a.print_info()

print("\n-- Quadratic Formula Demo --")
a,b,c=2.0,-3.0,-77.0
x1,x2=quadratic_formula(a,b,c)
print(f'Solutions to {a:.0f}x^2 + {b:.0f}x + {c:.0f} = 0')
print_number(x1,'x1 = ')
print_number(x2,'x2 = ')

print("\n-- Random Unique Integers --")
nums=unique_random_ints(5,7,seed=2)
print(*nums, end=' ')
print(f'retries={retries}')

print("\n-- Dates Toolkit --")
dates=[read_date('2022-01-27'),read_date('2022-07-04'),read_date('2020-12-31'),read_date('2022-07-29')]
sorted_dates=sorted(dates)
for d in sorted_dates: print(d.strftime('%m/%d/%Y'))
print((sorted_dates[-1]-sorted_dates[-2]).days)
print((sorted_dates[-1]+timedelta(weeks=3)).strftime('%B %d, %Y'))
print(sorted_dates[0].strftime('%A'))

print("\n-- Radioactive Decay --")
N0,t,T=100.0,50.0,28.94
Nt=compute_Nt(N0,t,T)
print(f'Nt = {Nt:.4f}')
Tb=compute_T(100.0,30.2007,50.0)
print(f'T = {Tb:.4f}')

print("\n-- Extra: Random Quadratics With Guaranteed Integer Roots --")
random.seed(11)
for i in range(3):
    r1=random.randint(-7,7) or 1
    r2=random.randint(-7,7) or -2
    a=1; b=-(r1+r2); c=r1*r2
    x1,x2=quadratic_formula(a,b,c)
    print(f'Eq{i+1}: x^2 + {b:+d}x + {c:+d} = 0 -> roots: {int(x1)}, {int(x2)}')

print("\n-- Extra: ASCII Decay Chart (N0=100, T=28.94) --")
for years in range(0,101,10):
    n=compute_Nt(100.0,years,28.94)
    print(f'{years:3d}y | {bar(n,scale=2)} {n:6.2f}')
