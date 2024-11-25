*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To Selector Page

*** Test Cases ***
Selector Does Not Redirect If Reference Type Not Chosen
    Click Button  Submit
    Selector Page Should Be Open 

Selector Redirects To Add New Book Reference
    Click Element  xpath://input[@type="radio" and @value="/add_book_reference"]
    Click Button  Submit
    Add New Book Reference Page Should Be Open

Clicking Go to front page Goes To Front Page
    Click Link  Go to front page
    Front Page Should Be Open

*** Keywords ***
Reset Application And Go To Selector Page
    Reset Database
    Go To Selector Page