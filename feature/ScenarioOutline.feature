Feature: Testing objects
    Scenario Outline: Given the inputs below
        Given a <Dictionary> and <List>
        When we insert them
        Then we confirm the result in the database
#https://stackoverflow.com/questions/52635025/how-can-i-pass-an-object-like-a-list-or-dictionary-in-python-behave-feature-fil
Examples: Input Variables
|Dictionary                |List         |
|{"name": "Fred", "age":2} |[1,2,"three"]|
|{"name": "Test", "age":2} |[1,2,"For"]|