from PageObjects.DashboardPage import DashBoardPage
import pytest
import constants
import time

"""

Create/Edit/View/Delete Projects in Dashboard's PM Tool

"""
@pytest.mark.dash
@pytest.mark.parametrize("project_name,description", [("Dashboard QA Automation", "Project for Automating the Dashboard page in the PM tool")])
def test_create_view_edit_delete_project(project_name,description):
    #LOGIN
    user = DashBoardPage()
    user.user_login("nick@email.gr","password",constants.URL)
    time.sleep(3)

    #CREATE/VIEW PROJECT
    user.create_project_btn_click()
    user.enter_project_name(project_name)
    user.enter_project_description(description)
    user.submit_button()
    time.sleep(3)
    projects_text = user.get_all_projects_text()

    assert  project_name in projects_text

    #EDIT PROJECT
    new_name = f"Version2 of {project_name}"
    user.edit_project()
    time.sleep(3)
    user.enter_project_name(new_name)
    time.sleep(3)
    user.submit_button()
    time.sleep(3)
    updated_projects_text = user.get_all_projects_text()

    assert new_name in updated_projects_text, "Name is not updated correctly"

    #DELETE PROJECT
    user.delete_project()
    time.sleep(2)
    updated_dashboard = user.get_all_projects_text()

    assert new_name not in updated_dashboard, "Name is not updated correctly"


@pytest.mark.dashNegative
def test_create_project_negative():

    # LOGIN
    user = DashBoardPage()
    user.user_login("nick@email.gr", "password", constants.URL)
    time.sleep(3)

    # TRY TO CREATE PROJECT NO NAME
    user.create_project_btn_click()
    user.enter_project_description("Test Negative")
    user.submit_button()
    time.sleep(3)


    desc_message = user.get_validation_project_name_msg()

    assert desc_message == "This field is required"

    time.sleep(3)

    user.navigate_to_dashboard()

    #TRY TO CREATE PROJECT NO DESC
    user.create_project_btn_click()
    user.enter_project_name("Test Name")
    user.submit_button()
    time.sleep(3)

    name_message = user.get_validation_project_desc_msg()

    assert name_message == "This field is required"


