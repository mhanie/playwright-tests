from pages.login_page import LoginPage


def test_successful_login(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    assert "inventory" in page.url


def test_invalid_password(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("standard_user", "wrong_password")

    error = page.get_by_text("do not match").first
    assert error.is_visible()


def test_locked_out_user(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("locked_out_user", "secret_sauce")

    error = page.get_by_text("locked out").first
    assert error.is_visible()