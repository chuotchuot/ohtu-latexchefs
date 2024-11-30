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
    Click Button    Delete
    Delete Reference Page Should Be Open
    Click Button    Delete
    List Of References Page Should Be Open
    Page Should Contain  No references found

Delete Reference And Cancel
    Add New Reference
    Click Link  View list of references
    Wait Until Element Is Visible  class:button  10s
    Click Button    Delete
    Delete Reference Page Should Be Open
    Click Link    Cancel
    List Of References Page Should Be Open

*** Keywords ***
Reset Application And Go To List of References Page
    Reset Database
    Go To List Of References Page

Add New Reference
    Go To Add New Book Reference Page
    Input Text  name=authors  Test Authors
    Input Text  name=title  Test Title
    Input Text  name=year  2000
    Input Text  name=publisher  Test Publisher
    Input Text  name=editor  Test Editor
    Input Text  name=reference_key  TestRefKey12-_
    Input text  name=keywords  Test Keywords
    Click Button    Submit
    Front Page Should Be Open