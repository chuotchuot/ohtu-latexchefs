*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To List Of References Page

*** Test Cases ***

Empty Reference List Is Declared
    Page Should Contain    No references found

Single Reference Is Displayed
    Submit Valid Filled Out Form    Test Authors    Test Title    2000    Test Publisher  Test Editor  Test-Ref-Key-1
    Go To List Of References Page
    Page Should Contain    Test Title, Test Authors, 2000, Test Publisher
Multiple References Are Displayed
    Submit Valid Filled Out Form    Test Authors    Test Title    2000    Test Publisher  Test Editor  Test-Ref-Key-1
    Submit Valid Filled Out Form    Other Authors    Other Title    1990    Other Publisher  Other Editor  Test-Ref-Key-2
    Page Should Contain    Test Title, Test Authors, 2000, Test Publisher, Test Editor
    Page Should Contain    Other Title, Other Authors, 1990, Other Publisher, Other Editor

Single Reference Is Viewable In BibTeX
    Submit Valid Filled Out Form    Test Authors    Test Title    2000    Test Publisher  Test Editor  Test-Ref-Key-1
    Toggle BibTeX format
    Wait Until Element Is Visible  class:bibtex-container
    Page Should Contain    @book{Test-Ref-Key-1,\n author = {Test Authors},\n editor = {Test Editor},\n publisher = {Test Publisher},\n title = {Test Title},\n year = {2000}\n}

Multiple References Are Viewable In BibTeX
    Submit Valid Filled Out Form    Test Authors    Test Title    2000    Test Publisher  Test Editor  Test-Ref-Key-1
    Submit Valid Filled Out Form    Other Authors    Other Title    1990    Other Publisher  Other Editor  Test-Ref-Key-2
    Toggle BibTeX format
    Page Should Contain    @book{Test-Ref-Key-1,\n author = {Test Authors},\n editor = {Test Editor},\n publisher = {Test Publisher},\n title = {Test Title},\n year = {2000}\n}
    Page Should Contain    @book{Test-Ref-Key-2,\n author = {Other Authors},\n editor = {Other Editor},\n publisher = {Other Publisher},\n title = {Other Title},\n year = {1990}\n}

Clicking Go to front page Goes To Front Page
    Click Link  Go to front page
    Front Page Should Be Open
    
*** Keywords ***

Reset Application And Go To List Of References Page
    Reset Database
    Go To List Of References Page

Submit Valid Filled Out Form 
    [Arguments]  ${authors}  ${title}  ${year}  ${publisher}  ${editor}  ${reference_key}
    Go To Add New Book Reference Page
    Input Text  name=authors  ${authors}
    Input Text  name=title  ${title}
    Input Text  name=year  ${year}
    Input Text  name=publisher  ${publisher}
    Input Text  name=editor  ${editor}
    Input Text  name=reference_key  ${reference_key}
    Click Button  Submit
    Go To List Of References Page

Toggle BibTeX format
    Click Button    Toggle BibTeX format