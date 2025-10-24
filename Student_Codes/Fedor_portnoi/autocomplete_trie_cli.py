import argparse, json, os, sys, heapq

class TrieNode:
    __slots__=("children","end","freq")
    def __init__(self):
        self.children={}
        self.end=False
        self.freq=0

class Trie:
    def __init__(self):
        self.root=TrieNode()
        self.count=0
    def insert(self,word,inc=1):
        node=self.root
        for ch in word.lower():
            node=node.children.setdefault(ch,TrieNode())
        if not node.end:
            node.end=True
            self.count+=1
        node.freq+=inc
    def _walk(self,node,prefix,limit,heap):
        if node.end:
            heapq.heappush(heap,(-node.freq,prefix))
            if len(heap)>limit: heapq.heappop(heap)
        for ch,nxt in node.children.items():
            self._walk(nxt,prefix+ch,limit,heap)
    def suggest_prefix(self,prefix,k=10):
        node=self.root
        for ch in prefix.lower():
            if ch not in node.children: return []
            node=node.children[ch]
        heap=[]
        self._walk(node,prefix.lower(),k,heap)
        return [w for _,w in sorted(heap,reverse=True)]
    def _collect(self,node,prefix,acc):
        if node.end: acc.append((prefix,node.freq))
        for ch,nxt in node.children.items():
            self._collect(nxt,prefix+ch,acc)
    def suggest_fuzzy(self,query,max_dist=1,k=10):
        acc=[]
        self._collect(self.root,"",acc)
        out=[]
        for w,f in acc:
            d=_levenshtein_bounded(w,query.lower(),max_dist)
            if d<=max_dist:
                out.append((d,-f,w))
        out.sort()
        return [w for _,__,w in out[:k]]
    def to_dict(self):
        acc=[]
        self._collect(self.root,"",acc)
        return {w:f for w,f in acc}
    @staticmethod
    def from_dict(d):
        t=Trie()
        for w,f in d.items():
            t.insert(w,f)
        return t

def _levenshtein_bounded(a,b,limit):
    la,lb=len(a),len(b)
    if abs(la-lb)>limit: return limit+1
    prev=list(range(lb+1))
    for i,ca in enumerate(a,1):
        cur=[i]+[0]*lb
        mn=cur[0]
        for j,cb in enumerate(b,1):
            cost=0 if ca==cb else 1
            cur[j]=min(prev[j]+1,cur[j-1]+1,prev[j-1]+cost)
            if cur[j]<mn: mn=cur[j]
        if mn>limit: return limit+1
        prev=cur
    return prev[-1]

DEFAULT_WORDS="""
data structure algorithm analysis array list linked queue stack deque tree trie heap graph vertex edge dfs bfs dijkstra bellman ford kruskal prim union find hash map set dictionary tuple string substring suffix prefix sort merge quick heap bubble insertion selection shell radix count stable unstable recursion iteration dynamic programming memoization tabulation greedy backtracking branch bound complexity runtime big o big theta big omega amortized worst average best case recursion depth tail call pointer reference object class method attribute inheritance polymorphism encapsulation abstraction interface module package import export file io stream buffer binary hex encode decode json csv pickle network socket server client protocol http tcp udp concurrency thread process lock mutex semaphore condition queue future coroutine async await event loop scheduler timer test unit pytest assert mock stub benchmark timeit profiling optimize memo memory cache lru ipc pipe shared memory serialization deserialization random seed shuffle sample probability statistics mean median mode variance stdev math linear algebra matrix vector dot product normalize distance cosine euclidean manhattan knn svm perceptron gradient descent regression classification clustering kmeans dbscan pca tSNE visualization plot render ascii ui cli tui menu prompt parse argparse sys os pathlib pathlib glob re regex compile match search group capture lambda map filter reduce comprehension generator iterator yield context manager with open read write seek flush close try except finally raise error exception valueerror typeerror runtimeerror keyboardinterrupt exit quit swosu bulldogs basketball game stats player coach season
""".split()

def build_default_trie():
    t=Trie()
    for w in DEFAULT_WORDS:
        if w: t.insert(w,1)
    freq_boost=["data","structure","algorithm","analysis","class","object","graph","tree","trie","heap","sort","python","swosu","basketball"]
    for w in freq_boost:
        t.insert(w,5)
    return t

def save_trie(t,path):
    with open(path,"w",encoding="utf-8") as f:
        json.dump(t.to_dict(),f,ensure_ascii=False)

def load_trie(path):
    with open(path,"r",encoding="utf-8") as f:
        return Trie.from_dict(json.load(f))

def interactive(t,model_path):
    print("Autocomplete CLI | prefix: p <text> | fuzzy: f <text> | add: a <word> [freq] | save: s | load: l | top: t <prefix> | quit: q")
    while True:
        try:
            line=input("> ").strip()
        except EOFError:
            print()
            break
        if not line: continue
        cmd,*rest=line.split()
        c=cmd.lower()
        if c in ("q","quit","exit"):
            break
        elif c in ("p","prefix"):
            if not rest: print("need text"); continue
            pref=" ".join(rest)
            res=t.suggest_prefix(pref,10)
            print(", ".join(res) if res else "(none)")
        elif c in ("f","fuzzy"):
            if not rest: print("need text"); continue
            q=" ".join(rest)
            res=t.suggest_fuzzy(q,1,10)
            print(", ".join(res) if res else "(none)")
        elif c in ("a","add"):
            if not rest: print("need word"); continue
            w=rest[0]
            freq=int(rest[1]) if len(rest)>1 and rest[1].isdigit() else 1
            t.insert(w,freq)
            print("ok")
        elif c in ("s","save"):
            if not model_path: print("no model path provided"); continue
            save_trie(t,model_path); print("saved")
        elif c in ("l","load"):
            if not model_path or not os.path.exists(model_path): print("no model file"); continue
            tt=load_trie(model_path); t.root, t.count = tt.root, tt.count; print("loaded")
        elif c in ("t","top"):
            if not rest: print("need prefix"); continue
            pref=" ".join(rest)
            res=t.suggest_prefix(pref,20)
            print("\n".join(res) if res else "(none)")
        else:
            print("unknown")

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--model","-m",default="autocomplete_model.json")
    ap.add_argument("--pref")
    ap.add_argument("--fuzzy")
    ap.add_argument("--k",type=int,default=10)
    ap.add_argument("--maxdist",type=int,default=1)
    ap.add_argument("--add",nargs="+")
    ap.add_argument("--save",action="store_true")
    ap.add_argument("--load",action="store_true")
    ap.add_argument("--interactive","-i",action="store_true")
    args=ap.parse_args()
    t=build_default_trie()
    if args.load and os.path.exists(args.model):
        t=load_trie(args.model)
    if args.add:
        w=args.add[0]; f=int(args.add[1]) if len(args.add)>1 and args.add[1].isdigit() else 1
        t.insert(w,f)
    out=None
    if args.pref:
        out=t.suggest_prefix(args.pref,args.k)
    if args.fuzzy:
        out=t.suggest_fuzzy(args.fuzzy,args.maxdist,args.k)
    if out is not None:
        print("\n".join(out))
    if args.save:
        save_trie(t,args.model)
    if args.interactive or (len(sys.argv)==1):
        interactive(t,args.model)

if __name__=="__main__":
    main()
