
class Function():
    def __init__(self, arg1):
        self.numer = None
        self.denom = None

# interface        
class Constraint:
    def name(self):
        return self.__class__.__name__
        
    def has_same_type(self, obj):
        return self.name() == obj.name()

class HorizontalAsymptote(Constraint):
    def __init__(self, y):
        self.y = y

    def modify_function(self, function):
        # make sure the coefficient of the order of the numerator is
        # less than the order of the denominator.
        pass

    def max_allowed(self): return 1

class VerticalAsymptote(Constraint):
    def __init__(self, x):
        self.x = x

    def modify_function(self, function):
        # ensure the denominator of the function is equal to zero at self.x
        pass

    def max_allowed(self): return 2

class FunctionSpec():
    '''
    this if for order n rational functions
    '''
    def __init__(self):
        self.constraints = []

    def add_constraint(self, c):
        # count how many constraints of this type c have already been added.
        matches = sum(1 for x in self.constraints if x.has_same_type(c))
        
        if matches < c.max_allowed():
            self.constraints.append(c)
            return self
        raise Exception(f"Can't add any more constraints of type: {c.name()}" )
        
    def add_horizontal_asymptote(self, y):
        return self.add_constraint(HorizontalAsymptote(y))
        
    def add_vertical_asymptote(self, x):
        return self.add_constraint(VerticalAsymptote(x))

    
