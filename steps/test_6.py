# coding=utf-8
from behave   import given, when, then

@given(u'the basket has {initial} cucumbers')
def step_impl(context,initial):
    print('Initial')


@when(u'{more} cucumbers are added to the basket')
def step_impl(context,more):
    print('More')


@then(u'the basket contains {total} cucumbers')
def step_impl(context,total):
    print('total')
    assert total == initial + more