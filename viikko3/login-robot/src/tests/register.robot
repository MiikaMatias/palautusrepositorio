*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input  new
    Input Credentials  new_1  new_2
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command
    Input Credentials  kalle  kalle123
    Output Should Contain  Username taken

Register With Too Short Username And Valid Password
    Input New Command
    Input Credentials  k  kalle123
    Output Should Contain  Shit length bozo

Register With Enough Long But Invalid Username And Valid Password
    Input New Command
    Input Credentials  ka!lle  kalle123
    Output Should Contain  Shit letters try again bozo

Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  kallee  k
    Output Should Contain  Shit pass try again bozo

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  kallee  kkkkkkkkkkk
    Output Should Contain  Only letters in pass try again bozo

*** Keywords ***
Input New Command And Create User
    Input New Command
    Input Credentials  kalle  kalle123

