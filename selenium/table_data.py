from selenium import webdriver
from selenium.webdriver.common.by import By


def test_table_data():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get('https://the-internet.herokuapp.com/tables')

    driver.find_element(By.XPATH, "//span[text()='Last Name']").click()
    driver.find_element(By.XPATH, "//span[text()='First Name']").click()

    list_element = driver.find_elements(By.XPATH, '//table[@id ="table1"]/tbody/tr/td[3]')

    i = 1
    status = False
    for element in list_element:
        email = element.text
        if email == "jsmith@gmail.com":
            #driver.find_element(By.XPATH,'//table[@id ="table1"]/tbody/tr['+str(i)+']/td[6]/a').click()
            print("email found")
            status = True
            break
        i +=1
    assert status == True






