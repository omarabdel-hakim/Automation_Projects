import pytest
from selenium import webdriver
from selenium.webdriver.ie.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def pytest_addoption(parser):
    parser.addoption(
        "--browse_name", action="store", default="chrome"
    )
@pytest.fixture(scope="class")
def setup(request):
    browse_name = request.config.getoption("browse_name")
    if browse_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=chrome_options)

    elif browse_name == "edge":
        edge_options = webdriver.EdgeOptions()
        edge_options.add_argument("--start-maximized")
        driver = webdriver.Edge(options=edge_options)

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    driver.close()