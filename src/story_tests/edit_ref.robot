*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To List Of References Page
Library    XML

*** Test Cases ***
Empty Reference List Is Declared
    Page Should Contain  No references found

Edit Book Reference Change Author Name And Submit Form
    Add New Book Reference
    Click Link  View list of references
    Page Should Contain  Unit Test Frameworks: Tools for High-Quality Software Development, Paul Hamill, 2004, O'Reilly Media, inc.
    Click Button  Edit
    Input Text  name=authors  John Hamill
    Click Button  Confirm Changes
    List Of References Page Should Be Open
    Page Should Contain  Unit Test Frameworks: Tools for High-Quality Software Development, John Hamill, 2004, O'Reilly Media, inc.

Edit Book Reference Year And Submit Form
    Add New Book Reference
    Click Link  View list of references
    Page Should Contain  Unit Test Frameworks: Tools for High-Quality Software Development, Paul Hamill, 2004, O'Reilly Media, inc.
    Click Button  Edit
    Input Text  name=year  2005
    Click Button  Confirm Changes
    List Of References Page Should Be Open
    Page Should Contain  Unit Test Frameworks: Tools for High-Quality Software Development, Paul Hamill, 2005, O'Reilly Media, inc.

Edit Misc Reference And Submit Form
    Add New Misc Reference
    Click Link  View list of references
    Page Should Contain  Lean Testing: Or Why Unit Tests Are Worse Than You Think, Eugen Kiss, WebPage Medium.com
    Click Button    Edit
    Input Text    name=year    2018
    Click Button  Confirm Changes
    List Of References Page Should Be Open
    Page Should Contain  Lean Testing: Or Why Unit Tests Are Worse Than You Think, Eugen Kiss, 2018, WebPage Medium.com

Edit Inbook Reference And Submit Form
    Add New Inbook Reference
    Click Link  View list of references
    Page Should Contain  Chapter 2 Media Technologies, Paul Hodkinson, 2017, SAGE Publications Inc., Media, Culture and Society: an Introduction
    Click Button  Edit
    Input Text  name=editors  Michal Ainsley
    Click Button  Confirm Changes
    List Of References Page Should Be Open
    Page Should Contain  Chapter 2 Media Technologies, Paul Hodkinson, 2017, SAGE Publications Inc., Michal Ainsley, Media, Culture and Society: an Introduction

Discard Changes
    Add New Book Reference
    Click Link  View list of references
    Page Should Contain  Unit Test Frameworks: Tools for High-Quality Software Development, Paul Hamill, 2004, O'Reilly Media, inc.
    Click Button  Edit
    Input Text  name=publisher  Wrong Publisher
    Click Link  Discard Changes
    List Of References Page Should Be Open
    Page Should Contain  Unit Test Frameworks: Tools for High-Quality Software Development, Paul Hamill, 2004, O'Reilly Media, inc.

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
    Input Text  name=authors  Paul Hamill
    Input Text  name=title  Unit Test Frameworks: Tools for High-Quality Software Development
    Input Text  name=year  2004
    Input Text  name=publisher  O'Reilly Media, inc.
    Click Button  Submit
    Front Page Should Be Open

Add New Misc Reference
    Go To Add New Misc Reference Page
    Input Text  name=authors  Eugen Kiss
    Input Text  name=title  Lean Testing: Or Why Unit Tests Are Worse Than You Think
    Input Text  name=howpublished  WebPage Medium.com
    Click Button  Submit
    Front Page Should Be Open

Add New Inbook Reference
    Go To Add New Inbook Reference Page
    Input Text  name=authors  Paul Hodkinson
    Input Text  name=title  Chapter 2 Media Technologies
    Input Text  name=booktitle  Media, Culture and Society: an Introduction
    Input Text  name=year  2017
    Input Text  name=publisher  SAGE Publications Inc.
    Click Button  Submit
    Front Page Should Be Open