*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To List Of References Page

*** Test Cases ***

Empty Reference List Is Declared
    Page Should Contain    No references found

Single Reference Is Displayed
    Submit Valid Filled Out Form    Test Authors    Test Title    2000    Test Publisher  Test Editor
    Go To List Of References Page
    Page Should Contain    Test Title, Test Authors, 2000, Test Publisher
Multiple References Are Displayed
    Submit Valid Filled Out Form    Test Authors    Test Title    2000    Test Publisher  Test Editor
    Submit Valid Filled Out Form    Other Authors    Other Title    1990    Other Publisher  Other Editor
    Page Should Contain    Test Title, Test Authors, 2000, Test Publisher, Test Editor
    Page Should Contain    Other Title, Other Authors, 1990, Other Publisher, Other Editor

Single Reference Is Viewable In BibTeX
    Submit Valid Filled Out Form    Test Authors    Test Title    2000    Test Publisher  Test Editor
    Toggle BibTeX Format
    Wait Until Element Is Visible  class:bibtex-container
    Page Should Contain    @book{TestTitle-2000,\n author = {Test Authors},\n editor = {Test Editor},\n publisher = {Test Publisher},\n title = {Test Title},\n year = {2000}\n}

Multiple References Are Viewable In BibTeX
    Submit Valid Filled Out Form    Test Authors    Test Title    2000    Test Publisher  Test Editor
    Submit Valid Filled Out Form    Other Authors    Other Title    1990    Other Publisher  Other Editor
    Toggle BibTeX Format
    Wait Until Element Is Visible  class:bibtex-container
    References Are Viewable In BibTeX
    

Clicking Go to front page Goes To Front Page
    Click Link  Go to front page
    Front Page Should Be Open
    
Copying BibTeX Properly Copies BibTeX
    Submit Valid Filled Out Form    Test Authors    Test Title    2000    Test Publisher  Test Editor
    Toggle BibTeX Format
    Copy BibTeX
    Go To Add New Book Reference Page
    Add New Book Reference Page Should Be Open
    Paste Copied Text And Compare

*** Keywords ***
Copy BibTeX
    Wait Until Element Is Visible  id=copy_button
    Click Button  id=copy_button

Paste Copied Text And Compare
    Press Keys  name=authors  \CTRL+v
    ${value}=  Get Value  name=authors
    Should Be Equal  ${value}  @book{TestTitle-2000,\n author = {Test Authors},\n editor = {Test Editor},\n publisher = {Test Publisher},\n title = {Test Title},\n year = {2000}\n}\n

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

Toggle BibTeX Format
    Click Button    Toggle BibTeX format


References Are Viewable In BibTeX
    Page Should Contain    @book{TestTitle-2000,\n author = {Test Authors},\n editor = {Test Editor},\n publisher = {Test Publisher},\n title = {Test Title},\n year = {2000}\n}
    Page Should Contain    @book{OtherTitle-1990,\n author = {Other Authors},\n editor = {Other Editor},\n publisher = {Other Publisher},\n title = {Other Title},\n year = {1990}\n}