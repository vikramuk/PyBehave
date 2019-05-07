from nose.tools import assert_equals
from App.Calculator import Calculator

@given(u'i Launch Calculator')
def step_impl(context):
    #raise NotImplementedError(u'STEP: Given i Launch Calculator')
    calc =Calculator()

@when(u'I start X and Y')
def step_impl(context):
    #raise NotImplementedError(u'STEP: When I start X and Y')
    result = Calculator.add(2,3)

@then(u'the result is Z')
def step_impl(context):
    #raise NotImplementedError(u'STEP: Then the result is Z')
    actual_result = Calculator.add(2,3)
    assert_equals(int(6), actual_result)