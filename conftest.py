import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from datetime import datetime
from selenium.webdriver.common.by import By

@pytest.fixture(scope="session")
def base_url():
    return "https://opensource-demo.orangehrmlive.com/"

@pytest.fixture
def driver(tmp_path, request):
    options = Options()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless=new")
    drv = webdriver.Chrome(options=options)
    drv.implicitly_wait(8)

    screenshots_dir = tmp_path / "screenshots"
    screenshots_dir.mkdir(exist_ok=True)
    drv._screenshots_dir = screenshots_dir

    def fin():
        # guardar una captura final con timestamp
        try:
            ts = datetime.now().strftime("%Y%m%d_%H%M%S")
            drv.save_screenshot(str(screenshots_dir / f"final_{ts}.png"))
        except Exception:
            pass
        drv.quit()
    request.addfinalizer(fin)
    return drv

def save_step_screenshot(driver, name):
    # helper para usar en tests
    import os
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = driver._screenshots_dir / f"{name}_{ts}.png"
    driver.save_screenshot(str(path))
    return str(path)

def login(driver, base_url, username, password):
    driver.get(base_url)
    # Inputs robustos por placeholder
    user = driver.find_element(By.XPATH, "//input[@placeholder='Username' or @name='username' or @id='txtUsername']")
    pwd = driver.find_element(By.XPATH, "//input[@placeholder='Password' or @name='password' or @id='txtPassword']")
    user.clear(); user.send_keys(username)
    pwd.clear(); pwd.send_keys(password)
    # botón login
    btn = driver.find_element(By.XPATH, "//button[contains(., 'Login') or contains(@type,'submit')]")
    btn.click()
