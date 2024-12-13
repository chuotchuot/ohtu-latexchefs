*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To List Of References Page

*** Test Cases ***

Empty Reference List Is Declared
    Page Should Contain    No references found

Single Reference Is Displayed
    Submit Valid Filled Out Form    Paul Hamill    Unit Test Frameworks: Tools for High-Quality Software Development    2004    O'Reilly Media, inc.
    Go To List Of References Page
    Page Should Contain    Unit Test Frameworks: Tools for High-Quality Software Development, Paul Hamill, 2004, O'Reilly Media, inc.
Multiple References Are Displayed
    Submit Valid Filled Out Form    Paul Hamill    Unit Test Frameworks: Tools for High-Quality Software Development    2004    O'Reilly Media, inc.
    Submit Valid Filled Out Form    Paul Hamill    Unit Test Frameworks: Tools for High-Quality Software Development    2003    O'Reilly Media, inc.
    Page Should Contain    Unit Test Frameworks: Tools for High-Quality Software Development, Paul Hamill, 2004, O'Reilly Media, inc.
    Page Should Contain    Unit Test Frameworks: Tools for High-Quality Software Development, Paul Hamill, 2003, O'Reilly Media, inc.

Single Reference Is Viewable In BibTeX
    Submit Valid Filled Out Form    Paul Hamill    Unit Test Frameworks: Tools for High-Quality Software Development    2004    O'Reilly Media, inc.
    Toggle BibTeX Format
    Wait Until Element Is Visible  class:bibtex-container
    Page Should Contain    @book{Unit-Test-Frameworks:-2004,\n author = {Paul Hamill},\n publisher = {O'Reilly Media, inc.},\n title = {Unit Test Frameworks: Tools for High-Quality Software Development},\n year = {2004}\n}\n

Multiple References Are Viewable In BibTeX
    Submit Valid Filled Out Form    Paul Hamill    Unit Test Frameworks: Tools for High-Quality Software Development    2004    O'Reilly Media, inc.
    Submit Valid Filled Out Form    Paul Hamill    Unit Test Frameworks: Tools for High-Quality Software Development    2003    O'Reilly Media, inc.
    Toggle BibTeX Format
    Wait Until Element Is Visible  class:bibtex-container
    References Are Viewable In BibTeX
    

Clicking Go to front page Goes To Front Page
    Click Link  Go to front page
    Front Page Should Be Open
    
Copying BibTeX Properly Copies BibTeX
    Submit Valid Filled Out Form    Paul Hamill    Unit Test Frameworks: Tools for High-Quality Software Development    2004    O'Reilly Media, inc.
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
    Should Be Equal  ${value}  @book{Unit-Test-Frameworks:-2004,\n author = {Paul Hamill},\n publisher = {O'Reilly Media, inc.},\n title = {Unit Test Frameworks: Tools for High-Quality Software Development},\n year = {2004}\n}\n
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

Toggle BibTeX Format
    Click Button    Toggle BibTeX format


References Are Viewable In BibTeX
    Page Should Contain    @book{Unit-Test-Frameworks:-2004,\n author = {Paul Hamill},\n publisher = {O'Reilly Media, inc.},\n title = {Unit Test Frameworks: Tools for High-Quality Software Development},\n year = {2004}\n}\n
    Page Should Contain    @book{Unit-Test-Frameworks:-2003,\n author = {Paul Hamill},\n publisher = {O'Reilly Media, inc.},\n title = {Unit Test Frameworks: Tools for High-Quality Software Development},\n year = {2003}\n}\n