import json

from behave import given, when, then

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


@given("que el usuario se encuentra en la página de inicio de sesión")
def step_open_login(context):
    context.login_page = LoginPage(context.page)
    context.login_page.navigate()


@when("ingresa credenciales válidas")
def step_enter_credentials(context):

    with open("test_data/users.json", encoding="utf-8") as file:
        users = json.load(file)

    user = users["valid_user"]

    context.username = user["username"]
    context.password = user["password"]


@when("selecciona la opción de iniciar sesión")
def step_login(context):

    context.login_page.login(
        context.username,
        context.password
    )


@then("debe ingresar correctamente al Home Banking")
def step_validate_login(context):

    dashboard = DashboardPage(context.page)

    assert dashboard.is_loaded(), \
        "El usuario no ingresó correctamente al Home Banking"