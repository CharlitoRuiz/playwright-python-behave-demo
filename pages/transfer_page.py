from playwright.sync_api import Page, expect


class TransferPage:

    def __init__(self, page: Page):
        self.page = page

        self.transfer_type = page.locator("#transfer-type")
        self.source_account = page.locator("#source-account")
        self.destination_account = page.locator("#destination-own-account")
        self.amount_input = page.locator("#transfer-amount")
        self.description_input = page.locator("#transfer-description")

        self.transfer_button = page.get_by_role(
            "button",
            name="Transferir"
        )

        self.confirm_button = page.get_by_role(
            "button",
            name="Confirmar"
        )
        self.success_message = page.get_by_text(
            "Transferencia realizada exitosamente"
        )

    def navigate_to_transfer(self):
        self.page.get_by_text("Transferencias", exact=True).first.click()

        self.page.get_by_role(
            "heading",
            name="Transferencias"
        ).wait_for(state="visible")

    def fill_transfer(
        self,
        amount: str,
        description: str
    ):
        self.transfer_type.select_option(index=0)
        self.source_account.select_option(index=0)
        self.destination_account.select_option(index=1)

        self.amount_input.fill(amount)
        self.description_input.fill(description)

    def submit_transfer(self):
        self.transfer_button.click()

    def confirm_transfer(self):
        self.confirm_button.wait_for(
            state="visible",
            timeout=5000
        )

        self.confirm_button.click()

    def is_transfer_confirmed(self) -> bool:
        expect(self.success_message).to_be_visible()
        return True