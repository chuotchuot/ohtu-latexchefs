*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To List Of References Page

*** Test Cases ***
One Reference With Searched Word Is Displayed
    Submit Valid Filled Out Form    Test Authors    Test Title    2000    Test Publisher  Test Editor
    Submit Valid Filled Out Form    Test Authors    Test Title    2001    Test Publisher  Test Editor
    Go To List Of References Page
    List Of References Page Should Be Open
    Input Text    query    2000
    Click Button    Search
    Page Should Contain    Test Title, Test Authors, 2000, Test Publisher

No References With Searched Word Is Displayed
    Submit Valid Filled Out Form    Test Authors    Test Title    2000    Test Publisher  Test Editor
    Submit Valid Filled Out Form    Test Authors    Test Title    2001    Test Publisher  Test Editor
    Go To List Of References Page
    List Of References Page Should Be Open
    Input Text    query    2010
    Click Button    Search
    Page Should Contain  No references found

*** Keywords ***
Reset Application And Go To List Of References Page
    Reset Database
    Go To List Of References Page

Submit Valid Filled Out Form
    [Arguments]  ${authors}  ${title}  ${year}  ${publisher}  ${editor}
    Go To Add New Book Reference Page
    Input Text  name=authors  ${authors}
    Input Text  name=title  ${title}
    Input Text  name=year  ${year}
    Input Text  name=publisher  ${publisher}
    Input Text  name=editors  ${editor}
    Click Button  Submit
    Go To List Of References Page