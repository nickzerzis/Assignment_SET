from selenium.webdriver.common.by import By
from PageObjects.TaskPage import TaskPage


class TaskDbPage(TaskPage):

    TASK_DB_PRESENT = (By.XPATH, "//*[@id='card_title']")
    ALL_DB_TASKS = (By.XPATH, "//*[@id='items']/div[1]/div")
    SORT_BY_SUMMARY = (By.ID, "sort_tasks")
    SEARCH_BAR = (By.CSS_SELECTOR, "#search")
    SORTED_TASK = (By.XPATH, "//*[@id='card_title']")

    def __init__(self):
        super().__init__()

    def get_all_taskdb_items(self):
        all_db_tasks = self.driver.find_elements(*self.ALL_DB_TASKS)
        return all_db_tasks

    def sort_by_summary(self):
        self.find_element(self.SORT_BY_SUMMARY).click()

    def search_for_task(self, task):
        self.wait_for(self.TASK_DB_PRESENT)
        self.find_element(self.SEARCH_BAR).send_keys(task)

    def get_sorted_task(self):
        return self.find_element(self.SORTED_TASK)

