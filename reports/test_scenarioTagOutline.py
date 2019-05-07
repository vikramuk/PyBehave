# coding=utf-8
import json
from behave import given, when, then
#https://stackoverflow.com/questions/52635025/how-can-i-pass-an-object-like-a-list-or-dictionary-in-python-behave-feature-fil
@given('a {dictionary} and {a_list}')
def given_dict_and_list(context, dictionary, a_list):
    context.dictionary = json.loads(dictionary)
    context.a_list = json.loads(a_list)

@when('we insert them')
def insert_data(context):
    print('inserting dictionary', context.dictionary)
    print('inserting list', context.a_list)

@then('we confirm the result in the database')
def confirm(context):
    print('checking dictionary', context.dictionary)
    print('checking list', context.a_list)

#C:\Users\vikram.uk\PycharmProjects\Behave>C:\Python36\Scripts\behave   feature/ScenarioTagOutline.feature  --tags=@integration
#C:\Users\vikram.uk\PycharmProjects\Behave>C:\Python36\Scripts\behave   feature/ScenarioTagOutline.feature  --tags=@develop

