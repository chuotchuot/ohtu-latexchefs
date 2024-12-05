*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To List Of References Page
Library    XML

*** Test Cases ***
Empty Reference List Is Declared
    Page Should Contain  No references found

Edit Book Reference Add New Author And Submit Form
    Add New Book Reference
    Click Link  View list of references
    Page Should Contain    Test Title, Test Authors, 2000, Test Publisher, Test Editor
    Click Button  Edit
    Input Text  name=authors  New Author
    Click Button  Confirm Changes
    List Of References Page Should Be Open
    Page Should Contain    Test Title, New Author, 2000, Test Publisher, Test Editor

Edit Book Reference Year And Submit Form
    Add New Book Reference
    Click Link  View list of references
    Page Should Contain    Test Title, Test Authors, 2000, Test Publisher, Test Editor
    Click Button  Edit
    Input Text  name=year  2005
    Click Button  Confirm Changes
    List Of References Page Should Be Open
    Page Should Contain    Test Title, Test Authors, 2005, Test Publisher, Test Editor

Edit Book Reference Add New Title And Submit Form
    Add New Book Reference
    Click Link  View list of references
    Page Should Contain    Test Title, Test Authors, 2000, Test Publisher, Test Editor
    Click Button  Edit
    Clear Element Text  name=title
    Input Text  name=title  New Title
    Click Button  Confirm Changes
    List Of References Page Should Be Open
    Page Should Contain    New Title, Test Authors, 2000, Test Publisher, Test Editor

Edit Misc Reference And Submit Form
    Add New Misc Reference
    Click Link  View list of references
    Page Should Contain   Test Title, Test Authors, Test Published
    Click Button    Edit
    Input Text    name=title    New Title
    Input Text    name=howpublished    New Publishing Way
    Input Text    name=year    2000
    Click Button  Confirm Changes
    List Of References Page Should Be Open
    Page Should Contain    New Title, Test Authors, 2000, New Publishing Way

Edit Inbook Reference And Submit Form
    Add New Inbook Reference
    Click Link  View list of references
    Page Should Contain  Test Title, Test Authors, 2000, Test Publisher, Test Book Title
    Click Button  Edit
    Input Text  name=title  New Title
    Click Button  Confirm Changes
    List Of References Page Should Be Open
    Page Should Contain  New Title, Test Authors, 2000, Test Publisher, Test Book Title

Discard Changes
    Add New Book Reference
    Click Link  View list of references
    Page Should Contain    Test Title, Test Authors, 2000, Test Publisher, Test Editor
    Click Button  Edit
    Input Text  name=publisher  Wrong Publisher
    Click Link  Discard Changes
    List Of References Page Should Be Open
    Page Should Contain    Test Title, Test Authors, 2000, Test Publisher, Test Editor

Can't Submit Form When Title Empty
    Add New Book Reference
    Click Link  View list of references
    Click Button  Edit
    Clear Element Text  name=title
    Click Button  Confirm Changes
    Edit Reference Page Should Be Open

*** Keywords ***
Reset Application And Go To List of References Page
    Reset Database
    Go To List Of References Page

Add New Book Reference
    Go To Add New Book Reference Page
    Input Text  name=authors  Test Authors
    Input Text  name=title  Test Title
    Input Text  name=year  2000
    Input Text  name=publisher  Test Publisher
    Input Text  name=editors  Test Editor
    Input Text  name=reference_key  TestRefKey12-_
    Input text  name=keywords  Test Keywords
    Click Button    Submit
    Front Page Should Be Open

Add New Misc Reference
    Go To Add New Misc Reference Page
    Input Text  name=authors  Test Authors
    Input Text  name=title  Test Title
    Input Text    name=howpublished    Test Published
    Input Text  name=reference_key  TestRefKey12-_
    Click Button    Submit
    Front Page Should Be Open

Add New Inbook Reference
    Go To Add New Inbook Reference Page
    Input Text  name=authors  Test Authors
    Input Text  name=title  Test Title
    Input Text  name=booktitle  Test Book Title
    Input Text  name=year  2000
    Input Text  name=publisher  Test Publisher
    Input Text  name=reference_key  TestRefKey12-_
    Click Button  Submit
    Front Page Should Be Open