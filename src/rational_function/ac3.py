# https://en.wikipedia.org/wiki/AC-3_algorithm

# https://www.youtube.com/watch?v=lCrHYT_EhDs
# Forward Checking
# Min Conflicts

# Input:
#   A set of variables X
#   A set of domains D(x) for each variable x in X. D(x) contains vx0, vx1... vxn, the possible values of x
#   A set of unary constraints R1(x) on variable x that must be satisfied
#   A set of binary constraints R2(x, y) on variables x and y that must be satisfied

# Output:
#   Arc consistent domains for each variable.
 
# function ac3 (X, D, R1, R2)
#     // Initial domains are made consistent with unary constraints.
#     for each x in X
#         D(x) := { vx in D(x) | vx satisfies R1(x) }   
#     // 'worklist' contains all arcs we wish to prove consistent or not.
#     worklist := { (x, y) | there exists a relation R2(x, y) or a relation R2(y, x) }
 
#     do
#         select any arc (x, y) from worklist
#         worklist := worklist - (x, y)
#         if arc-reduce (x, y) 
#             if D(x) is empty
#                 return failure
#             else
#                 worklist := worklist + { (z, x) | z != y and there exists a relation R2(x, z) or a relation R2(z, x) }
#     while worklist not empty
 
# function arc-reduce (x, y)
#     bool change = false
#     for each vx in D(x)
#         find a value vy in D(y) such that vx and vy satisfy the constraint R2(x, y)
#         if there is no such vy {
#             D(x) := D(x) - vx
#             change := true
#         }
#     return change


# -----------------------------------------------------------------------------

#   A set of variables X
class Var():
    def __init__(self, domain):
        self.domain = domain
        

#  A set of domains D(x) for each variable x in X. D(x) contains vx0,
#  vx1... vxn, the possible values of x
class Domain():
    def __init__(self, values):
        self.values = values
        
class Value:
    pass

class Agenda:
    def __init__(self):
        self.arc_stack = []

    def empty():
        return bool(self.arc_stack)
        
    def next():
        if self.empty():
            return None
        return self.arc_stack.pop(0)

    def add(self, arc):
        self.arc_stack.append(arc)

# A set of unary constraints R1(x) on variable x that must be satisfied
class UnaryConstraint:
    pass

# A set of binary constraints R2(x, y) on variables x and y that must be satisfied
class BinaryConstraint:
    pass

class AC3():
    def __init__(self, X, R1, R2):
        # A set of variables X
        # A set of domains D(x) for each variable x in X. D(x) contains vx0, vx1... vxn, the possible values of x
        # in this design, X contains the domain.
        self.X = X
        #   A set of unary constraints R1(x) on variable x that must be satisfied
        self.R1 = set() 
        #   A set of binary constraints R2(x, y) on variables x and y that must be satisfied
        self.R2 = set()
        

    # find a value vy in D(y) such that vx and vy satisfy the constraint R2(x, y)
    def satisfy_r2(self, vx):
        pass
    
    
    def arc_reduce(self, x, y):
        #     bool change = false
        #     for each vx in D(x)
        #         find a value vy in D(y) such that vx and vy satisfy the constraint R2(x, y)
        #         if there is no such vy {
        #             D(x) := D(x) - vx
        #             change := true
        #         }
        #     return change
        change = False
        for vx in D(x):
            if not self.satisfy_r2(vx):
                D(x).remove(vx)
            change = True
        return change
            

    # function ac3 (X, D, R1, R2)
    #     // Initial domains are made consistent with unary constraints.
    #     for each x in X
    #         D(x) := { vx in D(x) | vx satisfies R1(x) }   
    #     // 'worklist' contains all arcs we wish to prove consistent or not.
    #     worklist := { (x, y) | there exists a relation R2(x, y) or a relation R2(y, x) }
    
    #     do
    #         select any arc (x, y) from worklist
    #         worklist := worklist - (x, y)
    #         if arc-reduce (x, y) 
    #             if D(x) is empty
    #                 return failure
    #             else
    #                 worklist := worklist + { (z, x) | z != y and there exists a relation R2(x, z) or a relation R2(z, x) }
    #     while worklist not empty
    def ac3(self):
        for x in self.X:
            pass
        pass


    
