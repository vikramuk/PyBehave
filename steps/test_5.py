# coding=utf-8
from behave   import given, when, then

@given(u'I am an author user')
def step_impl(context):
	pass
	print(u'STEP: Given I am an author user')


@given('I have an article')
def i_have_an_article(context):
	pass

@when('I go to the article page')
def i_go_to_the_article_page(context):
	pass


@when('I press the publish button')
def i_press_the_publish_button(context):
	pass	



@then('I should not see the error message')
def i_should_not_see_the_error_message(context):
	pass	
	
	"""I should not see the error message.
	raise NotImplementedError"""


@then('the article should be published')
def the_article_should_be_published(context):
	pass    
'''
@then(u'the article should be published  # Note: will query the database')
def step_impl(context):
    print('STEP: Then the article should be published  # Note: will query the database')
'''

@then(u'I can check')
def step_impl(context):
	print('STEP: Then I can check ')	 # should Fail for this')
	assert context.failed is True
