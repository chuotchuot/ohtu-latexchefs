*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To Add Reference With Doi Page
*** Test Cases ***
Add A Reference Using Doi
    Input Text  doi  10.1093/sleep/zsaa159
    Click Button  Submit
    Front Page Should Be Open
    Go To List Of References Page
    Page Should Contain  Limiting racial disparities and bias for wearable devices in health science research, Colvonen, Peter J and DeYoung, Pamela N and Bosompra, Naa-Oye A and Owens, Robert L, 2020, Sleep, 43, 10, September

*** Keywords ***
Reset Application And Go To Add Reference With Doi Page
    Reset Database
    Go To Add Reference With Doi Page