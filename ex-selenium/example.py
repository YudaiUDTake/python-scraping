from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Chrome Options
options = Options()
options.add_argument('--headless') # headlessモード


DRIVER_PATH = 'chromedriver path'
driver = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=options)


url = 'https://www.google.com/'
driver.get(url)


# 操作一覧
"""
title = driver.title
url = driver.current_url

driver.back()
driver.forward()
driver.refresh()

driver.close()
driver.quit()

driver.save_screenshot('保存先path')

handle_array = driver.window_handles
driver.switch_to.window(handle_array[-1])

CSS selector

text : fetch Text

send_keys : Input Text

clear : delete Text

click : click element

send_keys(Keys.ENTER) : click Enter key ex.BACK_SPACE, ESCAPE, TAB

Select(element).select_by_value('value') ex. index, text
<-> deselect


driver.implicitly_wait(10) : implicit waiting

# 指定した要素が表示されるまで、明示的に30秒待機
selector = '{{ CSSセレクタ }}'
element = WebDriverWait(driver, 30).until(
	EC.visibility_of_element_located((By.CSS_SELECTOR, selector))
)
"""

# Options一覧
"""
options.add_argument('--headless') # headless
options.add_argument('--kiosk') # maximize window
options.add_argument('--disable-gpu');
options.add_argument('--disable-extensions');
options.add_argument('--proxy-server="direct://"');
options.add_argument('--proxy-bypass-list=*');
options.add_argument('--start-maximized');
"""