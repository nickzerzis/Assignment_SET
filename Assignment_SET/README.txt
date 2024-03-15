This project is made to test the PM_tool

It uses Page Object Model approach with python and pytest for the testing.

The test suite have positive and negative cases for signup,login,dashboard projects and task actions.



Prerequisites to run the tests:

1) Install Python3 from https://www.python.org/ and follow the instructions there

2) Install the latest version of Chrome (The chromedriver is already uploaded on the project)

3) Navigate to projects repository on cmd and enter the command : "pip install -r requirements.txt"



When the prerequisites are installed, I suggest to run the test cases/scenarios by the custom tags in this order:

1) For signup Tests on cmd: "pytest -v -m signuPositive  --html=test_report.html"
                            "pytest -v -m signupNegative  --html=test_report.html"

2) For login Tests on cmd: "pytest -v -m loginPositive  --html=test_report.html"
                           "pytest -v -m loginNegative  --html=test_report.html"

3) For dashboard Tests on cmd: "pytest -v -m dash  --html=test_report.html"
                               "pytest -v -m dashNegative  --html=test_report.html"

4) For Task/TaskDB Tests on cmd: "pytest -v -m taskPositive  --html=test_report.html"
                                 "pytest -v -m TaskNegative  --html=test_report.html"
                                 "pytest -v -m ScenarioTaskDB1  --html=test_report.html"
                                 "pytest -v -m ScenarioTaskDB2  --html=test_report.html" (This scenario is not standalone. ScenarioTaskDB1 should run before)




Defects found after testing:
1) Cannot create Task with .txt file uploaded --Systematic
2) Created Tasks and TaskDb sometimes not aligned -- NonSystematic
