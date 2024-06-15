*** Settings ***
# Test Teardown    Teardown Keyword
#Resource         Shared.robot

*** Test Cases ***
Example 3 Passing Test
    [TAGS]    Test 03 
	# Register End Test Listener		Listener Keyword
	Log  This is an example of a test that passed

Example 3 Failing Test
    [TAGS]    Test 03 
    Sleep    2
	# Register End Test Listener		Listener Keyword
	# Fail  This is an example of a test that failed
	No Operation
	