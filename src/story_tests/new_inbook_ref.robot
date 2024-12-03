*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To Add New Inbook Reference Page

*** Test Cases ***
Submitting Valid Form Redirects To Front Page
    Input Text  name=authors  Test Authors
    Input Text  name=title  Test Title
    Input Text  name=booktitle  Test BookTitle
    Input Text  name=year  2000
    Input Text  name=publisher  Test Publisher
    Input Text  name=reference_key  TestRefKey12-_
    Click Button  Submit
    Front Page Should Be Open


Clicking Go To Front Page Redirects To Front Page
    Click Link  Go to front page
    Front Page Should Be Open

*** Keywords ***
Reset Application And Go To Add New Inbook Reference Page
    Reset Database
    Go To Add New Inbook Reference Page