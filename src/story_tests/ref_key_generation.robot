*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To List Of References Page

*** Test Cases ***

Key Is Generated Correctly For A Single Reference
    Submit Valid Filled Out Form    Paul Hamill    Unit Test Frameworks: Tools for High-Quality Software Development    2004    O'Reilly Media, Inc.  Test Editor
    Toggle BibTeX Format
    Wait Until Element Is Visible  class:bibtex-container
    Page Should Contain    @book{Unit-Test-Frameworks:-2004,\n author = {Paul Hamill},\n editor = {Test Editor},\n publisher = {O'Reilly Media, Inc.},\n title = {Unit Test Frameworks: Tools for High-Quality Software Development},\n year = {2004}\n}

Keys Are Generated Correctly For Identical References
    Submit Valid Filled Out Form    Paul Hamill    Unit Test Frameworks: Tools for High-Quality Software Development    2004    O'Reilly Media, Inc.  Test Editor
    Submit Valid Filled Out Form    Paul Hamill    Unit Test Frameworks: Tools for High-Quality Software Development    2004    O'Reilly Media, Inc.  Test Editor
    Submit Valid Filled Out Form    Paul Hamill    Unit Test Frameworks: Tools for High-Quality Software Development    2004    O'Reilly Media, Inc.  Test Editor
    Toggle BibTeX Format
    Wait Until Element Is Visible  class:bibtex-container
    Page Should Contain    @book{Unit-Test-Frameworks:-2004,\n author = {Paul Hamill},\n editor = {Test Editor},\n publisher = {O'Reilly Media, Inc.},\n title = {Unit Test Frameworks: Tools for High-Quality Software Development},\n year = {2004}\n}
    Page Should Contain    @book{Unit-Test-Frameworks:-2004-PaulHamill,\n author = {Paul Hamill},\n editor = {Test Editor},\n publisher = {O'Reilly Media, Inc.},\n title = {Unit Test Frameworks: Tools for High-Quality Software Development},\n year = {2004}\n}
    Page Should Contain    @book{Unit-Test-Frameworks:-2004-PaulHamill-OReillyMediaInc,\n author = {Paul Hamill},\n editor = {Test Editor},\n publisher = {O'Reilly Media, Inc.},\n title = {Unit Test Frameworks: Tools for High-Quality Software Development},\n year = {2004}\n}
    

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

Toggle BibTeX Format
    Click Button    Toggle BibTeX format
