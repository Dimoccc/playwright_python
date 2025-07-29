import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

def test_mock_tags(page):
    page.route("**/api/tags", lambda route: route.fulfill(path="./data/data.json"))
    page.goto('https://demo.realworld.io/')

def test_intercepted(page):
    def handle_route(route):
        response = route.fetch()
        json = response.json()
        json["tags"] = ["open", "solutions"]
        route.fulfill(json=json)

    page.route("**/api/tags", handle_route)

    page.goto("https://demo.realworld.io/")
    sidebar = page.locator('css=div.sidebar') 
    expect(sidebar.get_by_role('link')).to_contain_text(["open", "solutions"])