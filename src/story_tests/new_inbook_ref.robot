*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To Add New Inbook Reference Page

*** Test Cases ***
Submitting Valid Form Redirects To Front Page
    Input Text  name=authors  Paul Hodkinson
    Input Text  name=title  Chapter 2 Media Technologies
    Input Text  name=booktitle  Media, Culture ans Society: an Introduction
    Input Text  name=year  2017
    Input Text  name=publisher  SAGE Publications Inc.
    Input Text  name=editors  Michal Ainsley
    Input Text  name=keywords  media
    Click Button  Submit
    Front Page Should Be Open

Can't Submit Form When Authors empty
    Input Text  name=title  Chapter 2 Media Technologies
    Input Text  name=booktitle  Media, Culture ans Society: an Introduction
    Input Text  name=year  2017
    Input Text  name=publisher  SAGE Publications Inc.
    Input Text  name=editors  Michal Ainsley
    Input Text  name=keywords  media
    Click Button  Submit
    Add New Inbook Reference Page Should Be Open

Can't Submit Form When Title Empty
    Input Text  name=authors  Paul Hodkinson
    Input Text  name=booktitle  Media, Culture ans Society: an Introduction
    Input Text  name=year  2017
    Input Text  name=publisher  SAGE Publications Inc.
    Input Text  name=editors  Michal Ainsley
    Input Text  name=keywords  media
    Click Button  Submit
    Add New Inbook Reference Page Should Be Open

Can't Submit Form When Book Title Empty
    Input Text  name=title  Chapter 2 Media Technologies
    Input Text  name=authors  Paul Hodkinson
    Input Text  name=year  2017
    Input Text  name=publisher  SAGE Publications Inc.
    Input Text  name=editors  Michal Ainsley
    Input Text  name=keywords  media
    Click Button  Submit
    Add New Inbook Reference Page Should Be Open

Can't Submit Form When Publisher Empty
    Input Text  name=title  Chapter 2 Media Technologies
    Input Text  name=authors  Paul Hodkinson
    Input Text  name=booktitle  Media, Culture ans Society: an Introduction
    Input Text  name=year  2017
    Input Text  name=editors  Michal Ainsley
    Input Text  name=keywords  media
    Click Button  Submit
    Add New Inbook Reference Page Should Be Open

Clicking Go Back Redirects To Selector
    Click Link  Go back
    Selector Page Should Be Open

*** Keywords ***
Reset Application And Go To Add New Inbook Reference Page
    Reset Database
    Go To Add New Inbook Reference Page