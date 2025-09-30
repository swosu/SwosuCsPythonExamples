import json, random, time, sys
from pathlib import Path

SIZE=9; DIGS=set(range(1,10)); SAVEDIR=Path("saves"); SAVEDIR.mkdir(exist_ok=True)
def now(): return int(time.time())

def solve(board,limit=2):
    rows=[set(r)-{0} for r in board]
    cols=[{board[r][c] for r in range(SIZE)}-{0} for c in range(SIZE)]
    box = lambda r,c:(r//3)*3+(c//3)
    boxes=[set() for _ in range(9)]
    for r in range(SIZE):
        for c in range(SIZE):
            v=board[r][c]
            if v: boxes[box(r,c)].add(v)
    empt=[(r,c) for r in range(SIZE) for c in range(SIZE) if board[r][c]==0]
    sols=[]
    def cand(r,c): return DIGS-rows[r]-cols[c]-boxes[box(r,c)]
    empt.sort(key=lambda rc: len(cand(*rc)))
    def bt(i=0):
        if len(sols)>=limit: return
        if i==len(empt): sols.append([row[:] for row in board]); return
        r,c=empt[i]
        for v in sorted(cand(r,c), key=lambda _:random.random()):
            board[r][c]=v; rows[r].add(v); cols[c].add(v); boxes[box(r,c)].add(v)
            bt(i+1)
            boxes[box(r,c)].remove(v); cols[c].remove(v); rows[r].remove(v); board[r][c]=0
    bt(); return sols

def gen(digs_to_remove):
    base= [[0]*SIZE for _ in range(SIZE)]
    nums=list(range(1,10)); random.shuffle(nums)
    for i in range(3):
        for r in range(3):
            for c in range(3):
                base[i*3+r][i*3+c]=nums[(r*3+c+i)%9]
    solve(base,limit=1)  # fill fully via solver starting from seeded grid
    full=solve(base,limit=1)[0]
    puzzle=[row[:] for row in full]
    holes=list((r,c) for r in range(SIZE) for c in range(SIZE))
    random.shuffle(holes); removed=0
    for r,c in holes:
        if removed>=digs_to_remove: break
        tmp=puzzle[r][c]; puzzle[r][c]=0
        if len(solve([row[:] for row in puzzle],limit=2))!=1:
            puzzle[r][c]=tmp
        else:
            removed+=1
    return puzzle, full

def fmt(board,fixed=None):
    out=[]
    for r in range(SIZE):
        row=[]
        for c in range(SIZE):
            v=board[r][c]
            if v==0: row.append(" .")
            elif fixed and fixed[r][c]: row.append(f" {v}")
            else: row.append(f" {v}")
        out.append(("".join(row[:3])+" |"+ "".join(row[3:6])+" |"+ "".join(row[6:])))
        if r in (2,5): out.append("-"*22)
    return "\n".join(out)

def fixed_mask(puzzle):
    return [[1 if puzzle[r][c]!=0 else 0 for c in range(SIZE)] for r in range(SIZE)]

class Game:
    def __init__(self,puzzle,solution):
        self.p=[row[:] for row in puzzle]
        self.s=solution
        self.f=fixed_mask(puzzle)
        self.t0=now()
    def set(self,r,c,v):
        if self.f[r][c]: return "Cell is fixed."
        if v not in DIGS: return "Value must be 1-9."
        self.p[r][c]=v; return "OK"
    def hint(self):
        for r in range(SIZE):
            for c in range(SIZE):
                if self.p[r][c]==0:
                    self.p[r][c]=self.s[r][c]; return f"Hint: set ({r+1},{c+1}) to {self.s[r][c]}"
        return "Board already complete."
    def complete(self): return self.p==self.s
    def valid(self):
        def ok(group): 
            g=[x for x in group if x!=0]; 
            return len(g)==len(set(g))
        for i in range(SIZE):
            if not ok(self.p[i]): return False
            if not ok([self.p[r][i] for r in range(SIZE)]): return False
        for br in range(0,9,3):
            for bc in range(0,9,3):
                block=[self.p[r][c] for r in range(br,br+3) for c in range(bc,bc+3)]
                if not ok(block): return False
        return True
    def to_dict(self):
        return {"p":self.p,"s":self.s,"f":self.f,"t0":self.t0}
    @staticmethod
    def from_dict(d):
        g=Game(d["p"],d["s"]); g.f=d["f"]; g.t0=d["t0"]; return g

def digs_for_difficulty(level):
    return {"easy":40,"med":50,"hard":58,"insane":62}.get(level,50)

def save(name,game):
    data=game.to_dict()
    (SAVEDIR/f"{name}.json").write_text(json.dumps(data))
def load(name):
    d=json.loads((SAVEDIR/f"{name}.json").read_text()); return Game.from_dict(d)
def load_stats():
    path=Path("stats.json")
    if path.exists(): return json.loads(path.read_text())
    return {"games":0,"wins":0,"avg_time":0}
def save_stats(st):
    Path("stats.json").write_text(json.dumps(st))

def new_game(level):
    puzzle,sol=gen(digs_for_difficulty(level))
    return Game(puzzle,sol)

def main():
    print("Sudoku Master — type 'help' for commands.")
    st=load_stats(); game=None
    while True:
        try:
            cmd=input("> ").strip().split()
        except EOFError:
            print(); break
        if not cmd: continue
        op=cmd[0].lower()
        if op=="new":
            lvl=cmd[1].lower() if len(cmd)>1 else "med"
            game=new_game(lvl); st["games"]+=1
            print(f"New {lvl} game:\n"+fmt(game.p,game.f))
        elif op=="show":
            print(fmt(game.p,game.f) if game else "No game.")
        elif op=="set":
            if not game or len(cmd)!=4: print("Usage: set r c v"); continue
            try:
                r,c,v=map(int,cmd[1:]); r-=1;c-=1
                if not (0<=r<9 and 0<=c<9): print("Row/Col 1-9."); continue
                print(game.set(r,c,v))
            except ValueError:
                print("Use integers: set r c v")
        elif op=="hint":
            print(game.hint() if game else "No game.")
        elif op=="check":
            if not game: print("No game."); continue
            print("Valid." if game.valid() else "Invalid.")
            if game.complete():
                dt=now()-game.t0; st["wins"]+=1
                n=st["wins"]; st["avg_time"]= (st["avg_time"]*(n-1)+dt)/n
                print(f"Complete! Time: {dt}s")
        elif op=="solve":
            if not game: print("No game."); continue
            game.p=[row[:] for row in game.s]; print(fmt(game.p,game.f)); print("Solved.")
        elif op=="save":
            if not game: print("No game."); continue
            name=cmd[1] if len(cmd)>1 else f"game_{int(time.time())}"
            save(name,game); print(f"Saved as {name}.")
        elif op=="load":
            if len(cmd)<2: print("Usage: load name"); continue
            try:
                game=load(cmd[1]); print("Loaded.\n"+fmt(game.p,game.f))
            except FileNotFoundError:
                print("Save not found.")
        elif op=="stats":
            print(f"Games:{st['games']} Wins:{st['wins']} AvgTime:{int(st['avg_time'])}s")
        elif op=="help":
            print("new [easy|med|hard|insane], set r c v, hint, check, solve, save [name], load name, show, stats, quit")
        elif op in ("quit","exit"):
            break
        else:
            print("Unknown command. Type 'help'.")
    save_stats(st)

if __name__=="__main__":
    try: main()
    except KeyboardInterrupt: print("\nBye."); sys.exit(0)
