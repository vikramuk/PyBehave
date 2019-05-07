Feature: parametrized

Scenario: Parametrized given, when, thens
    Given there are <start> cucumbers
    When I eat <eat> cucumbers
    Then I should have <left> cucumbers
|start|eat|left|
|   5 |2  |   3 |
