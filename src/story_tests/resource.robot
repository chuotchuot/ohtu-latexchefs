*** Settings ***
Library  SeleniumLibrary
Library  OperatingSystem

*** Variables ***
${SERVER}            localhost:5001
${DELAY}             0.5 seconds
${HOME_URL}          http://${SERVER}
${SELECTOR_URL}      http://${SERVER}/selector
${RESET_URL}         http://${SERVER}/reset_db
${BOOK_REF_URL}      http://${SERVER}/add_book_reference
${INBOOK_REF_URL}    http://${SERVER}/add_inbook_reference
${MISC_REF_URL}      http://${SERVER}/add_misc_reference
${REF_LIST_URL}      http://${SERVER}/list_of_references
${BROWSER}           chrome
${HEADLESS}          false

*** Keywords ***
Open And Configure Browser
    IF  $BROWSER == 'chrome'
        ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    ELSE IF  $BROWSER == 'firefox'
        ${options}  Evaluate  sys.modules['selenium.webdriver'].FirefoxOptions()  sys
    END
    IF  $HEADLESS == 'true'
        Set Selenium Speed  0
        Call Method  ${options}  add_argument  --headless
    ELSE
        Set Selenium Speed  ${DELAY}
    END
    Open Browser  browser=${BROWSER}  options=${options}

Front Page Should Be Open
    Wait Until Page Contains  Front Page | References
    Title Should Be  Front Page | References

Selector Page Should Be Open
    Wait Until Page Contains  Select reference type | References
    Title Should Be  Select reference type | References

Add New Book Reference Page Should Be Open
    Wait Until Page Contains  Add a new book reference | References
    Title Should Be  Add a new book reference | References

Add New Misc Reference Page Should Be Open
    Wait Until Page Contains  Add a new miscellaneous reference | References
    Title Should Be  Add a new miscellaneous reference | References

Add New Inbook Reference Page Should Be Open
    Wait Until Page Contains  Add a new inbook reference | References
    Title Should Be  Add a new inbook reference | References

List Of References Page Should Be Open
    Wait Until Page Contains  List of references | References
    Title Should Be  List of references | References

Edit Reference Page Should Be Open
    Wait Until Page Contains  Edit Reference | References
    Title Should Be  Edit Reference | References

Delete Reference Page Should Be Open
    Wait Until Page Contains  Delete Reference | References
    Title Should Be  Delete Reference | References

Go To Front Page
    Go To  ${HOME_URL}

Go To Selector Page
    Go To  ${SELECTOR_URL}

Go To Add New Book Reference Page
    Go To  ${BOOK_REF_URL}

Go To Add New Misc Reference Page
    Go To  ${MISC_REF_URL}

Go To List Of References Page
    Go To  ${REF_LIST_URL}

Go To Add New Inbook Reference Page
    Go To  ${INBOOK_REF_URL}

Reset Database
    Go To  ${RESET_URL}