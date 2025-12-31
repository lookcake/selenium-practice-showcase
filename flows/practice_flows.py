# src/flows/practice_flows.py

class PracticeFlows:

    def __init__(self, practice_page):
        self.page = practice_page

    # Journey Flow 1: Autocomplete end-to-end selection + assertion
    def select_country_and_verify(self, keyword: str, expected_country: str) -> None:
        """
        Steps:
        1) Type keyword into autocomplete
        2) Pick expected country from suggestion list
        3) Verify input value
        """
        self.page.autocomplete.type_keyword(keyword)
        self.page.autocomplete.pick(expected_country)

        actual = self.page.autocomplete.current_value()
        assert actual == expected_country, f"Autocomplete value mismatch. expected={expected_country}, actual={actual}"

    # Journey Flow 2: Toggle visibility + assertions
    def toggle_textbox_visibility_and_verify(self) -> None:
        """
        Steps:
        1) Hide textbox
        2) Verify textbox not visible
        3) Show textbox
        4) Verify textbox visible
        """
        self.page.show_hide.hide()
        assert self.page.show_hide.is_visible() is False, "Textbox should be hidden after clicking Hide."

        self.page.show_hide.show()
        assert self.page.show_hide.is_visible() is True, "Textbox should be visible after clicking Show."

    # Journey Flow 3: Open tab and return (window handle management) + assertion
    def open_tab_and_return_to_practice_page(self, expected_title_contains: str = "Practice Page") -> None:
        """
        Steps:
        1) Open new tab
        2) Switch to newest tab and assert we are there
        3) Close current tab
        4) Switch back and assert we returned to Practice Page
        """
        self.page.windows_tabs.open_tab_and_close()
        assert expected_title_contains in self.page.driver.title, (
            f"Did not return to expected page. title={self.page.driver.title}"
        )
