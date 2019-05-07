# coding=utf-8
"""parametrized feature tests."""
'''
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('4.feature', 'Parametrized given, when, thens')
def test_parametrized_given_when_thens():
	pass
    
	"""Parametrized given, when, thens."""

'''
from behave   import given, when, then


@given('there are <start> cucumbers')
def there_are_start_cucumbers(context):
	print("Start Cucumber")

@when('I eat <eat> cucumbers')
def i_eat_eat_cucumbers(context):
	print("Eat Cucumber")


@then('I should have <left> cucumbers')
def i_should_have_left_cucumbers(context):
	print("Left Cucumber")


