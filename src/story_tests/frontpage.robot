*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To Front Page

*** Test Cases ***
Click To Selector Link
    Go To Front Page
    Click Link  Add a new reference
    Selector Page Should Be Open

*** Keywords ***
Reset Application And Go To Front Page
    Go To Front Page
    # Resetointia ei ole vielä implementoitu