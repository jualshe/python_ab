import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.open_home_page()