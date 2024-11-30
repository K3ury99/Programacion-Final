import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Configurar el navegador Edge para las pruebas
@pytest.fixture
def driver():
    edge_options = Options()
    edge_options.add_argument("--start-maximized")
    driver = webdriver.Edge(options=edge_options)
    yield driver
    driver.quit()




# Crear carpeta 'imagenes' si no existe
@pytest.fixture(scope="session", autouse=True)
def create_images_folder():
    if not os.path.exists("imagenes"):
        os.makedirs("imagenes")




    # Función para esperar un elemento
def esperar_elemento(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))



# Prueba 1: Login vacío (sin credenciales)
def test_login_fallido(driver):
    url = "https://bondelic.netlify.app"
    driver.get(url)

    
    email_field = esperar_elemento(driver, By.CSS_SELECTOR, "input[type='text']")
    password_field = esperar_elemento(driver, By.CSS_SELECTOR, "input[type='password']")
    password_field.send_keys(Keys.RETURN) 

    
    driver.save_screenshot("imagenes/Prueba_1_Login_vacío.png")


# Prueba 2: Login con credenciales válidas
def test_login_con_credenciales(driver):
    url = "https://bondelic.netlify.app"
    driver.get(url)

    
    email_field = esperar_elemento(driver, By.CSS_SELECTOR, "input[type='text']")
    password_field = esperar_elemento(driver, By.CSS_SELECTOR, "input[type='password']")
    email_field.clear()
    password_field.clear()
    email_field.send_keys("keury@example.com") 
    password_field.send_keys("369") 

    driver.save_screenshot("imagenes/Prueba_2_login_con_credenciales_1.png")

    password_field.send_keys(Keys.RETURN)

    time.sleep(2)

    driver.save_screenshot("imagenes/Prueba_2_login_con_credenciales_2.png")



# Prueba 3: Hacer scroll down hasta el final de la página de inicio y tomar una captura
def test_scroll_inicial(driver):
    url = "https://bondelic.netlify.app"
    driver.get(url)
    time.sleep(2)

    
    email_field = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
    password_field = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
    email_field.clear()
    password_field.clear()
    email_field.send_keys("keury@example.com") 
    password_field.send_keys("369") 
    password_field.send_keys(Keys.RETURN)
    time.sleep(5)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(3)

    driver.save_screenshot("imagenes/Prueba_3_Scroll_Down.png")


# Prueba 4: Ir a la página de productos y tomar una captura
def test_pagina_productos(driver):
    url = "https://bondelic.netlify.app"
    driver.get(url)

    
    email_field = esperar_elemento(driver, By.CSS_SELECTOR, "input[type='text']")
    password_field = esperar_elemento(driver, By.CSS_SELECTOR, "input[type='password']")
    email_field.clear()
    password_field.clear()
    email_field.send_keys("keury@example.com") 
    password_field.send_keys("369")  
    password_field.send_keys(Keys.RETURN)

    productos_button = esperar_elemento(driver, By.LINK_TEXT, "Productos")
    productos_button.click()

    driver.save_screenshot("imagenes/Prueba_4_Pagina_Productos.png")



# Prueba 5: Ir a la página del formulario y tomar una captura
def test_pagina_formulario(driver):
    url = "https://bondelic.netlify.app"
    driver.get(url)

    email_field = esperar_elemento(driver, By.CSS_SELECTOR, "input[type='text']")
    password_field = esperar_elemento(driver, By.CSS_SELECTOR, "input[type='password']")
    email_field.clear()
    password_field.clear()
    email_field.send_keys("keury@example.com") 
    password_field.send_keys("369")
    password_field.send_keys(Keys.RETURN)

    formulario_button = esperar_elemento(driver, By.LINK_TEXT, "Registrate")
    formulario_button.click()

    driver.save_screenshot("imagenes/Prueba 5_Pagina_Formulario.png")



# Prueba 6: Ir a "Nosotros > Bondelic" y tomar una foto
def test_nosotros_bondelic(driver):
    url = "https://bondelic.netlify.app"
    driver.get(url)

    email_field = esperar_elemento(driver, By.CSS_SELECTOR, "input[type='text']")
    password_field = esperar_elemento(driver, By.CSS_SELECTOR, "input[type='password']")
    email_field.clear()
    password_field.clear()
    email_field.send_keys("keury@example.com") 
    password_field.send_keys("369")  
    password_field.send_keys(Keys.RETURN)

    nosotros_button = esperar_elemento(driver, By.LINK_TEXT, "Nosotros")
    nosotros_button.click()

    bondelic_buttons = driver.find_elements(By.LINK_TEXT, "Bondelic")

    # Hacer clic en el segundo elemento
    if len(bondelic_buttons) > 1: 
        bondelic_buttons[1].click() 
    else:
        raise Exception("No se encontró un segundo elemento 'Bondelic'.")

    driver.save_screenshot("imagenes/Prueba_6_Nosotros_Bondelic.png")


# Prueba 7: Ir a "Nosotros > Misión" y tomar una foto
def test_nosotros_mision(driver):
    url = "https://bondelic.netlify.app"
    driver.get(url)

    email_field = esperar_elemento(driver, By.CSS_SELECTOR, "input[type='text']")
    password_field = esperar_elemento(driver, By.CSS_SELECTOR, "input[type='password']")
    email_field.clear()
    password_field.clear()
    email_field.send_keys("keury@example.com") 
    password_field.send_keys("369")  
    password_field.send_keys(Keys.RETURN)

    nosotros_button = esperar_elemento(driver, By.LINK_TEXT, "Nosotros")
    nosotros_button.click()

    mision_button = esperar_elemento(driver, By.LINK_TEXT, "Misión")
    mision_button.click()

    driver.save_screenshot("imagenes/Prueba_7_Nosotros_Mision.png")



# Prueba 8: Ir a "Nosotros > Visión" y tomar una foto
def test_nosotros_vision(driver):
    url = "https://bondelic.netlify.app"
    driver.get(url)

    email_field = esperar_elemento(driver, By.CSS_SELECTOR, "input[type='text']")
    password_field = esperar_elemento(driver, By.CSS_SELECTOR, "input[type='password']")
    email_field.clear()
    password_field.clear()
    email_field.send_keys("keury@example.com") 
    password_field.send_keys("369")  
    password_field.send_keys(Keys.RETURN)

    nosotros_button = esperar_elemento(driver, By.LINK_TEXT, "Nosotros")
    nosotros_button.click()

    vision_button = esperar_elemento(driver, By.LINK_TEXT, "Visión")
    vision_button.click()

    driver.save_screenshot("imagenes/Prueba_8_Nosotros_Vision.png")



# Prueba 9: Ir a "Nosotros > Valores" y tomar una foto
def test_nosotros_valores(driver):
    url = "https://bondelic.netlify.app"
    driver.get(url)

    email_field = esperar_elemento(driver, By.CSS_SELECTOR, "input[type='text']")
    password_field = esperar_elemento(driver, By.CSS_SELECTOR, "input[type='password']")
    email_field.clear()
    password_field.clear()
    email_field.send_keys("keury@example.com") 
    password_field.send_keys("369")  
    password_field.send_keys(Keys.RETURN)

    nosotros_button = esperar_elemento(driver, By.LINK_TEXT, "Nosotros")
    nosotros_button.click()

    valores_button = esperar_elemento(driver, By.LINK_TEXT, "Valores")
    valores_button.click()

    driver.save_screenshot("imagenes/Prueba_9_Nosotros_Valores.png")




# Prueba 10: Navegar por el slideshow en la página de productos
def test_navegar_slideshow(driver):
    url = "https://bondelic.netlify.app"
    driver.get(url)

    email_field = esperar_elemento(driver, By.CSS_SELECTOR, "input[type='text']")
    password_field = esperar_elemento(driver, By.CSS_SELECTOR, "input[type='password']")
    email_field.clear()
    password_field.clear()
    email_field.send_keys("keury@example.com") 
    password_field.send_keys("369")  
    password_field.send_keys(Keys.RETURN)

    productos_button = esperar_elemento(driver, By.LINK_TEXT, "Productos")
    productos_button.click()

    time.sleep(2)

    # Navegar - primer slide 6 veces a la derecha
    driver.execute_script("document.querySelector('.swiper-container').swiper.slideTo(6);")
    time.sleep(2)

    # Navegar al segundo slider
    driver.execute_script("document.querySelectorAll('.swiper-container')[1].swiper.slideTo(0);") 
    time.sleep(2)

    # Mover el segundo slider 5 veces a la derecha
    for _ in range(5):
        driver.execute_script("document.querySelectorAll('.swiper-container')[1].swiper.slideNext();")
        time.sleep(2) 

    # Captura de pantalla despues de la navegación - Funciona no sabia que esto se podía!
    driver.save_screenshot("imagenes/Prueba_10_navegar_slideshow_productos.png")




# Prueba 11: Tomar una foto antes y después de hacer clic en el botón de salir
def test_salir_login(driver):
    url = "https://bondelic.netlify.app"
    driver.get(url)

    email_field = esperar_elemento(driver, By.CSS_SELECTOR, "input[type='text']")
    password_field = esperar_elemento(driver, By.CSS_SELECTOR, "input[type='password']")
    email_field.clear()
    password_field.clear()
    email_field.send_keys("keury@example.com") 
    password_field.send_keys("369")  
    password_field.send_keys(Keys.RETURN)

    time.sleep(2)

    driver.save_screenshot("imagenes/Prueba_11_Antes_salir_login.png")

    salir_button = esperar_elemento(driver, By.LINK_TEXT, "Salir")
    salir_button.click()

    time.sleep(2) 

    driver.save_screenshot("imagenes/Prueba_11_Despues_salir_login.png")


# Gracias por revisar este codigo, cualquier inquietud en el inicio de GitHub esta mi correo personal!
# Keury Ramirez - 20231101.
