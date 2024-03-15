from PageObjects.TaskPage import TaskPage
from PageObjects.TaskDBPage import TaskDbPage
import constants
import time
import pytest

"""

Create/Edit/View/Delete Tasks in Projects

TaskDB Scenarios

"""
@pytest.mark.taskPositive
def test_create_view_edit_delete_task():

    #LOGIN
    user = TaskPage()
    user.user_login("nick@email.gr","password",constants.URL)
    time.sleep(3)

    #CREATE PROJECT
    user.create_project("Automate Task Page", "Project to automate the Task Page")
    time.sleep(3)

    #ADD TASK
    user.add_task()
    user.enter_summary("Selenium Locators")

    user.enter_task_description("Find the suitable Locators")
    user.status_dropdown()
    user.select_task_status("to do")
    time.sleep(3)
    user.select_task_labels("backend","frontend")
    time.sleep(3)
    user.file_upload("test.png")
    time.sleep(3)
    user.submit_button()
    time.sleep(2)

    tasks = user.get_all_tasks()

    assert len(tasks) != 0

    #EDIT TASK
    time.sleep(3)
    to_do_task = user.get_all_to_do_tasks()
    task_id= to_do_task[0].get_attribute("id")
    user.edit_task(task_id)
    time.sleep(3)
    user.status_dropdown()
    user.select_task_status("in review")
    time.sleep(3)
    user.select_task_labels("ci","jenkins")
    time.sleep(3)
    user.submit_button()
    time.sleep(2)

    updated_task = user.get_all_in_review_tasks()[0]
    in_review_tasks=user.get_all_in_review_tasks()
    assert "ci","jenkins" in updated_task.text and len(in_review_tasks) == 1

    #DELETE TASK
    print("Delete Task")
    user.delete_task(task_id)
    time.sleep(3)

    updated_in_review_tasks = user.get_all_in_review_tasks()
    assert len(updated_in_review_tasks) == 0

    #DELETE PROJECT
    user.navigate_to_dashboard()
    user.delete_project()
    time.sleep(2)

    message = user.successful_page_landing()
    assert "There are no projects created yet" in message

    user.logout()

    time.sleep(2)

@pytest.mark.taskNegative
def test_create_edit_task_negative():
    #LOGIN
    user = TaskPage()
    user.user_login("nick@email.gr","password",constants.URL)
    time.sleep(3)

    #CREATE PROJECT
    user.create_project("Automate Task Page", "Project to automate the Task Page")
    time.sleep(3)

    user.add_task()
    user.enter_summary("Negative Automation")

    #user.enter_task_description("Find the suitable Locators")
    user.status_dropdown()
    user.select_task_status("to do")
    time.sleep(3)
    user.select_task_labels("backend", "frontend")
    time.sleep(3)
    user.file_upload("test.png")
    time.sleep(3)
    user.submit_button()
    time.sleep(3)

    message = user.get_validation_task_msg()

    assert message == "This field is required"

    user.logout()


@pytest.mark.ScenarioTaskDB1
@pytest.mark.parametrize("project_name,project_summary,project_number,expected_taskdbitems,summary,description,status,labels,file", [
    ("Project1", "Summary1",0,1,"Python Auto", "A priority","to do","performance","test.xlsx"),
    ("Project2", "Summary2",1,2,"Web Scraping","B priority","in progress","frontend","test.png"),
    ("Project3", "Summary3",2,3,"Design Mockups", "C priority","in review","design","test.xlsx"),
    ("Project4", "Summary4",3,4,"Test Design", "D priority","done","testing","test.txt")])
def test_add_multiple_projects_tasks(project_name,project_summary,project_number,expected_taskdbitems,summary,description,status,labels,file):
    """
    This Scenario creates multiple projects and one task for each project.
    After checks if the total number of tasks is equal to the displayed tasks in TaskDB at the current time

    """
    #LOGIN
    user = TaskDbPage()
    user.user_login("nick@email.gr", "password", constants.URL)
    time.sleep(3)

    # CREATE PROJECT
    user.create_project(project_name,project_summary)
    time.sleep(3)

    # ADD TASK
    user.add_task(project_number)
    user.enter_summary(summary)

    user.enter_task_description(description)
    user.status_dropdown()
    user.select_task_status(status)
    time.sleep(3)
    user.select_task_labels(labels)
    time.sleep(3)
    user.file_upload(file)
    time.sleep(3)
    user.submit_button()
    time.sleep(3)

    #CHECK TASKDB
    user.navigate_to_task_db()
    time.sleep(3)
    tasks = user.get_all_taskdb_items()
    time.sleep(3)

    assert len(tasks) == expected_taskdbitems, "The TaskDB is not aligned with project Tasks! Either task is not created or TaskDB not updated correctly"

@pytest.mark.ScenarioTaskDB2
def test_search_sort_taskDB():
    """
     This Scenario takes projects/tasks from ScenarioTaskDB1 and checks
     the sorting on TaskDB tab and the search bar

     """

    user = TaskDbPage()
    user.user_login("nick@email.gr", "password", constants.URL)
    time.sleep(3)

    user.navigate_to_task_db()
    time.sleep(3)
    #CHECK SORTING
    user.sort_by_summary()
    taskdb_items= user.get_all_taskdb_items()

    assert "Design Mockups" in taskdb_items[0].text, "Cannot find the requested Task"

    user.search_for_task("Python Auto")
    time.sleep(3)

    sorted_task = user.get_sorted_task()

    assert "Python Auto" in sorted_task.text, "Cannot find the requested Task"

    #DELETE ALL PROJECTS
    user.navigate_to_dashboard()

    projects = user.get_all_projects()

    for project in range(len(projects)):
        user.delete_project()
        time.sleep(3)


