*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To Selector Page

*** Test Cases ***
Selector Does Not Redirect If Reference Type Not Chosen
    Go To Selector Page
    Click Button  Submit
    Selector Page Should Be Open 

Selector Redirects To Add New Book Reference
    Go To Selector Page
    Click Element  xpath://input[@type="radio" and @value="/add_book_reference"]
    Click Button  Submit
    Add New Book Reference Page Should Be Open

*** Keywords ***
Reset Application And Go To Selector Page
    Go To Front Page
    # Resetointia ei ole vielä implementoitu