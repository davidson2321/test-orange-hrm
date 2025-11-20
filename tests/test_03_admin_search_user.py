import pytest
from selenium.webdriver.common.by import By
from conftest import save_step_screenshot, login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_admin_buscar_usuario(driver, base_url):
    # Login
    login(driver, base_url, "Admin", "admin123")
    WebDriverWait(driver, 10).until(EC.url_contains("dashboard")) # Esperar a estar logueado

    # Ir a Admin → User Management
    driver.get(base_url.rstrip('/') + "/web/index.php/admin/viewSystemUsers")
    # Esperar a que el campo de búsqueda sea visible
    search_input_locator = (By.XPATH, "//label[contains(text(),'Username')]/following::input[1]")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(search_input_locator))

    # Buscar usuario "Admin"
    search_input = driver.find_element(*search_input_locator)
    search_input.send_keys("Admin")
    driver.find_element(By.XPATH, "//button[contains(.,'Search')]").click()

    # Validación: esperar a que el resultado aparezca en la tabla
    result_locator = (By.XPATH, "//div[contains(@class,'oxd-table-card')]//div[contains(text(),'Admin')]")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(result_locator))
    
    # La aserción es implícita: si el elemento se encuentra, la prueba pasa.
    save_step_screenshot(driver, "admin_usuario_encontrado")
