*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To List Of References Page

*** Test Cases ***

Empty Reference List Is Declared
    Page Should Contain    No references found

Single Reference Is Displayed
    Submit Valid Filled Out Form    Test Authors    Test Title    2000    Test Publisher  Test-Ref-Key-1
    Go To List Of References Page
    Page Should Contain    Test Title, Test Authors, 2000, Test Publisher
Multiple References Are Displayed
    Submit Valid Filled Out Form    Test Authors    Test Title    2000    Test Publisher  Test-Ref-Key-1
    Submit Valid Filled Out Form    Other Authors    Other Title    1990    Other Publisher  Test-Ref-Key-2
    Page Should Contain    Test Title, Test Authors, 2000, Test Publisher
    Page Should Contain    Other Title, Other Authors, 1990, Other Publisher

Clicking Go to front page Goes To Front Page
    Click Link  Go to front page
    Front Page Should Be Open
*** Keywords ***

Reset Application And Go To List Of References Page
    Reset Database
    Go To List Of References Page

Submit Valid Filled Out Form 
    [Arguments]  ${authors}  ${title}  ${year}  ${publisher}  ${reference_key}
    Go To Add New Book Reference Page
    Input Text  name=authors  ${authors}
    Input Text  name=title  ${title}
    Input Text  name=year  ${year}
    Input Text  name=publisher  ${publisher}
    Input Text  name=reference_key  ${reference_key}
    Click Button  Submit
    Go To List Of References Page
    