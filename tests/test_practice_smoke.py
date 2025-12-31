# tests/test_practice_smoke.py
import pytest
from flows.practice_flows import PracticeFlows

@pytest.mark.smoke
def test_journey_autocomplete_select_country(practice_page):
    practice_page.open()
    flow = PracticeFlows(practice_page)
    # Journey flow: multi-step + wait-sensitive
    flow.select_country_and_verify(keyword="Sin", expected_country="Singapore")


@pytest.mark.smoke
def test_journey_toggle_show_hide(practice_page):
    practice_page.open()
    flow = PracticeFlows(practice_page)

    # Journey flow: UI state transition + assertions
    flow.toggle_textbox_visibility_and_verify()


@pytest.mark.smoke
def test_component_dropdown_simple(practice_page):
    practice_page.open()

    # Component direct call: single-step interaction doesn't need a flow
    practice_page.dropdown.select_by_value("option2")
    assert practice_page.dropdown.selected_text() == "Option2"


@pytest.mark.smoke
def test_component_web_table_total_simple(practice_page):
    practice_page.open()

    # Component direct call: computation assertion is clear at test level
    amounts = practice_page.web_table.fixed_table_amounts()
    assert sum(amounts) == practice_page.web_table.displayed_total()


@pytest.mark.smoke
def test_journey_open_tab_and_return(practice_page):
    practice_page.open()
    flow = PracticeFlows(practice_page)

    # Journey flow: window/tab switching is a classic place to abstract
    flow.open_tab_and_return_to_practice_page(expected_title_contains="Practice Page")
