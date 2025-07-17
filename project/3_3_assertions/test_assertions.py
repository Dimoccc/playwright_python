# Тест проверки заполнения формы

# открыть https://demo.playwright.dev/todomvc/#/
# проверить что открыт корректный url
# найти поле ввода задачи
# проверить что оно пустое
# ввести задачу номер один
# ввести задачу номер два
# проверить что количество задач в списке равно двум
# отметить одну задачу выполненной
# проверить что эта задача отмечена выполненной

import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

def test_assertions(page):
    page.goto('https://demo.playwright.dev/todomvc/#/')
    expect(page).to_have_url('https://demo.playwright.dev/todomvc/#/')
    # input_field = page.get_by_placeholder('What needs to be done?')
    input_field = page.locator("//div//input[@class='new-todo']")
    expect(input_field).to_be_empty()
    input_field.fill("Первая задача")
    input_field.press('Enter')
    input_field.fill("Вторая задача")
    input_field.press('Enter')
    todo_item = page.get_by_test_id('todo-item')
    expect(todo_item).to_have_count(2)
    todo_item.get_by_role('checkbox').nth(0).click()
    expect(todo_item.nth(0)).to_have_class('completed')
    page.locator("//div//li[1]//button[@class='destroy']").click() # бонусный шаг от меня - удаления первой записи
    expect(todo_item).to_have_count(1) # проверка что осталась 1 запись
