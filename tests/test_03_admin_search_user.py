import pytest
from selenium.webdriver.common.by import By
from conftest import save_step_screenshot
import time

def test_admin_buscar_usuario(driver, base_url):
    driver.get(base_url)

    # Login
    driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[contains(.,'Login')]").click()
    time.sleep(2)

    # Ir a Admin → User Management
    driver.get(base_url.rstrip('/') + "/web/index.php/admin/viewSystemUsers")
    time.sleep(2)

    # Buscar usuario "Admin"
    search_input = driver.find_element(By.XPATH, "//label[contains(text(),'Username')]/following::input[1]")
    search_input.send_keys("Admin")

    driver.find_element(By.XPATH, "//button[contains(.,'Search')]").click()
    time.sleep(2)

    # Validación: que aparezca en tabla
    result = driver.find_elements(By.XPATH, "//div[contains(@class,'oxd-table-card')]//div[contains(text(),'Admin')]")
    assert len(result) > 0

    save_step_screenshot(driver, "admin_usuario_encontrado")
