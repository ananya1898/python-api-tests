import pytest
import requests
from utils.logger import get_logger

log = get_logger(__name__)   # create logger for this file

BASE_URL = "https://dog.ceo/api"

@pytest.fixture(scope="module")
def base_url():
    """Fixture to provide the base API URL."""
    return BASE_URL

def test_get_random_dog_image(base_url):
    """Verify fetching a completely random dog image."""
    log.info("Starting test: Get Random Dog Image")
    url=f"{base_url}/breeds/image/random"
    response = requests.get(url)
    log.info(f"GET {url} -> {response.status_code}")

    assert response.status_code == 200, "Status code mismatch"
    data = response.json()
    assert data["status"] == "success"
    assert data["message"].startswith("https://"), "Image URL must be valid"



@pytest.mark.parametrize("breed", ["hound", "bulldog", "retriever"])
def test_get_random_dog_by_breed(base_url, breed):
    url = f"{base_url}/breed/{breed}/images/random"

    response = requests.get(url)
    log.info(f"Get {url} -> {response.status_code}")
    log.debug(f"Response: {response.json()}")

    assert response.status_code == 200, "Status code mismatch"
    data = response.json()
    assert data["status"] == "success"
    assert breed in data["message"], f"Expected breed {breed} in image URL"



def test_get_all_breeds(base_url):
    """Verify that all dog breeds can be fetched."""
    url = f"{base_url}/breeds/list/all"
    response = requests.get(url)
    log.info(f"GET {url} -> {response.status_code}")

    assert response.status_code == 200, "Status code mismatch"
    data = response.json()
    assert data["status"] == "success"
    assert isinstance(data["message"], dict), "Expected a dict of breeds"
    assert "hound" in data["message"], "Hound breed should be present"


