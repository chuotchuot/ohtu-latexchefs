*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To List Of References Page

*** Test Cases ***
Empty Reference List Is Declared
    Page Should Contain  No references found

Edit Add New Author
    Add New Reference
    Click Link  View list of references
    Click Button  Edit
    Input Text  name=authors  New Author
    Click Button  Confirm Changes
    Edit Should Succeed

Edit Year
    Add New Reference
    Click Link  View list of references
    Click Button  Edit
    Input Text  name=year  2005
    Click Button  Confirm Changes
    Edit Should Succeed

Edit New Title
    Add New Reference
    Click Link  View list of references
    Click Button  Edit
    Clear Element Text  name=title
    Input Text  name=title  NewTitle
    Click Button  Confirm Changes
    Edit Should Succeed

Discard Changes
    Add New Reference
    Click Link  View list of references
    Click Button  Edit
    Input Text  name=publisher  Wrong Publisher
    Click Link  Discard Changes
    List Of References Page Should Be Open

*** Keywords ***
Reset Application And Go To List of References Page
    Reset Database
    Go To List Of References Page

Edit Should Succeed
    List Of References Page Should Be Open

Add New Reference
    Go To Add New Book Reference Page
    Input Text  name=authors  Test Authors
    Input Text  name=title  Test Title
    Input Text  name=year  2000
    Input Text  name=publisher  Test Publisher
    Input Text  name=reference_key  TestRefKey12-_
    Input text  name=keywords  Test Keywords
    Click Button    Submit
    Front Page Should Be Open