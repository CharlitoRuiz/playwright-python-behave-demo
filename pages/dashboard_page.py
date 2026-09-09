from playwright.sync_api import Page, expect


class DashboardPage:

    def __init__(self, page: Page):
        self.page = page
        self.panel_heading = page.get_by_role("heading", name="Panel Principal")

    def is_loaded(self) -> bool:
        expect(self.panel_heading).to_be_visible()
        return True