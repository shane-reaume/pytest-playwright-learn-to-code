from playwright.sync_api import Page
from conftest import describe, it, usefixture

@describe("Browser app test - per test")
class TestBrowserApp:
    @it("navigates to 'What's New' when logged in fresh each time")
    def test_whats_new(self, luma_test_page):
        luma_test_page.goto("https://magento.softwaretestingboard.com/what-is-new.html")
        assert "What's New" in luma_test_page.title()

    @it("navigates to 'Gear' also with fresh login")
    def test_gear(self, luma_test_page):
        luma_test_page.goto("https://magento.softwaretestingboard.com/gear.html")
        assert "Gear" in luma_test_page.title()

@describe("Browser app test - single login per class")
class TestBrowserAppClassScope:
    @it("navigates to 'What's New' and stays logged in across tests")
    def test_whats_new_single_login(self, luma_test_class_page):
        luma_test_class_page.goto("https://magento.softwaretestingboard.com/what-is-new.html")
        assert "What's New" in luma_test_class_page.title()

    @it("navigates to 'Gear' and is still logged in")
    def test_gear_single_login(self, luma_test_class_page):
        luma_test_class_page.goto("https://magento.softwaretestingboard.com/gear.html")
        assert "Gear" in luma_test_class_page.title()