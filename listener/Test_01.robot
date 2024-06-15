*** Settings ***
# Test Teardown    Teardown Keyword
# Resource         Shared.robot


*** Test Cases ***
Example 1 Passing Test
    [TAGS]    Test 01     
	# Register End Test Listener		Listener Keyword
	Log  This is an example of a test that passed

Example 1 Failing Test
    [TAGS]    Test 01   
    Sleep    2
	# Register End Test Listener		Listener Keyword
	Fail  This is an example of a test that failed