from http import HTTPStatus
import os
import json
import dotenv
import pytest
import requests
from faker import Faker


@pytest.fixture(scope="session", autouse=True)
def envs():
    dotenv.load_dotenv()


@pytest.fixture(scope="session")
def app_url():
    return os.getenv("APP_URL")


@pytest.fixture
def users(app_url):
    response = requests.get(f"{app_url}/api/users/")
    assert response.status_code == HTTPStatus.OK
    return response.json()


@pytest.fixture
def port():
    return 8002


# preconditions - add users to database without users id
# scope="module" - this fixture for this module (page)
@pytest.fixture(scope="module")
def fill_test_data(app_url):
    with open("users.json") as f:
        test_data_users = json.load(f)
    api_users = []
    for user in test_data_users:
        response = requests.post(f"{app_url}/api/users/", json=user)
        api_users.append(response.json())

    user_ids = [user["id"] for user in api_users]

    yield user_ids  # test start here, fixture return user_ids

    # delete created users from database
    for user_id in user_ids:
        requests.delete(f"{app_url}/api/users/{user_id}")


@pytest.fixture
def new_user() -> dict:
    fake = Faker()
    new_user = {
        "email": fake.email(),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "avatar": fake.image_url()
    }
    return new_user



@pytest.fixture
def create_new_user() -> int:
    url = os.getenv("APP_URL")
    fake = Faker()
    new_user = {
        "email": fake.email(),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "avatar": fake.image_url()
    }
    user = requests.post(f"{url}/api/users/", json=new_user)
    assert user.status_code == HTTPStatus.CREATED
    return user.json()['id']
