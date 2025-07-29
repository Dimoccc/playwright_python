import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

def test_screenshot(page):
    page.goto('https://zimaev.github.io/draganddrop/')
    page.screenshot(path="./data/screenshot.png")# сменить формат скрина page.screenshot(path="example.jpeg", type="jpeg")
    page.screenshot(path="./data/full_screenshot.png", full_page=True)
    page.locator("#drop").screenshot(path="./data/drop_screenshot.png")
    #page.screenshot(path="example.jpeg", type="jpeg", quality=80) #смена качества quality
    #page.screenshot(path="clipped_image.png", clip={"x": 50, "y": 0, "width": 400, "height": 300}) # скриншот области
    # page.screenshot(path="transparent_background.png", omit_background=True) # скриншот без фона 
    # page.screenshot(path="timeout_example.png", timeout=10000) # задание задержки 