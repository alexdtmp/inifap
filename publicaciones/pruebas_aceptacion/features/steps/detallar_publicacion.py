import time
from behave import given, when, then

@given(u'que me encuentro ya logueado como usuario revisor')
def step_impl(context):
    login(context)

@given(u'me dirijo a la pantalla de inicio del sistema')
def step_impl(context):
    context.driver.get(f"{context.url}")
    time.sleep(1)

@given(u'hago click en la pestaña que lleva por nombre "Mis revisiones"')
def step_impl(context):
    context.driver.find_element_by_id('id_mis_revisiones').click()
    time.sleep(1)
    
@given(u'veo el encabezado "{encabezado}"')
def step_impl(context, encabezado):
    respuesta = context.driver.find_element_by_id('id_revisar_encabezado').text
    assert encabezado in respuesta, f"esperado es {encabezado} y obtenido es {respuesta}"
    time.sleep(1)


@when(u'presiono el botón ver en una de las publicaciones de la lista')
def step_impl(context):
    context.driver.find_element_by_id('id_ver').click()
    time.sleep(1)

@then(u'el sistema me muestra el encabezado "{encabezado}"')
def step_impl(context,encabezado):
    respuesta = context.driver.find_element_by_id('id_encabezado').text
    assert encabezado in respuesta, f"esperado es {encabezado} y obtenido es {respuesta}"
    time.sleep(1)
    
@then(u'puedo ver el campo "Título de la publicación"')
def step_impl(context):
    respuesta = context.driver.find_element_by_id('id_titulo').text
    assert "Título de la publicación" in respuesta, f"esperado es 'Título de la publicación' y obtenido es {respuesta}"
    time.sleep(1)
    
@then(u'puedo ver el campo "Autor"')
def step_impl(context):
    respuesta = context.driver.find_element_by_id('id_autor').text
    assert "Autor" in respuesta, f"esperado es 'Autor' y obtenido es {respuesta}"
    time.sleep(1)

@then(u'puedo ver el campo "Estado"')
def step_impl(context):
    respuesta = context.driver.find_element_by_id('id_estado').text
    assert "Estado" in respuesta, f"esperado es 'Estado' y obtenido es {respuesta}"
    time.sleep(1)

def login(context):
    context.driver.get(f"{context.url}{'usuarios/login'}")
    context.driver.find_element_by_id('id_username').send_keys('revisor')
    context.driver.find_element_by_id('id_password').send_keys('temporal2019')
    context.driver.find_element_by_xpath(
        '//*[@id="layoutAuthentication_content"]/main/div/div/div/div/div[2]/form/div[3]/button').click()