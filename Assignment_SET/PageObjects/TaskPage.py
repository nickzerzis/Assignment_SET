from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from PageObjects.DashboardPage import DashBoardPage
import time
import os

STATUSES = {"TO DO":1, "IN PROGRESS":2, "IN REVIEW":3, "DONE":4}
DELETE_POP_UP_TASK = "Are you sure you want to delete this task?"

class TaskPage(DashBoardPage):

    SUMMARY = (By.ID, "summary")
    DESCRIPTION = (By.ID, "description")
    STATUS_DROP = (By.XPATH,"//*[@class='select-wrapper']")
    SELECT_STATUS = (By.XPATH, "//*[@class='select-wrapper']/ul/li")
    SELECT_DROP = (By.XPATH, "//*[@id='search_input']")
    SELECT_LABEL = (By.XPATH,"//*[@id='multiselectContainerReact']/div[2]/ul/li[1]")
    FILE_UPLOAD = (By.XPATH, "//*[@id='attachments']")

    TASK_PRESENT = (By.XPATH,"//*[@id='card_title']")

    ALL_TASKS =(By.XPATH,"//*[@id='items']/div")
    TO_DO_TASKS= (By.XPATH,"//*[@id='to_do_items']/div")
    IN_PROGRESS_TASKS = (By.XPATH,"//*[@id='in_progress_items']/div")
    IN_REVIEW_TASKS = (By.XPATH, "//*[@id='in_review_items']/div")
    DONE_TASKS = (By.XPATH, "//*[@id='done_items']/div")
    BODY =(By.XPATH,"//*[@id='root']/div")

    INVALID_MESSAGE_TASK = (By.XPATH, "//*[@id='root']/div/div/div/form/div[2]/div/p")



    def __init__(self):
        super().__init__()

    def enter_summary(self, summary):
        self.wait_for(self.SUMMARY)
        self.find_element(self.SUMMARY).clear()
        self.find_element(self.SUMMARY).send_keys(summary)

    def enter_task_description(self, task_description):
        self.wait_for(self.DESCRIPTION)
        self.find_element(self.DESCRIPTION).clear()
        self.find_element(self.DESCRIPTION).send_keys(task_description)

    def status_dropdown(self):
        self.wait_for(self.STATUS_DROP)
        self.find_element(self.STATUS_DROP).click()

    def select_task_status(self, status="to do"):
        self.wait_for(self.SELECT_STATUS)
        real_status = status.strip().upper()
        if real_status in STATUSES.keys():
           self.driver.find_element(By.XPATH, f"({self.SELECT_STATUS[1]})[{STATUSES[real_status]}]").click()
        else:
            raise ValueError ("Please fill in a correct task status")

    def select_task_labels(self, *argv):
        self.wait_for(self.SELECT_DROP)
        try:
            for arg in argv:
                self.find_element(self.SELECT_DROP).send_keys(arg)
                self.wait_for(self.SELECT_LABEL)
                self.find_element(self.SELECT_LABEL).click()
                time.sleep(5)
            self.find_element(self.BODY).click()
        except:
            raise ValueError ("The label does not exist")

    def file_upload(self,filename):#bug on file upload in .txt
        file= self.find_element(self.FILE_UPLOAD)
        cwd = os.getcwd()
        file.send_keys(rf"{cwd}\files_to_upload\{filename}")

    def get_all_tasks(self):
        all_tasks = self.driver.find_elements(*self.ALL_TASKS)
        return all_tasks

    def get_task(self):
        task = self.driver.find_element(*self.ALL_TASKS)
        return task

    def get_all_to_do_tasks(self):
        to_do_tasks = self.driver.find_elements(*self.TO_DO_TASKS)
        return to_do_tasks

    def get_all_in_progress_tasks(self):
        in_progress_tasks = self.driver.find_elements(*self.IN_PROGRESS_TASKS)
        return in_progress_tasks

    def get_all_in_review_tasks(self):
        review_tasks = self.driver.find_elements(*self.IN_REVIEW_TASKS)
        return review_tasks

    def get_all_done_tasks(self):
        done_tasks = self.driver.find_elements(*self.DONE_TASKS)
        return done_tasks

    def edit_task(self, id):
        self.wait_for(self.TASK_PRESENT)
        self.driver.find_element(By.XPATH, f"//*[@id='{id}']/div[2]/a[1]").click()

    def delete_task(self, id):
        self.wait_for(self.TASK_PRESENT)
        self.driver.find_element(By.XPATH, f"//*[@id='{id}']/div[2]/a[2]").click()
        try:
             self.wait.until(EC.alert_is_present())
             alert = self.driver.switch_to.alert
             if DELETE_POP_UP_TASK in alert.text:
                 print(f'Clicking "YES" to "{alert.text}"')
                 time.sleep(2)
                 alert.accept()
             else:
                 alert.dismiss()
        except NoAlertPresentException:
            print("Wrong or No alert popped up")

    def get_validation_task_msg(self):
        self.wait_for(self.INVALID_MESSAGE_TASK)
        return self.find_element(self.INVALID_MESSAGE_TASK).text


