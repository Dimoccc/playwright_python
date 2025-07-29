import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

def test_drag_and_drop(page):
    page.goto('https://zimaev.github.io/draganddrop/')
    page.drag_and_drop("#drag", "#drop")