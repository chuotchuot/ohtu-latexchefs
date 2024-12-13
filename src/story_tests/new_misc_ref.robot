*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To Add New Misc Reference Page

*** Test Cases ***
Can't Submit Form When Authors Empty
    Input Text  name=title  Lean Testing: Or Why Unit Tests Are Worse Than You Think
    Input Text  name=howpublished  WebPage Medium.com
    Input Text  name=year  2018
    Input Text    name=keywords    lean
    Click Button  Submit
    Add New Misc Reference Page Should Be Open

Can't Submit Form When Title Empty
    Input Text  name=authors  Eugen Kiss
    Input Text  name=howpublished  WebPage Medium.com
    Input Text  name=year  2018
    Input Text    name=keywords    lean
    Click Button  Submit
    Add New Misc Reference Page Should Be Open

Can't Submit Form When HowPublished Empty
    Input Text  name=authors  Eugen Kiss
    Input Text  name=year  2018
    Input Text    name=keywords    lean
    Click Button  Submit
    Add New Misc Reference Page Should Be Open

Submits Correctly Filled Out Form And Redirects To Front Page
    Input Text  name=authors  Eugen Kiss
    Input Text  name=title  Lean Testing: Or Why Unit Tests Are Worse Than You Think
    Input Text  name=howpublished  WebPage Medium.com
    Input Text  name=year  2018
    Input Text    name=keywords    lean
    Click Button  Submit
    Front Page Should Be Open

Clicking Go Back Redirects To Selector
    Click Link  Go back
    Selector Page Should Be Open

*** Keywords ***
Reset Application And Go To Add New Misc Reference Page
    Reset Database
    Go To Add New Misc Reference Page
