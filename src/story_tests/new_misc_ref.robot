*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To Add New Misc Reference Page

*** Test Cases ***
Can't Submit Form When Authors Empty
    Input Text  name=title  Test Title
    Input Text  name=howpublished  Test Way Of Publishing
    Input Text  name=month  12
    Input Text  name=year  2000
    Input Text  name=note  Test Note
    Input text  name=keywords  Test Keywords
    Click Button  Submit
    Add New Misc Reference Page Should Be Open

Can't Submit Form When Title Empty
    Input Text  name=authors  Test Authors
    Input Text  name=howpublished  Test Way Of Publishing
    Input Text  name=month  12
    Input Text  name=year  2000
    Input Text  name=note  Test Note
    Input text  name=keywords  Test Keywords
    Click Button  Submit
    Add New Misc Reference Page Should Be Open

Can't Submit Form When How Published Empty
    Input Text  name=authors  Test Authors
    Input Text  name=title  Test Title
    Input Text  name=month  12
    Input Text  name=year  2000
    Input Text  name=note  Test Note
    Input text  name=keywords  Test Keywords
    Click Button  Submit
    Add New Misc Reference Page Should Be Open

Submits Correctly Filled Out Form And Redirects To Front Page
    Input Text  name=authors  Test Authors
    Input Text  name=title  Test Title
    Input Text  name=howpublished  Test Way Of Publishing
    Click Button  Submit
    Front Page Should Be Open

Clicking Go Back Redirects To Selector
    Click Link  Go back
    Selector Page Should Be Open

*** Keywords ***
Reset Application And Go To Add New Misc Reference Page
    Reset Database
    Go To Add New Misc Reference Page
