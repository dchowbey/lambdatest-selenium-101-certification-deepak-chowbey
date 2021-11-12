import time
import urllib.request
import os

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_selenium_101_lambda_assignment(get_remote_driver):
    driver = get_remote_driver

    try:
        driver.find_element(By.XPATH, "//span[contains(@class,'cookie__bar__close')]").click()
    except NoSuchElementException as e:
        print(e)

    driver.maximize_window()
    driver.get('https://www.lambdatest.com/automation-demos/')
    driver.find_element(By.ID, "username").send_keys('lambda')
    driver.find_element(By.NAME, 'password').send_keys('lambda123')
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    driver.find_element(By.NAME, "email").send_keys("deepakchowbey8@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "#populate").click()
    alert_win = driver.switch_to.alert
    alert_win.accept()

    driver.find_element(By.XPATH, "//input[@id='3months']").click()
    driver.find_element(By.CSS_SELECTOR, "#customer-service").click()
    driver.find_element(By.CSS_SELECTOR, "#discounts").click()
    driver.find_element(By.XPATH, "//label[text()='Delivery time']").click()

    drop_down = Select(driver.find_element(By.CSS_SELECTOR, "#preferred-payment"))
    drop_down.select_by_visible_text("Cash on delivery")
    driver.execute_script("window.scrollBy(0, 500)","")
    tried_ecom = driver.find_element(By.CSS_SELECTOR, "input[name='tried-ecom']")
    tried_ecom.click()
    # driver.execute_script("arguments[0].scrollIntoView();", tried_ecom)
    time.sleep(1)

    scale = driver.find_element(By.XPATH, "//div[contains(@style,'height: 16px; width: 5px;')]")

    time.sleep(1)
    target = driver.find_element(By.XPATH, "//div[contains(@style,'540px')]")
    action = ActionChains(driver)
    print("Before Perform")
    action.click_and_hold(scale).move_to_element(target).perform()
    print("After Perform")

    time.sleep(5)
    slider_position = int(driver.find_element(By.XPATH, "//div[@role='slider']").get_attribute('aria-valuenow'))
    print(slider_position)
    assert slider_position / 10 == 9

    driver.find_element(By.CSS_SELECTOR, "textarea[id='comments']").send_keys("feedback entered")

    time.sleep(2)
    # driver.execute_script('''window.open("https://www.lambdatest.com/selenium-automation", "_blank");''')
    driver.execute_script("window.open('https://www.lambdatest.com/selenium-automation', '_blank');")
    driver.switch_to.window(driver.window_handles[1])
    # driver.pag

    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "//span[contains(@class,'cookie__bar__close')]").click()
    except NoSuchElementException as e:
        print(e)

    img_loc = driver.find_element(By.CSS_SELECTOR, "img[title='Jenkins']").get_attribute('src')
    print(img_loc)
    img_name = img_loc.split("/")[-1]
    print(img_loc)
    urllib.request.urlretrieve(img_loc, 'jenkins.svg')
    driver.switch_to.window(driver.window_handles[0])
    print(os.getcwd())
    driver.find_element(By.CSS_SELECTOR, "#file").send_keys( os.getcwd() + "/" +img_name)
    print(alert_win.text)
    alert_msg = alert_win.text
    assert "your image upload sucessfully!!" == alert_msg

    alert_win.accept()
    driver.find_element(By.CSS_SELECTOR, "button[id='submit-button']").click()
    msg = driver.find_element(By.CLASS_NAME, "success-message").text
    print(msg)
    assert "You have successfully submitted the form." in msg

    # driver.quit()




