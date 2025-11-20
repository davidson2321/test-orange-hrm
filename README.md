# Automatización de Pruebas – OrangeHRM
Automatización de 3 funcionalidades críticas del sistema OrangeHRM utilizando **Python**, **Selenium** y **PyTest**, como parte del proceso de validación del sistema de Recursos Humanos.

---

## 🚀 Funcionalidades Automatizadas

### 1. Login
- Validación de login exitoso.
- Validación de login inválido.
- Verificación de mensajes de error.

### 2. Crear Empleado (Módulo PIM)
- Acceso al módulo PIM.
- Registro de un nuevo empleado con datos dinámicos.
- Validación de la pantalla “Personal Details”.

### 3. Buscar Usuario (Módulo Admin)
- Navegación a Admin → User Management.
- Búsqueda del usuario "Admin".
- Validación del resultado en la tabla.

---

## 📂 Estructura del Proyecto
automation-orangehrm/
│
├── conftest.py
├── requirements.txt
├── README.md
│
├── tests/
│ ├── test_01_login.py
│ ├── test_02_pim_add_employee.py
│ └── test_03_admin_search_user.py
│
└── report.html (se genera tras ejecutar las pruebas)



---

## 🛠️ Requisitos

Antes de ejecutar las pruebas, asegúrate de tener instalado:

- Python 3.8 o superior
- Google Chrome
- Pip actualizado

Instala las dependencias:

```bash
pip install -r requirements.txt
