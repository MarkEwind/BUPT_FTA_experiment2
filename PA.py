from Grammar import Grammar


class PA:
    def __init__(self, Q, T, Gamma, delta, q0, Z):
        self.Q = Q  #状态集合
        self.T = T  #字符集合
        self.Gamma = Gamma  #栈状态集合
        self.delta = delta  #转移字典，三元组到二元组：(q,t,g)->{(q,(g1,g2)),(q,(g1,g2))，...}
        self.q0 = q0  #初态
        self.Z = Z  #栈初态

    def generate(self):
        G_N = set()
        G_T = self.T
        G_P = {}
        G_S = "@S"
        G_N.add(G_S)
        G_P[G_S] = set()
        for q in self.Q:
            n = (self.q0,self.Z,q)
            G_N.add(n)
            # if n not in G_P.keys():
            #     G_P[n] = set()
            G_P[G_S].add((n,))
        for k,S in self.delta.items():
            for g in S:  #k[0]为初态，k[1]为字符,k[2]为栈状态，g[0]为末态，g[1]为栈末态，元组
                if len(g[1]) == 1 and g[1][0] == "#":
                    n = (k[0],k[2],g[0])
                    G_N.add(n)
                    if n not in G_P.keys():
                        G_P[n] = set()
                    G_P[n].add(k[1])
                    continue
                if k[1] != "#":
                    D = {(k[1],):g[0]}
                else:
                    D = {tuple(): g[0]}
                for gamma in g[1]:
                    D = self.extend(D,gamma)
                for kd,vd in D.items():
                    n2 = (k[0],k[2],vd)
                    if n2 not in G_P.keys():
                        G_P[n2] = set()
                    G_P[n2].add(kd)
        G = Grammar(G_N, G_T, G_P, G_S)
        # G.update2()
        return G

    def print(self):
        print(self.Q)
        print("初态：")
        print(self.q0)
        print("栈初态：")
        print(self.Z)
        print("状态：")
        for q in self.Q:
            print(q,end=",")
        print()
        print("字符：")
        for t in self.T:
            print(t, end=",")
        print()
        print("栈字符：")
        for g in self.Gamma:
            print(g, end=",")
        print()
        for k,v in self.delta.items():
            print("d",end="")
            print(k,end="")
            print("=",end="")
            for l in v:
                print(l,end="")
            print()


    def extend(self,D,Z):
        D_new = {}
        for k,v in D.items():
            for q in self.Q:
                n = (v,Z,q)
                e = k + (n,)
                D_new[e] = q
        return D_new