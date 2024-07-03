

class Grammar:
    def __init__(self, N, T, P, S):
        self.N = N  #状态集合
        self.T = T  #字符集合
        self.P = P  #边字典，状态->集合，元素为元组
        self.S = S  #初态

    def print(self):
        print("初态：")
        print(self.S)
        print("状态：")
        for i in self.N:
            print(i,end="，")
        print("\n字符：")
        for i in self.T:
            print(i,end="，")
        print("\n边：")
        for k,v in self.P.items():
            print(k, end="  --->  ")
            x = 0
            for s in v:
                for s1 in s:
                    print(s1, end="")
                if x < len(v) - 1:
                    print("|",end="")
                x += 1
            print()
        print()
    def update(self, N_new, T_new):  # 给出新状态和字符集合，更新文法
        for q, S in self.P.items():  # 遍历每个键值对
            if q not in N_new:  # 如果状态不在新状态里面就跳过，主要处理值的问题
                continue
            to_remove = set()  # 需要删除的值（集合）
            for l in S:
                flag = 0
                for x in l:
                    if x not in N_new and x not in T_new:  # 如果语句有元素不在新状态以及新字符集里，记录一下
                        flag = 1
                        break
                if flag:  # 将包含非法字符的语句添加到需要删除的集合中
                    to_remove.add(l)
            S -= to_remove  # 将其删除
        self.N = N_new
        self.T = T_new
        self.P = {k: v for k, v in self.P.items() if k in self.N}
    def algorithm1(self):
        T_fin = self.T  # 开始终结符集合就是T
        N0 = {}  # 开始有用集合为空
        N_new = self.search1(T_fin)  # N_new 为可导出终结串的状态集合
        while N_new != N0:  # 如果有用集合不是可导出终结串的状态集合
            N0 = N_new
            T_fin = T_fin.union(N_new)  # 将可导出终结串的状态加入终结状态集合
            N_new = self.search1(T_fin)  # 产生新的可导出终结串集合
        self.update(N0, self.T)

    def algorithm2(self):
        N0 = {self.S}  # 一开始只有初态
        N_new = self.search2(N0)  # 从初态找所有可导字符
        N_new = N_new.union(N0)  # 与初态取并集
        while N_new != N0:  # 如果还有可导的字符
            N0 = N_new
            N_new = self.search2(N0)  # 那就再找
            N_new = N_new.union(N0)  # 导出字符与原集合取并
        self.update(N0.intersection(self.N), N0.intersection(self.T))

    def algorithm3(self):
        T_fin = {"#"}  # 开始终结符集合就是空字符
        N0 = {}  # 开始有用集合为空
        N_new = self.search1(T_fin)  # N_new 为可导出空的状态集合
        while N_new != N0:  # 如果有用集合不是可导出空的状态集合
            N0 = N_new
            T_fin = T_fin.union(N_new)  # 将可导出空的状态加入终结状态集合
            N_new = self.search1(T_fin)  # 产生新的可导出空集合
        P_new = {}
        for q, S in self.P.items():  # 对于每个状态，计算出去空串的串集合，并加入到新边中
            S1 = {k: 0 for k in S}
            S2 = seperate(S1, N0)
            while S1 != S2:
                S1 = S2
                S2 = seperate(S1, N0)
            P_new[q] = {v for v in S1.keys()}
        if self.S in N0:
            P_new["#S"] = {(self.S, "#")}
            self.S = "#S"
            self.N.add(self.S)
        else:
            self.T.remove("#")
        self.P = P_new
        self.algorithm1()
    def algorithm4(self):
        P_new = {}
        for q, S in self.P.items():
            Q0 = {q}
            Q1 = self.search4(Q0)
            Q1 = Q1.union(Q0)
            while Q1 != Q0:
                Q0 = Q1
                Q1 = self.search4(Q0)
                Q1 = Q1.union(Q0)
            S_new = set()
            for p in Q0:
                S_new = S_new.union(self.P[p])
            S_new = {s for s in S_new if not (len(s) == 1 and s[0] in self.N)}
            P_new[q] = S_new
        self.P = P_new

    def search2(self, N0):  # 给出状态集合，给出其可导的状态和字符
        N_new = set()
        for n in N0:  # 遍历状态集合的元素
            if n not in self.N:  # 如果不是状态就跳过，可能为字符
                continue
            s = self.P[n]
            for l in s:  # 遍历语句集合的每一个元素
                for x in l:  # 遍历语句的每一个字符
                    if x in self.N or x in self.T:  # 如果在状态和字符集合就加到可导集合中
                        N_new.add(x)
        return N_new

    def search1(self, T_fin):  # 给终结符集合Tfin，找到所有可以导出全终结符串的状态集合
        N = set()
        for q, S in self.P.items():  # 遍历字典的状态和对应列表集合
            for l in S:  # 遍历列表集合的列表
                flag = 1
                for x in l:  # 遍历列表的每一个元素
                    if x not in T_fin:  # 如果有元素不是终结符
                        flag = 0
                if flag:  # 可推出终结符集合
                    N.add(q)
                    break
        return N

    def search4(self, Q0):
        N0 = Q0
        N_new = set()
        for n in N0:
            for l in self.P[n]:
                if len(l) == 1 and l[0] in self.N:
                    N_new.add(l[0])
        return N_new

    def generate(self):
        Q = {"q0"}
        print(Q)
        T = self.T
        Gamma = self.T.union(self.N)
        q0 = "q0"
        Z = self.S
        d = {}

        for k,v in self.P.items():
            q = (q0,"#",k)
            d[q] = set()
            for l in v:
                d[q].add((q0, l))
        for t in self.T:
            if t == "#":
                continue
            q = (q0,t,t)
            d[q] = {(q0,"#")}
        return Q, T, Gamma, d, q0, Z

def seperate(E, A):  # 给出一个句子加序的字典，可导空状态集，返回新的字典
    E_new = {}
    for k, v in E.items():  #   E为字典，键为待操作的集合，值为待操作的序
        if v >= len(k):  #   如果序大于串的长度，说明已操作完成，将其加入新边中
            E_new[k] = v
            continue
        if len(k) == 1 and k[0] == "#":  #   如果是导空状态，删掉导空边
            continue
        if len(k) == 1 and k[0] in A:  #   如果导出的为单空生成式，避免无意义运算，直接跳过
            E_new[k] = 1
            continue
        for i in range(v, len(k)):  #   从序开始遍历串
            E_new[k] = i + 1  #   先将原串加入到新字典中，并且序加1
            if k[i] in A:  # 如果碰到导空状态
                if i == len(k) - 1:  # 如果状态在末尾，则添加删除末尾状态的串
                    T_new = k[:-1]
                else:  # 如果状态不在末尾，就加入删掉导空状态的串
                    T_new = k[:i] + k[i + 1:]
                if T_new == None:
                    continue
                E_new[T_new] = i  # 因为串的长度缩小，序比原先减1
                break
    return E_new
