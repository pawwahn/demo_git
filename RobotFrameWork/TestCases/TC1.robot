*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://demo.nopcommerce.com

*** Test Cases ***
LoginTest
    #create webdriver chrome executable_path='C:\Python38\Scripts\chromedriver.exe'
    open browser    ${url} ${browser}
    maximize browser window
    loginToApplication
    close browser


*** Keywords ***
loginToApplication
    click link  xpath://a[@class='ico-login']
    sleep   5
    input text  id:Email    pavan.soft44@gmail.com
    sleep   5
    input text  id:Password     password123
