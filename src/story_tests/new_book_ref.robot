*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To Add New Book Reference Page

*** Test Cases ***
Can't Submit Form When Author Empty
    Input Text  name=title  Unit Test Frameworks: Tools for High-Quality Software Development
    Input Text  name=year  2004
    Input Text  name=publisher  O'Reilly Media, inc.
    Click Button  Submit
    Add New Book Reference Page Should Be Open

Can't Submit Form When Title Empty
    Input Text  name=authors  Paul Hamill
    Input Text  name=year  2004
    Input Text  name=publisher  O'Reilly Media, inc.
    Click Button  Submit
    Add New Book Reference Page Should Be Open

Can't Submit Form When Year Empty
    Input Text  name=authors  Paul Hamill
    Input Text  name=title  Unit Test Frameworks: Tools for High-Quality Software Development
    Input Text  name=publisher  O'Reilly Media, inc.
    Click Button  Submit
    Add New Book Reference Page Should Be Open

Can't Submit Form When Publisher Empty
    Input Text  name=authors  Paul Hamill
    Input Text  name=title  Unit Test Frameworks: Tools for High-Quality Software Development
    Input Text  name=year  2004
    Click Button  Submit
    Add New Book Reference Page Should Be Open

Can Submit Form When Optional Fields Empty
    Input Text  name=authors  Paul Hamill
    Input Text  name=title  Unit Test Frameworks: Tools for High-Quality Software Development
    Input Text  name=year  2004
    Input Text  name=publisher  O'Reilly Media, inc.
    Click Button  Submit
    Front Page Should Be Open
    Go To List Of References Page
    Page Should Contain  Unit Test Frameworks: Tools for High-Quality Software Development, Paul Hamill, 2004, O'Reilly Media, inc.

Submitting Filled Out Form Redirects To Front Page
    Input Text  name=authors  Paul Hamill
    Input Text  name=title  Unit Test Frameworks: Tools for High-Quality Software Development
    Input Text  name=year  2004
    Input Text  name=publisher  O'Reilly Media, inc.
    Click Button  Submit
    Front Page Should Be Open

Clicking Go Back Redirects To Selector
    Click Link  Go back
    Selector Page Should Be Open

*** Keywords ***
Reset Application And Go To Add New Book Reference Page
    Reset Database
    Go To Add New Book Reference Page
