*** Settings ***
Resource  resource.robot
Resource  login_resource.robot

*** Test Cases ***
Login After Successful Registration
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Succeed
    Go To Login Page
    Login Page Should Be Open
    Set Username  kalle
    Set Password  kalle123
    Submit Credentials
    Login Should Succeed


Login After Failed Registration
    Set Username  ka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Fail With Message  too shorte
    Go To Login Page
    Login Page Should Be Open
    Set Username  kalle
    Set Password  kalle123
    Submit Credentials
    Login Should Fail With Message  


