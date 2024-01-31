# Python WebUI Test Automation with Playwright Tutorial

This tutorial provides a step-by-step guide on using Python and Playwright for WebUI test automation.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Running UI Tests](#running-ui-tests)
- [Running API Tests](#running-api-tests)
- [Running All Tests](#running-all-tests)
- [Debugging Tests](#debugging-tests)
- [Allure Report](#allure-report)
- [License](#license)

## Introduction

In this tutorial, we will explore how to use Python and Playwright to automate WebUI tests.

## Prerequisites

Before getting started, make sure you have the following prerequisites installed:

- [Python 3.x](https://www.python.org/downloads/)
- PIP
 ```shell
    python3 -m ensurepip
```
- venv
 ```shell
    pip install virtualenv
```


## Getting Started

To get started with Python and Playwright, follow these steps:

1. Clone or download this repository.
2. Open a terminal and navigate to the project directory.
3. Create and activate isolated environment by running following commands
```shell
python3 -m venv venv
```
For Linux & Mac run 
```shell
source venv/bin/activate
```
For Windows run
```shell
venv\Scripts\activate.bat
```
4. Install the project dependencies by running the following command:
```shell
pip3 install -r requirements.txt
```

## Running UI Tests

1. Running UI tests in headless mode Chrome

```shell
python3 -m pytest -m webtest tests --verbose
```
2. Running UI tests in headed mode & specific browser(chromium,firefox,webkit)

```shell
python3 -m pytest -m webtest tests --browser webkit  --headed --verbose
```
3. Running UI tests in headed mode in all browsers in parallel

```shell
python3 -m pytest -m webtest tests --numprocesses auto --browser chromium --browser firefox --browser webkit  --headed --verbose
```

## Running API Tests

Running API tests using Playwright

```shell
python3 -m pytest -m apitest -s tests --screenshot on --verbose
```
## Running All Tests

1. Running All tests using Playwright in headless mode

```shell
python3 -m pytest -s tests --screenshot on --verbose
```

1. Running All tests using Playwright in headed mode
```shell
python3 -m pytest -s tests --screenshot on --verbose --headed
```

## Debugging Tests

In order to launch Playwright inspector and debug specific tests run following commands

```shell
PWDEBUG=1 python3 -m pytest -s -k test_basic_duckduckgo_search --verbose
```

## Allure Report
By default test summary will be posted into commandline

In order to generate HTML report using Allure reporting framework run tests with `--alluredir` parameter

```shell
python3 -m pytest -s --alluredir=allure-results tests --numprocesses auto --browser chromium --browser firefox --browser webkit --screenshot on --video on --headed --verbose
```

And the generate and open report in browser by running
```shell
allure serve -h localhost
```

## License

This project is licensed under the [MIT License](LICENSE).
