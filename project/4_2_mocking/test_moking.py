import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

def test_listen_network(page):
    page.on("request", lambda request: print(">>", request.method, request.url))
    page.on("response", lambda response: print("<<", response.status, response.url))
    page.goto('https://osinit.ru/')

def test_route_picture(page):
    page.route("**/*.{png,jpg,jpeg}", lambda route: route.abort())
    page.goto('https://osinit.ru/')