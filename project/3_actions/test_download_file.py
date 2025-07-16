import pytest, os

from playwright.sync_api import Playwright, sync_playwright, expect

@pytest.mark.xfail(reason="Не работает через обработчик событий dowload")
def test_on_download(page):
    page.goto("https://demoqa.com/upload-download")
    page.on("download", lambda download: print(download.path()))
    page.locator('xpath=//*[@id="downloadButton"]').click()

def test_expect_download(page):
    # page.set_default_timeout(60000)  
    page.goto("https://demoqa.com/upload-download", wait_until="domcontentloaded")

    with page.expect_download() as download_info:
        page.locator("a:has-text(\"Download\")").click()

    download = download_info.value
    file_name = download.suggested_filename
    destination_folder_path = "./data/"
    download.save_as(os.path.join(destination_folder_path, file_name))
