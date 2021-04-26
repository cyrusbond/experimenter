from nimbus.pages.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BranchesPage(Base):
    """Experiment Branches Page."""

    _reference_branch_name_locator = (By.CSS_SELECTOR, "#referenceBranch-name")
    _reference_branch_description_locator = (
        By.CSS_SELECTOR,
        "#referenceBranch-description",
    )
    _remove_branch_locator = (By.CSS_SELECTOR, ".bg-transparent")
    _add_feature_locator = (By.CSS_SELECTOR, ".feature-config-add")
    _page_wait_locator = (By.CSS_SELECTOR, "#PageEditBranches")
    _save_continue_btn_locator = (By.CSS_SELECTOR, "#save-and-continue-button")

    def wait_for_page_to_load(self):
        self.wait.until(EC.presence_of_element_located(self._page_wait_locator))

        return self

    def save_and_continue(self):
        element = self.selenium.find_element(*self._save_continue_btn_locator)
        element.click()
        from nimbus.pages.metrics import MetricsPage

        return MetricsPage(self.driver, self.base_url).wait_for_page_to_load()

    @property
    def reference_branch_name(self):
        return self.find_element(*self._reference_branch_name_locator).text

    @reference_branch_name.setter
    def reference_branch_name(self, text=None):
        name = self.find_element(*self._reference_branch_name_locator)
        name.send_keys(f"{text}")

    @property
    def reference_branch_description(self):
        return self.find_element(*self._reference_branch_description_locator).text

    @reference_branch_description.setter
    def reference_branch_description(self, text=None):
        name = self.find_element(*self._reference_branch_description_locator)
        name.send_keys(f"{text}")

    def remove_branch(self):
        el = self.find_element(*self._remove_branch_locator)
        el.click()

    def select_feature(self):
        el = self.find_element(*self._add_feature_locator)
        el.click()
