Feature: My test feature with the Behave BDD
    @Linux
	@slow
	Scenario: A simple test#1
    Given you are happy
    When someone says hi
    Then you smile
	
	@WINDOWS
	@wip
	Scenario: A simple test#2
    Given you are happy
    When someone says hi
    Then you smile
	
	@use.with_browser=chrome
	Scenario: A simple test#3
    Given you are happy
    When someone says hi
    Then you smile