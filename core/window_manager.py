# src/core/window_manager.py
class WindowManager:
    def __init__(self, driver):
        self.driver = driver

    def current_handle(self) -> str:
        return self.driver.current_window_handle

    def handles(self) -> list[str]:
        return self.driver.window_handles

    def switch_to_newest(self):
        self.driver.switch_to.window(self.handles()[-1])

    def switch_to(self, handle: str):
        self.driver.switch_to.window(handle)

    def close_current_and_back(self, original_handle: str):
        self.driver.close()
        self.driver.switch_to.window(original_handle)
