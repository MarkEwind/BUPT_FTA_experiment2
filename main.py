from Grammar import Grammar
from PA import PA

N = {"S","A","B","C","D",}
T = {"#","a","b","c","d",}
P = {"S":{("a",),("b","A"),("B",),("c","c","D")},
     "A":{("a","b","B"),("#",)},
     "B":{("a","A")},
     "C":{("d","d","C")},
     "D":{("d","d","d")},
     }
S = "S"
G = Grammar(N,T,P,S)
G.print()
G.algorithm1()
G.print()
G.algorithm2()
G.print()
G.algorithm3()
G.print()
G.algorithm4()
G.print()

# print("输入状态集，逗号隔开")
# str = input()
# strs = str.split(',')
# for s in strs:
#     N.add(s)
#
# print("输入字符集，逗号隔开")
# str = input()
# strs = str.split(',')
# for s in strs:
#     T.add(s)
#
# while True:
#     print("输入转移起点，#结束")
#     str = input()
#     if str == "#":
#         break
#     if str not in P:
#         P[str] = set()
#     print("输入串，逗号隔开")
#     str2 = input()
#     strs = str2.split(',')
#     for s in strs:
#         P[str].add(tuple([char for char in s]))
#
# print("输入起点")
# S = input()



# G = Grammar(N,T,P,S)
# G.print()
# G.algorithm1()
# G.print()
# G.algorithm2()
# G.print()
# G.algorithm3()
# G.print()
# G.algorithm4()
# G.print()

# A = {"S"}
# B = {('a', 'S', 'b', 'S'): 0, ('b', 'S', 'a', 'S'): 0, ("#",):0}
# E1 = B
# E2 = seperate(E1,A)
# # while E1 != E2:
# #     E2 = seperate(E1,A)
# print(E2)
# print(seperate({("S",):0},A))
# while E1 != E2:
#     E1 = E2
#     E2 = seperate(E1, A)
# print(E2)

(Q,T,Gamma,delta,p0,Z) = G.generate()
pa = PA(Q,T,Gamma,delta,p0,Z)
pa.print()
G2 = pa.generate()
G2.print()