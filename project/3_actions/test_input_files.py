import pytest

from playwright.sync_api import Playwright, sync_playwright, expect

def test_set_input_files(page):
    page.goto('https://zimaev.github.io/upload/')
    page.set_input_files("#formFile", "project/3_actions/hello.txt")
    page.locator("#file-submit").click()

def test_filechooser_input(page):
    page.goto('https://zimaev.github.io/upload/')
    page.on("filechooser", lambda file_chooser: file_chooser.set_files("project/3_actions/hello.txt"))
    page.locator("#formFile").click()
    page.locator("#formFileLg").click()

def test_with_input(page):
    page.goto('https://zimaev.github.io/upload/')
    with page.expect_file_chooser() as fc_info:
        page.locator("#formFile").click()
    file_chooser = fc_info.value
    file_chooser.set_files("hello.txt")