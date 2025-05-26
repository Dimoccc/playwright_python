import pytest

from playwright.sync_api import Playwright, sync_playwright, expect


# Пропустить тест браузером
# import pytest

# @pytest.mark.skip_browser("firefox")
# def test_visit_example(page):
#     page.goto("https://example.com")
#     # ...
 
# Запуск в определенном браузере
# @pytest.mark.only_browser("chromium")
# def test_visit_example(page):
#     page.goto("https://example.com")
#     # ...

def test_add_todo(page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    page.get_by_placeholder("What needs to be done?").press("Enter")
