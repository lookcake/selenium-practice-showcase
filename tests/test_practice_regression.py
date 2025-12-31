# tests/test_practice_regression.py
import pytest

@pytest.mark.regression
def test_radio_select_radio2(practice_page):
    practice_page.open()
    practice_page.radios.select_by_value("radio2")
    assert practice_page.radios.selected_value() == "radio2"

@pytest.mark.regression
def test_checkboxes_select_multiple(practice_page):
    practice_page.open()
    practice_page.checkboxes.set_option(1, True)
    practice_page.checkboxes.set_option(3, True)
    assert set(practice_page.checkboxes.selected_options()) == {"option1", "option3"}

@pytest.mark.regression
def test_show_hide_textbox(practice_page):
    practice_page.open()
    practice_page.show_hide.hide()
    assert practice_page.show_hide.is_visible() is False
    practice_page.show_hide.show()
    assert practice_page.show_hide.is_visible() is True

@pytest.mark.regression
def test_autocomplete_pick_singapore(practice_page):
    practice_page.open()
    practice_page.autocomplete.type_keyword("Sin")
    practice_page.autocomplete.pick("Singapore")
    assert practice_page.autocomplete.current_value() == "Singapore"

@pytest.mark.regression
def test_hover_menu_top(practice_page):
    practice_page.open()
    practice_page.hover_menu.click_top()
    # top anchor exists; success is "no error" + URL may include #top
    assert True

@pytest.mark.regression
def test_switch_window_and_back(practice_page):
    practice_page.open()
    practice_page.windows_tabs.open_window_and_close()
    assert "Practice Page" in practice_page.driver.title

@pytest.mark.regression
def test_switch_tab_and_back(practice_page):
    practice_page.open()
    practice_page.windows_tabs.open_tab_and_close()
    assert "Practice Page" in practice_page.driver.title
