from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from PageObjects.LoginPage import LoginPage
import time

DELETE_POP_UP = "Are you sure you want to delete this project?"  #to put on conf file with constants and import

class DashBoardPage(LoginPage):

    DASHBOARD = (By.ID, "dashboard")
    TASK_DB = (By.ID, "task_db")
    SETTINGS = (By.ID, "settings")
    LOGOUT = (By.ID, "logout")

    CREATE_BTN = (By.CSS_SELECTOR, "a[href='/createProject']")

    NAME_FORM = (By.XPATH, "//*[@id='name']")
    DESC_FORM = (By.CSS_SELECTOR, "input[id='description']")
    SUBMIT_BTN = (By.CSS_SELECTOR,"button[name='action']")

    PROJECTS = (By.CLASS_NAME, "card-title")
    ADD_TASK = (By.XPATH, "(//*[@id='btn_add_task'])")
    VIEW_TASKS = (By.XPATH, "(//*[@id='btn_view_tasks'])")
    EDIT_PROJECT = (By.XPATH, "(//*[@id='btn_update_project'])")
    DELETE_PROJECT = (By.XPATH, "(//*[@id='delete_project'])")

    INVALID_MESSAGE_PROJECT_NAME = (By.XPATH, "//*[@id='root']/div/div/div/form/div[1]/div/p")
    INVALID_MESSAGE_PROJECT_DESC = (By.XPATH, "//*[@id='root']/div/div/div/form/div[2]/div/p")




    def __init__(self):
        super().__init__()

    def create_project_btn_click(self):
        self.wait_for(self.CREATE_BTN)
        self.find_element(self.CREATE_BTN).click()

    def navigate_to_task_db(self):
        self.find_element(self.TASK_DB).click()

    def navigate_to_settings(self):
        self.find_element(self.SETTINGS).click()

    def navigate_to_dashboard(self):
        self.find_element(self.DASHBOARD).click()

    def logout(self):
        self.find_element(self.LOGOUT).click()

    def enter_project_name(self,project_name):
        self.wait_for(self.NAME_FORM)
        self.find_element(self.NAME_FORM).clear()
        self.find_element(self.NAME_FORM).send_keys(project_name)

    def enter_project_description(self,description_name):
        self.wait_for(self.DESC_FORM)
        self.find_element(self.DESC_FORM).clear()
        self.find_element(self.DESC_FORM).send_keys(description_name)

    def submit_button(self):
        self.find_element(self.SUBMIT_BTN).click()

    def get_all_projects(self):
        if self.find_element(self.PM_BOX).text == "Welcome!":
            return "No projects yet implemented, please create your first one"
        else:
             projects = self.driver.find_elements(*self.PROJECTS)
             return projects
    def get_all_projects_text(self):
        projects_text = []
        projects = self.driver.find_elements(*self.PROJECTS)
        for project in projects:
            projects_text.append(project.text)
        return  projects_text

    def create_project(self,name,desc):
        self.create_project_btn_click()
        self.enter_project_name(name)
        self.enter_project_description(desc)
        self.submit_button()

    def add_task(self, project_index=0):
        self.wait_for(self.ADD_TASK)
        self.driver.find_element(By.XPATH, f"({self.ADD_TASK[1]})[{project_index+1}]").click()

    def view_tasks(self, project_index=0):
        self.wait_for(self.VIEW_TASKS)
        self.driver.find_element(By.XPATH, f"({self.VIEW_TASKS[1]})[{project_index+1}]").click()

    def edit_project(self, project_index=0):
        self.wait_for(self.EDIT_PROJECT)
        self.driver.find_element(By.XPATH, f"({self.EDIT_PROJECT[1]})[{project_index+1}]").click()

    def delete_project(self, project_index=0):
        self.wait_for(self.DELETE_PROJECT)
        self.driver.find_element(By.XPATH, f"({self.DELETE_PROJECT[1]})[{project_index+1}]").click()
        try:
             self.wait.until(EC.alert_is_present())
             alert = self.driver.switch_to.alert
             if DELETE_POP_UP in alert.text:
                 print(f'Clicking "YES" to "{alert.text}"')
                 time.sleep(2)
                 alert.accept()
             else:
                 alert.dismiss()
        except NoAlertPresentException:
            print("Wrong or No alert popped up")

    def get_validation_project_name_msg(self):
        self.wait_for(self.INVALID_MESSAGE_PROJECT_NAME)
        return self.find_element(self.INVALID_MESSAGE_PROJECT_NAME).text

    def get_validation_project_desc_msg(self):
        self.wait_for(self.INVALID_MESSAGE_PROJECT_DESC)
        return self.find_element(self.INVALID_MESSAGE_PROJECT_DESC).text



