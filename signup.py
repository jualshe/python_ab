import pytest
from user import User
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_signup(app):
    app.open_home_page()
    app.click_signup_button()
    app.signup_user_data(User(email="lilonann@mailinator.com", password="12345678", firstname="lil",
                              lastname="nan"))
    app.select_agree_checkbox()
    # verification code field - driver.find_element_by_name("vcode").click()
