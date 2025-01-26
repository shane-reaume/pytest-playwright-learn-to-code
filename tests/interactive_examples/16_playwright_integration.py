"""
Playwright Integration Learning Module

This module covers Playwright test automation through practical test examples:
- Browser Automation Basics
  * Browser launch and context
  * Page navigation
  * Element selectors
  * Actions (click, type, etc.)
- Selectors and Elements
  * CSS selectors
  * XPath selectors
  * Text selectors
  * Chained selectors
- Page Interactions
  * Forms and inputs
  * File uploads
  * Dialogs
  * Frames and iframes
- Assertions and Verification
  * Element presence
  * Text content
  * Attributes
  * Screenshots
- Advanced Features
  * Network interception
  * Mobile emulation
  * Geolocation
  * Authentication
- Test Patterns
  * Page Object Model
  * Test data management
  * Error handling
  * Reporting

Each test demonstrates a specific concept with practical examples.
"""

from tests.conftest import describe, it
from tests.utils import (
    print_code_block, get_user_input, check_answer,
    print_section_header, print_subsection_header, print_instruction,
    print_success, print_error, print_info
)
import time
from playwright.sync_api import Page, expect

def get_browser_basics():
    return '''
        from playwright.sync_api import Page, expect

        # Basic test using pytest fixture
        # The 'page' fixture is automatically provided by pytest-playwright
        def test_basic_navigation(page: Page):
            # Navigate to a URL and wait for the page to load
            page.goto("https://example.com")
            
            # Verify page title using Playwright's expect API
            # This is preferred over assert statements
            expect(page).to_have_title("Example Domain")
            
            # Find element using locator and verify its text
            # Locators are chainable and retry automatically
            heading = page.locator("h1")
            expect(heading).to_have_text("Example Domain")
            
            # Capture screenshot for visual debugging
            # Screenshots are saved relative to test directory
            page.screenshot(path="example.png")

        # Example of form interaction and verification
        def test_form_submission(page: Page):
            page.goto("https://example.com/login")
            
            # Use role and label selectors (preferred over CSS/XPath)
            # These selectors are more resilient to UI changes
            page.get_by_label("Username").fill("user123")
            page.get_by_label("Password").fill("pass123")
            page.get_by_role("button", name="Login").click()
            
            # Verify successful login using role selector
            expect(page.get_by_role("heading")).to_have_text("Welcome back!")

        # Example of handling dynamic content
        def test_dynamic_content(page: Page):
            page.goto("https://example.com/dashboard")
            
            # Wait for all network requests to complete
            # This is useful for Single Page Applications
            page.wait_for_load_state("networkidle")
            
            # Use test-id for stable element selection
            # data-testid attributes are recommended for testing
            user_info = page.get_by_test_id("user-info")
            expect(user_info).to_be_visible()
            expect(user_info).to_contain_text("Profile")
    '''

def get_selector_examples():
    return '''
        # CSS Selectors
        page.locator("h1").click()                    # Tag name
        page.locator(".class-name").click()           # Class
        page.locator("#id-name").click()              # ID
        page.locator("div[data-test=value]").click()  # Attribute

        # Text selectors
        page.get_by_text("Click me").click()          # Exact text
        page.get_by_text("Click", exact=False)        # Partial text
        page.get_by_role("button", name="Submit")     # ARIA role

        # Chained selectors
        page.locator("form").locator("input#email")   # Form -> input
        page.locator("table").nth(2)                  # Third table
        page.locator("tr").filter(has_text="Name")    # Row with text

        # XPath selectors (use sparingly)
        page.locator("xpath=//button[contains(text(), 'Submit')]")
        page.locator("xpath=//div[@class='menu']//a")
    '''

def get_interaction_examples():
    return '''
        # Form interactions
        page.get_by_label("Username").fill("testuser")
        page.get_by_label("Password").fill("password123")
        page.get_by_role("button", name="Login").click()

        # File upload
        page.get_by_label("Upload file").set_input_files("path/to/file.pdf")

        # Handling dialogs
        page.on("dialog", lambda dialog: dialog.accept())
        page.get_by_text("Delete").click()  # Triggers confirmation dialog

        # Working with frames
        frame = page.frame_locator("iframe#chat").locator("button")
        frame.click()

        # Multiple elements
        rows = page.locator("tr")
        for i in range(await rows.count()):
            cell = rows.nth(i).locator("td").first
            print(await cell.text_content())
    '''

def get_assertion_examples():
    return '''
        from playwright.sync_api import expect

        # Element state assertions
        expect(page.get_by_role("button")).to_be_visible()
        expect(page.locator("#loading")).to_be_hidden()
        expect(page.get_by_label("Email")).to_be_enabled()
        expect(page.locator("#terms")).to_be_checked()

        # Content assertions
        expect(page.locator("h1")).to_have_text("Welcome")
        expect(page.get_by_role("alert")).to_contain_text("Success")
        expect(page.locator("img")).to_have_attribute("alt", "Logo")

        # Count assertions
        expect(page.locator("li")).to_have_count(5)
        expect(page.get_by_role("link")).to_have_count(3)

        # Screenshot comparison
        expect(page).to_have_screenshot("baseline.png")
    '''

def get_advanced_features():
    return '''
        # Network interception
        def handle_route(route):
            if route.request.resource_type == "image":
                return route.abort()
            return route.continue_()
        
        page.route("**/*", handle_route)

        # Mobile emulation
        iphone = playwright.devices['iPhone 12']
        context = browser.new_context(**iphone)
        page = context.new_page()

        # Geolocation
        context = browser.new_context(
            geolocation={"latitude": 51.5074, "longitude": -0.1278}
        )
        page.goto("https://maps.google.com")

        # Authentication
        context = browser.new_context(
            storage_state={
                "cookies": [{
                    "name": "session",
                    "value": "123456",
                    "domain": "example.com",
                    "path": "/"
                }]
            }
        )
    '''

def get_test_patterns():
    return '''
        # Page Object Model
        class LoginPage:
            def __init__(self, page: Page):
                self.page = page
                self.username = page.get_by_label("Username")
                self.password = page.get_by_label("Password")
                self.submit = page.get_by_role("button", name="Login")
            
            def login(self, username: str, password: str):
                self.username.fill(username)
                self.password.fill(password)
                self.submit.click()
                expect(page).to_have_url("/dashboard")

        # Test data management
        import json
        from pathlib import Path

        def load_test_data():
            data_file = Path(__file__).parent / "test_data.json"
            return json.loads(data_file.read_text())

        # Error handling
        def safe_click(page: Page, selector: str, timeout=5000):
            try:
                page.wait_for_selector(selector, timeout=timeout)
                page.locator(selector).click()
            except TimeoutError:
                page.screenshot(path="error.png")
                raise
    '''

def get_key_takeaways():
    return '''
        # 1. Browser Control
        page.goto(url)              # Navigation
        page.locator(selector)      # Find elements
        expect(locator).to_*        # Assertions

        # 2. Selectors
        .locator("css")            # CSS selector
        .get_by_role("button")     # Role selector
        .get_by_text("Click")      # Text content

        # 3. Actions
        .click()                   # Click element
        .fill("text")             # Enter text
        .press("Enter")           # Press key

        # 4. Testing
        @pytest.fixture           # Setup/teardown
        expect(locator).to_*      # Assertions
        page.screenshot()         # Debugging
    '''

@describe("Interactive Playwright with Pytest")
class TestPlaywrightBasicsInteractive:
    
    @it("teaches about browser automation basics")
    def test_browser_basics(self):
        print_section_header("Welcome to Playwright Integration - Part 1: Browser Basics")
        print_info("Let's explore Playwright's browser automation capabilities.")
        time.sleep(1)

        # Question 1: Browser Control
        print_subsection_header("Question 1: Browser Control")
        print_instruction("Look at these browser automation examples:")
        print_code_block(get_browser_basics())
        answer = get_user_input("What Playwright assertion method is used to verify page title?")
        check_answer(
            answer,
            ['to_have_title', 'expect(page).to_have_title'],
            "expect(page).to_have_title() is used to verify the page's title."
        )

        # Question 2: Element Location
        print_subsection_header("Question 2: Element Location")
        print_instruction("Look at the form submission example:")
        answer = get_user_input("What selector method is recommended for finding form elements by their label text?")
        check_answer(
            answer,
            ['get_by_label', 'page.get_by_label'],
            "get_by_label() is recommended for finding form elements using their associated label text."
        )

        # Question 3: Dynamic Content
        print_subsection_header("Question 3: Dynamic Content")
        print_instruction("Look at the dynamic content example:")
        answer = get_user_input("What wait method ensures all network requests are complete?")
        check_answer(
            answer,
            ['wait_for_load_state', 'page.wait_for_load_state'],
            "wait_for_load_state('networkidle') waits for all network requests to complete."
        )

    @it("teaches about selectors")
    def test_selectors(self):
        print_section_header("Part 2: Selectors")
        print_info("Let's learn about Playwright's powerful selector system.")
        time.sleep(1)

        # Question 1: Selector Types
        print_subsection_header("Question 1: Selector Types")
        print_instruction("Look at these selector examples:")
        print_code_block(get_selector_examples())
        answer = get_user_input("What method is used to find elements by their ARIA role and name?")
        check_answer(
            answer,
            ['get_by_role', 'page.get_by_role'],
            "get_by_role() is used to find elements by their ARIA role and name attributes."
        )

    @it("teaches about page interactions")
    def test_interactions(self):
        print_section_header("Part 3: Page Interactions")
        print_info("Let's explore interacting with page elements.")
        time.sleep(1)

        # Question 1: Form Interactions
        print_subsection_header("Question 1: Form Interactions")
        print_instruction("Look at these interaction examples:")
        print_code_block(get_interaction_examples())
        answer = get_user_input("What method is used to enter text into form fields?")
        check_answer(
            answer,
            ['fill', '.fill'],
            "The .fill() method is used to enter text into form fields."
        )

    @it("teaches about assertions")
    def test_assertions(self):
        print_section_header("Part 4: Assertions")
        print_info("Let's learn about Playwright's assertion system.")
        time.sleep(1)

        # Question 1: Expect API
        print_subsection_header("Question 1: Expect API")
        print_instruction("Look at these assertion examples:")
        print_code_block(get_assertion_examples())
        answer = get_user_input("What is the main function used for Playwright assertions?")
        check_answer(
            answer,
            ['expect', 'expect()'],
            "expect() is used for making assertions about page elements and state."
        )

    @it("teaches about advanced features")
    def test_advanced(self):
        print_section_header("Part 5: Advanced Features")
        print_info("Let's explore Playwright's advanced features.")
        time.sleep(1)

        # Question 1: Network Interception
        print_subsection_header("Question 1: Network Interception")
        print_instruction("Look at these advanced feature examples:")
        print_code_block(get_advanced_features())
        answer = get_user_input("What method is used to intercept network requests?")
        check_answer(
            answer,
            ['route', 'page.route'],
            "page.route() is used to intercept and modify network requests."
        )

    @it("teaches about test patterns")
    def test_patterns(self):
        print_section_header("Part 6: Test Patterns")
        print_info("Let's learn about Playwright test patterns and best practices.")
        time.sleep(1)

        # Question 1: Page Object Model
        print_subsection_header("Question 1: Page Object Model")
        print_instruction("Look at these test pattern examples:")
        print_code_block(get_test_patterns())
        answer = get_user_input("What design pattern encapsulates page interactions into a class?")
        check_answer(
            answer,
            ['page object model', 'page object pattern', 'pom'],
            "The Page Object Model pattern encapsulates page interactions into reusable classes."
        )

        print_success("🎉 Congratulations! You've completed the Playwright Integration lesson!")
        print_info("Key takeaways:")
        print_code_block(get_key_takeaways()) 