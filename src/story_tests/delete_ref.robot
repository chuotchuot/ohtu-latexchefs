*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To List Of References Page

*** Test Cases ***
Empty Reference List Is Declared
    Page Should Contain  No references found

Delete Reference
    Add New Reference
    Click Link  View list of references
    Page Should Contain  Unit Test Frameworks: Tools for High-Quality Software Development, Paul Hamill, 2004, O'Reilly Media, inc.
    Click Button    Delete
    Delete Reference Page Should Be Open
    Click Button    Delete
    List Of References Page Should Be Open
    Page Should Contain  No references found

Delete Reference And Cancel
    Add New Reference
    Click Link  View list of references
    Page Should Contain  Unit Test Frameworks: Tools for High-Quality Software Development, Paul Hamill, 2004, O'Reilly Media, inc.
    Click Button    Delete
    Delete Reference Page Should Be Open
    Wait Until Element Is Visible  class:button  10s
    Click Link    Cancel
    List Of References Page Should Be Open
    Page Should Contain  Unit Test Frameworks: Tools for High-Quality Software Development, Paul Hamill, 2004, O'Reilly Media, inc.

*** Keywords ***
Reset Application And Go To List of References Page
    Reset Database
    Go To List Of References Page

Add New Reference
    Go To Add New Book Reference Page
    Input Text  name=authors  Paul Hamill
    Input Text  name=title  Unit Test Frameworks: Tools for High-Quality Software Development
    Input Text  name=year  2004
    Input Text  name=publisher  O'Reilly Media, inc.
    Click Button    Submit
    Front Page Should Be Open