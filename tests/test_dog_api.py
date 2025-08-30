import requests
from utils.logger import get_logger

log = get_logger(__name__)   # create logger for this file

def test_get_random_dog_image():
    log.info("Starting test: Get Random Dog Image")
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    log.debug(f"Response status code: {response.status_code}")
    log.debug(f"Response body: {response.json()}")

    assert response.status_code == 200, "Expected status code 200"
    log.info("Test passed: Random dog image fetched successfully")

def test_get_random_dog_by_breed():
    breed="hound"
    url = f"https://dog.ceo/api/breed/{breed}/images/random"

    response = requests.get(url)
    log.info(f"Get {url} -> {response.status_code}")
    log.debug(f"Response: {response.json()}")

    assert response.status_code == 200
    data = response.json()

    assert data["status"] == "success"

    assert breed in data["message"], f"Expected breed {breed} in image URL"






