import pytest
from selenium.webdriver.common.by import By
from conftest import save_step_screenshot, login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_valido(driver, base_url):
    login(driver, base_url, "Admin", "admin123")
    # Usar una espera explícita para asegurar que la página ha cargado después del login.
    # Esperamos un máximo de 10 segundos hasta que la URL contenga "dashboard".
    WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
    assert "dashboard" in driver.current_url.lower()
    save_step_screenshot(driver, "login_valido_dashboard")

def test_login_invalido(driver, base_url):
    driver.get(base_url)
    login(driver, base_url, "invalidUser", "badpassword")
    # busca mensaje de error o que siga en la pagina de login
    err = driver.find_elements(By.XPATH, "//*[contains(., 'Invalid') or contains(., 'credentials') or contains(@class,'oxd-alert-content-text')]")
    assert len(err) > 0
    save_step_screenshot(driver, "login_invalido_error")
