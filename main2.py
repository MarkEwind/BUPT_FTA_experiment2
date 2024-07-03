from PA import *
from Grammar import *
Q = {"q0","q1"}
T = {'a','b','#'}
Gamma = {"B","Z0", "#"}
delta = {("q0","b","Z0"):{("q0",("B","Z0"))},
         ("q0","b","B"):{("q0",("B","B"))},
         ("q0","a","B"):{("q1",("#",))},
         ("q1","a","B"):{("q1",("#",))},
         ("q1","#","B"):{("q1",("#",))},
         ("q1","#","Z0"):{("q1",("#",))}}
q0 = "q0"
Z0 = "Z0"

# Q = {"q0","q1"}
# T = {'a','b','#'}
# Gamma = {"B","Z0", "#"}
# delta = {("q0","b","Z0"):{("q0",("B","Z0"))},
#          ("q0","b","B"):{("q0",("B","B"))},
#          ("q0","a","B"):{("q1",("B",))},
#          ("q1","a","Z0"):{("q0",("Z0",))},
#          ("q0","#","Z0"):{("q0",("#",))},
#          ("q1","b","B"):{("q1",("#",))}}
# q0 = "q0"
# Z0 = "Z0"

pa = PA(Q,T,Gamma,delta,q0,Z0)

pa.print()

g = pa.generate()
g.print()
g.algorithm1()
g.print()
g.algorithm2()
g.print()
g.algorithm3()
g.print()
g.algorithm4()
g.print()

