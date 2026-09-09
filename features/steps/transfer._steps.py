import json

from behave import given, when, then

from pages.login_page import LoginPage
from pages.transfer_page import TransferPage


@given("que el usuario se encuentra autenticado en Home Banking")
def step_authenticated_user(context):

    context.login_page = LoginPage(context.page)
    context.login_page.navigate()

    with open("test_data/users.json", encoding="utf-8") as file:
        data = json.load(file)

    user = data["valid_user"]

    context.login_page.login(
        user["username"],
        user["password"]
    )

    # Esperar que aparezca un elemento estable del dashboard.
    context.page.get_by_text(
        "Panel Principal"
    ).wait_for(
        state="visible",
        timeout=10000
    )


@when("navega hacia la opción de transferencias")
def step_navigate_transfer(context):

    context.transfer_page = TransferPage(context.page)
    context.transfer_page.navigate_to_transfer()


@when("completa los datos de una transferencia válida")
def step_fill_transfer(context):

    with open("test_data/users.json", encoding="utf-8") as file:
        data = json.load(file)

    transfer_data = data["transfer"]

    context.transfer_page.fill_transfer(
        transfer_data["amount"],
        transfer_data["description"]
    )

    context.transfer_page.submit_transfer()


@when("confirma la operación")
def step_confirm_transfer(context):

    context.transfer_page.confirm_transfer()


@then("debe visualizar la confirmación de la transferencia")
def step_validate_transfer(context):
    assert context.transfer_page.is_transfer_confirmed()