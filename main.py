import os
import shutil
import time
import subprocess

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


CHROME_DRIVER = os.environ.get("CHROMEDRIVER")
Download_path = r"C:\Users\dalla\.wdm\drivers\chromedriver\win32"
TINDER_SITE = r"https://tinder.com/"
subprocess.Popen(r"chrome.exe --remote-debugging-port=9222 --user-data-dir=C:\WebDriver\bin\localhost", shell=True)


try:
    service = Service(executable_path=CHROME_DRIVER)
except Exception as r:
    print(r)
    CHROM_VERSION = ChromeDriverManager().driver.get_version()
    service = Service(executable_path=ChromeDriverManager().install())
    shutil.move(os.path.join(Download_path, CHROM_VERSION, "chromedriver.exe"), r"C:\WebDriver\bin")


chrome_option = Options()
chrome_option.add_experimental_option("debuggerAddress", "localhost:9222")
driver = webdriver.Chrome(options=chrome_option)
driver.delete_all_cookies()


def swap_unlike():
    one_minutes = time.time() + 60
    while True:
        if time.time() < one_minutes:
            wait = WebDriverWait(driver, 15)
            dislike = wait.until(ec.element_to_be_clickable((By.TAG_NAME, 'body')))
            dislike.send_keys(Keys.LEFT)
        else:
            break
        time.sleep(1)


def main():
    driver.maximize_window()
    driver.get(TINDER_SITE)
    swap_unlike()
    driver.delete_all_cookies()
    time.sleep(5)
    driver.close()
    driver.quit()


if __name__ == '__main__':
    main()
