import pytest


@pytest.fixture(scope="function")
def page(browser):
    """Page fixture for tests"""
    context = browser.new_context(viewport={"width": 1280, "height": 720})
    page = context.new_page()
    yield page
    page.close()
    context.close()
