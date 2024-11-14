*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}        localhost:5001
${DELAY}         0.5 seconds
${HOME_URL}      http://${SERVER}
${SELECTOR_URL}  http://${SERVER}/Selector
${RESET_URL}     http://${SERVER}/reset_db
${BROWSER}       chrome
${HEADLESS}      false

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
    Title Should Be  Front Page

Selector Page Should Be Open
    Title Should Be  Select reference type

Go To Front Page
    Go To  ${HOME_URL}

Go To Selector Page
    Go To  ${SELECTOR_URL}