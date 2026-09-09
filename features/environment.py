from playwright.sync_api import sync_playwright


def before_all(context):
    context.playwright = sync_playwright().start()

    context.browser = context.playwright.firefox.launch(headless=False)


def before_scenario(context, scenario):
    context.browser_context = context.browser.new_context(
        viewport={
            "width": 1440,
            "height": 900
        },
        service_workers="block"
    )

    context.page = context.browser_context.new_page()


def after_scenario(context, scenario):
    if scenario.status == "failed":
        print("\nLa prueba falló. Presioná ENTER para cerrar...")
        input()

    context.page.close()
    context.browser_context.close()


def after_all(context):
    context.browser.close()
    context.playwright.stop()