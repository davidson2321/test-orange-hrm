import pytest
from selenium.webdriver.common.by import By
from conftest import save_step_screenshot
import time
from datetime import datetime

def test_pim_crear_empleado(driver, base_url):
    driver.get(base_url)

    # Login
    driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[contains(.,'Login')]").click()
    time.sleep(2)

    # Ir a PIM → Add Employee
    driver.get(base_url.rstrip('/') + "/web/index.php/pim/addEmployee")
    time.sleep(2)

    # Crear nombre dinámico
    ts = datetime.now().strftime("%H%M%S")
    first = "AutoFN" + ts
    last = "AutoLN" + ts

    # Llenar campos
    driver.find_element(By.NAME, "firstName").send_keys(first)
    driver.find_element(By.NAME, "lastName").send_keys(last)

    # Guardar
    driver.find_element(By.XPATH, "//button[contains(.,'Save')]").click()
    time.sleep(3)

    # 🔥 Validación actualizada (Personal Details)
    personal_details = driver.find_elements(
        By.XPATH, 
        "//*[contains(text(),'Personal Details') or contains(text(),'Employee Full Name')]"
    )

    assert len(personal_details) > 0, "El empleado no se creó correctamente."

    save_step_screenshot(driver, "empleado_creado_ok")
