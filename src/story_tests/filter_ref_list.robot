*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To List Of References Page

*** Test Cases ***
One Reference With Searched Word Is Displayed
    Add Two Valid Filled Out Forms
    Go To List Of References Page
    List Of References Page Should Be Open
    Input Text    query    2000
    Click Button    Search
    Page Should Contain  Unit Test Frameworks: Tools for High-Quality Software Development, Paul Hamill, 2000, O'Reilly Media, inc.

No References With Searched Word Is Displayed
    Add Two Valid Filled Out Forms
    Go To List Of References Page
    List Of References Page Should Be Open
    Input Text    query    2010
    Click Button    Search
    Page Should Contain  No references found

Toggling Bibtex Doesnt Reset Filter
    Add Two Valid Filled Out Forms
    Go To List Of References Page
    List Of References Page Should Be Open
    Input And Search Query  2004
    Click Button    Toggle BibTeX format
    Click Button    Toggle BibTeX format
    Page Should Contain    Unit Test Frameworks: Tools for High-Quality Software Development, Paul Hamill, 2004, O'Reilly Media, inc.
    Page Should Not Contain    Unit Test Frameworks: Tools for High-Quality Software Development, Paul Hamill, 2000, O'Reilly Media, inc.

Clear Filter Button Clears Filters
    Add Two Valid Filled Out Forms
    Go To List Of References Page
    List Of References Page Should Be Open
    Input And Search Query  2004
    Click Button    Toggle BibTeX format
    Click Button    Toggle BibTeX format
    Page Should Contain    Unit Test Frameworks: Tools for High-Quality Software Development, Paul Hamill, 2004, O'Reilly Media, inc.
    Page Should Not Contain    Unit Test Frameworks: Tools for High-Quality Software Development, Paul Hamill, 2000, O'Reilly Media, inc.
    Click Button  Clear filters
    Page Should Contain    Unit Test Frameworks: Tools for High-Quality Software Development, Paul Hamill, 2004, O'Reilly Media, inc.
    Page Should Contain    Unit Test Frameworks: Tools for High-Quality Software Development, Paul Hamill, 2000, O'Reilly Media, inc.

Download Bib File For All References
    Add Two Valid Filled Out Forms
    Click Button    Toggle BibTeX format
    Wait Until Element Is Visible  class:bibtex-container
    Click Link  Download All References
    Wait Until File Exists  ~/Downloads/allreferences.bib
    File Should Exist  ~/Downloads/allreferences.bib

Copy All Filtered References Works
    Add Two Valid Filled Out Forms
    Submit Valid Filled Out Form    Paul Hamill    Unit Test Frameworks: Tools for High-Quality Software Development    1999    O'Reilly Media, inc.
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
    Should Contain  ${value}      @book{Unit-Test-Frameworks:-2004,\n author = {Paul Hamill},\n publisher = {O'Reilly Media, inc.},\n title = {Unit Test Frameworks: Tools for High-Quality Software Development},\n year = {2004}\n}\n
    Should Contain  ${value}      @book{Unit-Test-Frameworks:-2000,\n author = {Paul Hamill},\n publisher = {O'Reilly Media, inc.},\n title = {Unit Test Frameworks: Tools for High-Quality Software Development},\n year = {2000}\n}\n
    Should Not Contain  ${value}      @book{Unit-Test-Frameworks:-1999,\n author = {Paul Hamill},\n publisher = {O'Reilly Media, inc.},\n title = {Unit Test Frameworks: Tools for High-Quality Software Development},\n year = {1999}\n}\n

Input And Search Query
    [Arguments]  ${query}
    Input Text  query  ${query}
    Click Button    Search

Add Two Valid Filled Out Forms
    Submit Valid Filled Out Form    Paul Hamill    Unit Test Frameworks: Tools for High-Quality Software Development    2004    O'Reilly Media, inc.
    Submit Valid Filled Out Form    Paul Hamill    Unit Test Frameworks: Tools for High-Quality Software Development    2000    O'Reilly Media, inc.

Reset Application And Go To List Of References Page
    Reset Database
    Go To List Of References Page

Submit Valid Filled Out Form
    [Arguments]  ${authors}  ${title}  ${year}  ${publisher}
    Go To Add New Book Reference Page
    Input Text  name=authors  ${authors}
    Input Text  name=title  ${title}
    Input Text  name=year  ${year}
    Input Text  name=publisher  ${publisher}
    Click Button  Submit
    Go To List Of References Page

Wait Until File Exists
    [Arguments]    ${path}    ${timeout}=10
    Wait Until Keyword Succeeds    ${timeout}    1s
    ...    File Should Exist    ${path}