*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To Add New Book Reference Page

*** Test Cases ***
Can't Submit Form When Author Empty
    Input Text  name=title  Test Title
    Input Text  name=year  2000
    Input Text  name=publisher  Test Publisher
    Input Text  name=reference_key  TestRefKey12-_
    Input text  name=keywords  Test Keywords
    Click Button  Submit
    Add New Book Reference Page Should Be Open

Can't Submit Form When Title Empty
    Input Text  name=authors  Test Authors
    Input Text  name=year  2000
    Input Text  name=publisher  Test Publisher
    Input Text  name=reference_key  TestRefKey12-_
    Input text  name=keywords  Test Keywords
    Click Button  Submit
    Add New Book Reference Page Should Be Open

Can't Submit Form When Year Empty
    Input Text  name=authors  Test Authors
    Input Text  name=title  Test Title
    Input Text  name=publisher  Test Publisher
    Input Text  name=reference_key  TestRefKey12-_
    Input text  name=keywords  Test Keywords
    Click Button  Submit
    Add New Book Reference Page Should Be Open

Can't Submit Form When Publisher Empty
    Input Text  name=authors  Test Authors
    Input Text  name=title  Test Title
    Input Text  name=year  2000
    Input Text  name=reference_key  TestRefKey12-_
    Input text  name=keywords  Test Keywords
    Click Button  Submit
    Add New Book Reference Page Should Be Open

Can't Submit Form When Reference Key Empty
    Input Text  name=authors  Test Authors
    Input Text  name=title  Test Title
    Input Text  name=year  2000
    Input Text  name=publisher  Test Publisher
    Input text  name=keywords  Test Keywords
    Click Button  Submit
    Add New Book Reference Page Should Be Open

Submitting Fully Filled Out Form Redirects To Front Page
    Input Text  name=authors  Test Authors
    Input Text  name=title  Test Title
    Input Text  name=year  2000
    Input Text  name=publisher  Test Publisher
    Input Text  name=reference_key  TestRefKey12-_
    Input text  name=keywords  Test Keywords
    Click Button  Submit
    Front Page Should Be Open

Submitting Filled Out Form Without Keywords Redirects To Front Page
    Input Text  name=authors  Test Authors
    Input Text  name=title  Test Title
    Input Text  name=year  2000
    Input Text  name=publisher  Test Publisher
    Input Text  name=reference_key  TestRefKey12-_
    Click Button  Submit
    Front Page Should Be Open

Clicking Go To Front Page Redirects To Front Page
    Click Link  Go to front page
    Front Page Should Be Open

*** Keywords ***
Reset Application And Go To Add New Book Reference Page
    Reset Database
    Go To Add New Book Reference Page