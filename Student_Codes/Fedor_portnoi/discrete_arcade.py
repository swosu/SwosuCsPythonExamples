import itertools, math, random, sys
from collections import deque, defaultdict

def rand_map(n, p):
    m=defaultdict(list)
    for i in range(n):
        for j in range(i+1,n):
            if random.random()<p:
                m[i].append(j); m[j].append(i)
    if n>1:
        for i in range(n-1):
            if (i+1) not in m[i]:
                m[i].append(i+1); m[i+1].append(i)
    return m

def bfs_route(m, start, goal):
    q=deque([start]); prev={start:None}
    while q:
        u=q.popleft()
        if u==goal: break
        for v in m[u]:
            if v not in prev:
                prev[v]=u; q.append(v)
    if goal not in prev: return []
    route=[]; cur=goal
    while cur is not None:
        route.append(cur); cur=prev[cur]
    return route[::-1]

def show_map(m):
    cities=sorted(m.keys())
    print(f'Cities: {cities}')
    for c in cities:
        print(f'City {c} has roads to: {sorted(m[c])}')

def derangements(n):
    d=0
    for k in range(n+1):
        d += ((-1)**k) * math.factorial(n)//math.factorial(k)
    return d

def catalan(n):
    return math.comb(2*n, n)//(n+1)

def nim_ai(heaps):
    x=0
    for h in heaps: x^=h
    if x==0:
        for i,h in enumerate(heaps):
            if h>0: return i, h-1
    for i,h in enumerate(heaps):
        t=h^x
        if t<h: return i, t
    return 0, max(0,heaps[0]-1)

def play_nim_coins():
    heaps=[random.randint(1,7) for _ in range(random.randint(3,5))]
    turn=random.choice(['you','ai'])
    print(f'Piles of coins: {heaps}  (on your turn, take any positive number of coins from ONE pile)')
    print(f'{turn.upper()} moves first.')
    while sum(heaps)>0:
        if turn=='you':
            print(f'Piles: {heaps}')
            try:
                i=int(input('Which pile index? '))
                r=int(input('How many coins to take? '))
            except:
                print('invalid'); continue
            if i<0 or i>=len(heaps) or r<=0 or r>heaps[i]:
                print('invalid'); continue
            heaps[i]-=r
            if sum(heaps)==0:
                print('You took the last coin. You win!')
                return
            turn='ai'
        else:
            i,t = nim_ai(heaps)
            r=heaps[i]-t
            print(f'AI takes {r} coin{"s" if r!=1 else ""} from pile {i}')
            heaps[i]=t
            if sum(heaps)==0:
                print('AI took the last coin. AI wins!')
                return
            turn='you'

def menu():
    while True:
        print('\nDiscrete Structures Arcade — City Map & Route, Counting, Nim (Coins)')
        print('1) Build a random City Map and find the fastest Road Route (BFS)')
        print('2) Combinatorics: derangements & Catalan numbers')
        print('3) Play Nim with piles of COINS vs optimal AI')
        print('4) Quit')
        choice=input('Select: ').strip()
        if choice=='1':
            print('\nYou will build a City Map (cities + roads) and compute the fastest Route between two cities.')
            try:
                n=int(input('How many cities? (4–20): '))
                p=float(input('Chance that a road exists between any two cities (0..1, e.g., 0.30): '))
            except:
                print('invalid'); continue
            n=max(4,min(20,n)); p=max(0.0,min(1.0,p))
            m=rand_map(n,p)
            print('\nCity Map (which cities have roads between them):')
            show_map(m)
            try:
                s=int(input('\nPick a START city id (0..{}): '.format(n-1)))
                t=int(input('Pick a DESTINATION city id (0..{}): '.format(n-1)))
            except:
                print('invalid'); continue
            if s not in m or t not in m:
                print('City ids out of range'); continue
            route=bfs_route(m,s,t)
            if not route:
                print('No road route connects those two cities. Try a higher road chance next time.')
            else:
                hops=len(route)-1
                print('Fastest Route by number of roads:')
                print('  ' + ' -> '.join(f'City {x}' for x in route) + f'   ({hops} road{"s" if hops!=1 else ""})')
        elif choice=='2':
            try:
                n=int(input('n (0..15) for derangements and Catalan: '))
            except:
                print('invalid'); continue
            n=max(0,min(15,n))
            d=derangements(n)
            c=catalan(n)
            print(f'!{n} (derangements) = {d}')
            if n>0:
                print(f'P(no one keeps their own spot) ≈ {d}/{math.factorial(n)} = {d/math.factorial(n):.6f} (→ 1/e)')
            print(f'Catalan({n}) = {c}')
        elif choice=='3':
            play_nim_coins()
        elif choice=='4':
            print('Bye'); return
        else:
            print('invalid')

if __name__=='__main__':
    try:
        menu()
    except KeyboardInterrupt:
        sys.exit(0)
