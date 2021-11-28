from behave import when, then, given
from selenium import webdriver
from unittest import TestCase
import time

#Nuevo usuario
@given(u'que ingreso al sistema con la dirección "{url}"')
def step_impl(context, url):

    context.driver = webdriver.Chrome()
    context.test = TestCase()
    context.driver.get(url)
    time.sleep(2)


@given(u'hago click en el botón "{texto_boton}"')
def step_impl(context, texto_boton):

    context.driver.find_element_by_link_text(texto_boton).click()
    time.sleep(2)


@given(u'capturo "{nombre}" en el nombre')
def step_impl(context, nombre):

    context.driver.find_element_by_id("id_nombre").send_keys(nombre)
    time.sleep(2)


@given(u'capturo "{apellido}" en el apellido')
def step_impl(context, apellido):

    context.driver.find_element_by_id("id_apellido").send_keys(apellido)
    time.sleep(2)


@given(u'capturo "{apellido}" en el segundo apellido')
def step_impl(context, apellido):

    context.driver.find_element_by_id("id_segundo_apellido").send_keys(apellido)
    time.sleep(2)


@given(u'capturo "{username}" en el username')
def step_impl(context, username):

    context.driver.find_element_by_id("id_username").send_keys(username)
    time.sleep(2)


@given(u'capturo "{email}" en correo')
def step_impl(context, email):

    context.driver.find_element_by_id("id_email").send_keys(email)
    time.sleep(2)


@given(u'capturo "{password}" en el password')
def step_impl(context, password):

    context.driver.find_element_by_id("id_password").send_keys(password)
    time.sleep(2)


@when(u'presiono el botón "Guardar"')
def step_impl(context):

    context.driver.find_element_by_id("id_guardar").click()
    time.sleep(2)


@then(u'puede ver al usuario "{usuario}" en la lista de usuarios'
      + ' y el mensaje "{mensaje}"')
def step_impl(context, usuario, mensaje):

    context.test.assertIn(usuario, context.driver.page_source)
    respuesta = context.driver.find_element_by_class_name('alert-success')
    assert mensaje == respuesta.text, f"esperado es {mensaje} y"
    +" obtenido es {respuesta}"
    time.sleep(2)


@then(u'puede ver el mensaje "{mensaje}" en la página')
def step_impl(context, mensaje):

    context.test.assertIn(mensaje, context.driver.page_source)
    time.sleep(2)


@then(u'sigo en la misma página con el título "{titulo}"')
def step_impl(context, titulo):

    respuesta = context.driver.find_element_by_tag_name('h1')
    assert titulo == respuesta.text, f"esperado es {titulo} y obtenido es {respuesta}"
    time.sleep(2)

#Iniciar sesión
@given(u'capturo "{username}" en el nombre de usuario')
def step_impl(context, username):

    context.driver.find_element_by_id("id_username").send_keys(username)
    time.sleep(2)

@given(u'capturo "{password}" en contraseña')
def step_impl(context, password):

    context.driver.find_element_by_id("id_password").send_keys(password)
    time.sleep(2)

@then(u'puedo ver la página de "{pagina}"')
def step_impl(context, pagina):

    context.test.assertIn(pagina, context.driver.page_source)
    time.sleep(2)

@then(u'puedo ver la alerta "{alerta}" en la página')
def step_impl(context, alerta):

    context.test.assertIn(alerta, context.driver.page_source)
    time.sleep(2)

#Eliminar Usuario
@given(u'presiono el botón de eliminar correspondiente a un registro de la lista')
def step_impl(context):

    context.drive.find_element_by_xpath('//*[@id="datatablesSimple"]/tbody/tr[1]/td[7]/button')
    time.sleep(2)
