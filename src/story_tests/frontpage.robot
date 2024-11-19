*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To Front Page

*** Test Cases ***
Click To Add A New Reference Link
    Click Link  Add a new reference
    Selector Page Should Be Open

Click View List Of References Link
    Click Link  View list of references
    List Of References Page Should Be Open

*** Keywords ***
Reset Application And Go To Front Page
    Reset Database
    Go To Front Page