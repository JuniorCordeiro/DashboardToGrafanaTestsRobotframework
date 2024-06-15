*** Settings ***
# Test Teardown    Teardown Keyword
#Resource         Shared.robot



*** Test Cases ***
Example 2 Passing Test
    [TAGS]    Test 02   
	# Register End Test Listener		Listener Keyword
	Log  This is an another example of a test that passed

Example 2 Failing Test
    [TAGS]    Test 02 
    Sleep    2
	# Register End Test Listener		Listener Keyword
	Fail  This is an another example of a test that failed