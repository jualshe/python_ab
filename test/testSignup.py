import pytest
from model.user import User
from fixture.application import Application


# signup creates the user but doesn't verify it
@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_signup(app):
    app.open_home_page()
    app.click_signup_button()
    app.input_user_data(User(email="lilonann@mailinator.com", password="12345678", firstname="lil",
                             lastname="nan"))
    app.select_agree_checkbox()
    # verification code field - driver.find_element_by_name("vcode").click()
    # add verification code extraction
