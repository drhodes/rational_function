import pytest
from rational_function.spec import FunctionSpec

# nice pytest.raises handling.
# https://stackoverflow.com/a/56569533/98770        

def test_function_spec_init():
    spec = FunctionSpec()

def test_dont_add_more_than_one_horizontal_asymptote():
    s = FunctionSpec()
    s.add_horizontal_asymptote(1)
    msg = "Can't add any more constraints of type: HorizontalAsymptote"
    with pytest.raises(Exception, match=msg) as e:
        s.add_horizontal_asymptote(42)    
    
