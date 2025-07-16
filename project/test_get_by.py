import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

def test_get_by(page):
    page.goto("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login", timeout=60000)
    page.get_by_text("Customer Login").click()
    page.get_by_label("Your Name")
    text = page.locator("text=Your Name :").inner_text()
    label = page.locator("//label[contains(., 'Your Name')]").text_content()
    print(text)  
    print(label)
    page.locator('//div/select[@id="userSelect"]').click()
    #page.get_by_alt_text('logo').click()
    #page.get_by_title("username").fill("Anton")
    #page.get_by_role("button", name="Submit").click()

def test_login(page):
    page.goto('https://zimaev.github.io/text_input/')
    page.get_by_label("Email address").fill("qa@example.com")
    page.get_by_title("username").fill("Anton")
    page.get_by_placeholder('password').fill("secret")
    page.get_by_role('checkbox').click()

def test_locator_and(page):
    page.goto("https://zimaev.github.io/locatorand/")
    selector = page.get_by_role("button", name="Sing up").and_(page.get_by_title("Sing up today"))
    selector.click()

def test_filter(page):
    page.goto("https://zimaev.github.io/filter/")
    row_locator = page.locator("tr")
    row_locator.filter(has_text="text in column 1").filter(has=page.get_by_role("button", name="column 2 button")).click()

def test_click_all_checkbox(page):
    # Через цикл
    # page.goto('https://zimaev.github.io/checks-radios/') 
    # checkbox = page.locator("input")
    # for i in range(checkbox.count()):
    #     checkbox.nth(i).click()
    
    # Через checkboxes.all()
    page.goto('https://zimaev.github.io/checks-radios/')
    checkboxes = page.locator("input")
    for checkbox in checkboxes.all():
        checkbox.check()