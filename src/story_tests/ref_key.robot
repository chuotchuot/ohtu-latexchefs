*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To Add New Book Reference Page

*** Test Cases ***
Reference Key Is Generated Correctly
    Input Text  name=authors  Paul Hamill
    Input Text  name=title  Unit Test Frameworks
    Input Text  name=year  2004
    Input Text  name=publisher  O'Reilly Media, Inc.
    Click Button  Submit
    Front Page Should Be Open
    Go To List Of References Page
    Toggle BibTeX Format
    Page Should Contain  Unit-Test-Frameworks-2004

A Duplicate Reference Key Is Corrected
    Input Text  name=authors  Paul Hamill
    Input Text  name=title  Unit Test Frameworks
    Input Text  name=year  2004
    Input Text  name=publisher  O'Reilly Media, Inc.
    Click Button  Submit
    Front Page Should Be Open

    Go To Add New Book Reference Page
    Input Text  name=authors  Hamill Paul
    Input Text  name=title  Unit Test Frameworks
    Input Text  name=year  2004
    Input Text  name=publisher  Media O'Reilly
    Click Button  Submit
    Front Page Should Be Open

    Go To List Of References Page
    Toggle BibTeX Format
    Page Should Contain  Unit-Test-Frameworks-2004
    Page Should Contain  Unit-Test-Frameworks-2004-HamillPaul

*** Keywords ***
Reset Application And Go To Add New Book Reference Page
    Reset Database
    Go To Add New Book Reference Page