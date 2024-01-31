import pytest
from typing import Generator
from playwright.sync_api import Playwright, APIRequestContext
import allure

@pytest.fixture(scope="session")
def user_ids():
    ids = []
    yield ids


@pytest.fixture(scope="session")
def user_api_request_context(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(
        base_url="https://reqres.in"
    )
    yield request_context
    request_context.dispose()

@allure.title("Create new user")
@allure.description("This test attempts to create a new user using reqres.in API")
@allure.tag("API", "CRUD", "POSITIVE")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.apitest
def test_create_user(user_api_request_context: APIRequestContext, user_ids) -> None:
    payload = {
        "name": "Rustam",
        "job": "QA Automation Engineer"
    }
    allure.attach(str(payload),"Request Body")
    response = user_api_request_context.post(url="/api/users", data=payload)
    assert response.ok

    json_response = response.json()
    allure.attach(str(json_response),"Response Body")
    print("Create User API Response:\n{}".format(json_response))
    assert json_response["name"] == payload.get("name")
    user_ids.append(json_response["id"])

@allure.title("Check for non-existing user")
@allure.description("This test attempts to get a non-existing user using reqres.in API")
@allure.tag("API", "CRUD", "NEGATIVE")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.apitest
def test_get_user_not_found(user_api_request_context: APIRequestContext, user_ids) -> None:
    response = user_api_request_context.get(url="/api/users/0")
    assert response.status == 404
    json_response = response.json()
    allure.attach(str(json_response),"Response Body")
    print("Get User API Response - User Not Found:\n{}".format(json_response))

@allure.title("Check for existing user")
@allure.description("This test attempts to get an existing user using reqres.in API")
@allure.tag("API", "CRUD", "POSITIVE")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.apitest
def test_get_user_happy_flow(user_api_request_context: APIRequestContext) -> None:
    response = user_api_request_context.get(url="/api/users/2")
    assert response.status == 200

    json_response = response.json()
    allure.attach(str(json_response),"Response Body")
    print("Get User API Response - Happy Flow:\n{}".format(json_response))
    assert json_response["data"]["id"] == 2