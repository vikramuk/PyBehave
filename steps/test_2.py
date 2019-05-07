# coding=utf-8
@given(u'there are 5 cucumbers')
def step_impl(context):
    print('STEP: Given there are 5 cucumbers')


@when(u'I eat 3 cucumbers')
def step_impl(context):
    print('STEP: When I eat 3 cucumbers')


@when(u'I eat 2 cucumbers')
def step_impl(context):
    print('STEP: When I eat 2 cucumbers')


@then(u'I should have 0 cucumbers')
def step_impl(context):
    print('STEP: Then I should have 0 cucumbers')
    assert context.failed is True
