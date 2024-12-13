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

Toggling Bibtex Doesnt Reset Filter
    Add Two Valid Filled Out Forms
    Go To List Of References Page
    List Of References Page Should Be Open
    Input And Search Query  2000
    Click Button    Toggle BibTeX format
    Click Button    Toggle BibTeX format
    Page Should Contain    Test Title, Test Authors, 2000, Test Publisher
    Page Should Not Contain    Test Title, Test Authors, 2001, Test Publisher

Clear Filter Button Clears Filters
    Add Two Valid Filled Out Forms
    Go To List Of References Page
    List Of References Page Should Be Open
    Input And Search Query  2000
    Click Button    Toggle BibTeX format
    Click Button    Toggle BibTeX format
    Page Should Contain    Test Title, Test Authors, 2000, Test Publisher
    Page Should Not Contain    Test Title, Test Authors, 2001, Test Publisher
    Click Button  Clear filters
    Page Should Contain    Test Title, Test Authors, 2000, Test Publisher
    Page Should Contain    Test Title, Test Authors, 2001, Test Publisher

Download Bib File For All References
    Add Two Valid Filled Out Forms
    Click Button    Toggle BibTeX format
    Wait Until Element Is Visible  class:bibtex-container
    Click Link  Download All References
    Wait Until File Exists  ~/Downloads/allreferences.bib
    File Should Exist  ~/Downloads/allreferences.bib

Copy All Filtered References Works
    Add Two Valid Filled Out Forms
    Submit Valid Filled Out Form    Test Authors    Test Title    1999    Test Publisher  Test Editor
    Input And Search Query  200
    Click Button    Toggle BibTeX format
    Wait Until Element Is Visible  id=copy_all_button
    Click Button  Copy All References
    Go To Add New Book Reference Page
    Add New Book Reference Page Should Be Open
    Paste Copied Text And Compare

*** Keywords ***
Paste Copied Text And Compare
    Press Keys  name=authors  \CTRL+v
    ${value}=  Get Value  name=authors
    Should Contain  ${value}      @book{Test-Title-2000,\n author = {Test Authors},\n editor = {Test Editor},\n publisher = {Test Publisher},\n title = {Test Title},\n year = {2000}\n}\n
    Should Contain  ${value}      @book{Test-Title-2001,\n author = {Test Authors},\n editor = {Test Editor},\n publisher = {Test Publisher},\n title = {Test Title},\n year = {2001}\n}\n
    Should Not Contain  ${value}      @book{Test-Title-1999,\n author = {Test Authors},\n editor = {Test Editor},\n publisher = {Test Publisher},\n title = {Test Title},\n year = {1999}\n}\n

Input And Search Query
    [Arguments]  ${query}
    Input Text  query  ${query}
    Click Button    Search
Add Two Valid Filled Out Forms
    Submit Valid Filled Out Form    Test Authors    Test Title    2000    Test Publisher  Test Editor
    Submit Valid Filled Out Form    Test Authors    Test Title    2001    Test Publisher  Test Editor

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

Wait Until File Exists
    [Arguments]    ${path}    ${timeout}=10
    Wait Until Keyword Succeeds    ${timeout}    1s
    ...    File Should Exist    ${path}