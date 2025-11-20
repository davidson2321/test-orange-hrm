import pytest
from selenium.webdriver.common.by import By
from conftest import save_step_screenshot, login
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_pim_crear_empleado(driver, base_url):
    # Login
    login(driver, base_url, "Admin", "admin123")
    WebDriverWait(driver, 10).until(EC.url_contains("dashboard")) # Esperar a estar logueado

    # Ir a PIM → Add Employee
    driver.get(base_url.rstrip('/') + "/web/index.php/pim/addEmployee")
    # Esperar a que el campo del nombre sea visible
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "firstName")))

    # Crear nombre dinámico
    ts = datetime.now().strftime("%H%M%S")
    first = "AutoFN" + ts
    last = "AutoLN" + ts

    # Llenar campos y guardar
    driver.find_element(By.NAME, "firstName").send_keys(first)
    driver.find_element(By.NAME, "lastName").send_keys(last)
    driver.find_element(By.XPATH, "//button[contains(.,'Save')]").click()

    # Validación: Esperar a que aparezca el título "Personal Details"
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Personal Details')]"))
    )
    
    # La aserción es implícita: si el elemento anterior se encuentra, la prueba continúa. Si no, WebDriverWait lanzará una excepción.
    save_step_screenshot(driver, "empleado_creado_ok")
