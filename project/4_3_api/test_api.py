import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

def test_inventory(page):
    response = page.request.get('https://petstore.swagger.io/v2/store/inventory')
    print(response.status)
    print(response.json())