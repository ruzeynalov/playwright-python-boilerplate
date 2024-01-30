# Python WebUI Test Automation with Playwright Tutorial

This tutorial provides a step-by-step guide on using Python and Playwright for WebUI test automation.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Running Tests](#running-tests)
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

## Running Tests

1. Running tests in headless mode Chrome

```shell
python3 -m pytest tests --verbose
```
2. Running tests in headed mode & specific browser(chromium,firefox,webkit)

```shell
python3 -m pytest tests --browser webkit  --headed --verbose
```
3. Running tests in headed mode in all browsers in parallel

```shell
python3 -m pytest tests --numprocesses auto --browser chromium --browser firefox --browser webkit  --headed --verbose
```

## License

This project is licensed under the [MIT License](LICENSE).
