## Demo project on Python with Web UI tests for [BookStore DemoQa](https://demoqa.com/books) service

<div align="center">
<img src="readme_images/logo.png" height="100"/>&nbsp;
</div>

### Tools and technologies used
<p>
<a href="https://www.python.org/"><img src="readme_images/technologies/python.png" width="40" height="40"  alt="PYTHON"/></a>
<a href="https://docs.pytest.org/en/"><img src="readme_images/technologies/pytest.png" width="40" height="40"  alt="PYTEST"/></a>
<a href="https://www.jetbrains.com/pycharm/"><img src="readme_images/technologies/pycharm.png" width="40" height="40"  alt="PYCHARM"/></a>
<a href="https://www.selenium.dev/"><img src="readme_images/technologies/selenium.png" width="40" height="40"  alt="SELENIUM"/></a>
<a href="https://github.com/yashaka/selene/"><img src="readme_images/technologies/selene.png" width="40" height="40"  alt="SELENE"/></a>
<a href="https://python-poetry.org/"><img src="readme_images/technologies/poetry.png" width="40" height="40"  alt="POETRY"/></a>
<a href="https://docs.pydantic.dev/latest/"><img src="readme_images/technologies/pydantic.png" width="40" height="40"  alt="PYDANTIC"/></a>
<a href="https://pypi.org/project/requests/"><img src="readme_images/technologies/requests.png" width="40" height="40"  alt="REQUESTS"/></a>
<a href="https://www.jenkins.io/"><img src="readme_images/technologies/jenkins.png" width="40" height="40"  alt="JENKINS"/></a>
<a href="https://allurereport.org/"><img src="readme_images/technologies/allure_report.png" width="40" height="40"  alt="ALLUREREPORT"/></a>
<a href="https://qameta.io/"><img src="readme_images/technologies/allure_testops.png" width="40" height="40"  alt="ALLURETESTOPS"/></a>
<a href="https://aerokube.com/selenoid/"><img src="readme_images/technologies/selenoid.png" width="40" height="40"  alt="SELENOID"/></a>
<a href="https://www.atlassian.com/software/jira"><img src="readme_images/technologies/jira.png" width="40" height="40"  alt="JIRA"/></a>
</p>

### Test coverage
Web GUI-tests:
* User authorization
* Bookstore: search, navigate, view book details
* Profile: View, navigate

* Example of Web test's running (successful login):

<img src="readme_images/bookstore_web_test.gif"/>&nbsp;

Example of test case in Allure Report:

<img src="readme_images/bookstore_api_test.png" height="400"/>&nbsp;

### Test Launch
Tests are launching using **Jenkins service**.
Jenkins is used for test runs. To run tests, go to Jenkins job and click 'Build with parameters', select browser + version (for example, firefox 98.0) click 'Build'.

<img src="readme_images/bookstore_jenkins_1.png"/>&nbsp;
<img src="readme_images/bookstore_jenkins_2.png"/>&nbsp;

Additionally, integration with Allure TestOps added into same Jenkins job. So you can run Jenkins job with all the tests or specify individual tests to run via Allure TestOps.

<img src="readme_images/bookstore_testops_jobs.png"/>&nbsp;

Select individual tests or test groups by their allure decorators:

<img src="readme_images/bookstore_testops_parameters.png"/>&nbsp;

### Test Report and Test Documentation

Reporting is implemented with Allure services.

Allure Report can be opened from Jenkins, see screenshot below. And contains charts, details of test executions, different kinds of attachments (screenshots, logs, video, page html)

<img src="readme_images/bookstore_allure_1.png"/>&nbsp;
<img src="readme_images/bookstore_allure_2.png"/>&nbsp;

Allure TestOps also contains such information. Also it's generating Test Documentation that can be imported to Jira.
<img src="readme_images/bookstore_testops_dashboard.png"/>&nbsp;
<img src="readme_images/bookstore_testops_tc.png"/>&nbsp;

### Integration with Jira

Test Cases and Allure Launches have been integrated into Jira Task:
<img src="readme_images/bookstore_jira.png"/>&nbsp;

### Test Results Notifications
When test run finished, telegram message with the following data is sent:

* total amount of tests and run duration
* percentage of passed/failed/skipped etc. tests
* link to the test run report

<img src="readme_images/bookstore_telegram.png" height="300"/>&nbsp;

The following tool is used for sending notifications: [allure-notifications library](https://github.com/qa-guru/allure-notifications). Telegram bot was created and added to a specific telegram group

(many different notifications supported: Telegram, Slack, Skype, Email, Mattermost, Discord, Loop)
