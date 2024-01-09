import re
from playwright.sync_api import Page, expect


def test_getting_started_link(page: Page) -> None:
    """
    Test the getting started link on the page.
    Args:
        page (Page): The page object representing the web page.
    Returns:
        None
    """
    page.goto("https://school-sova.onrender.com/")
    expect(page).to_have_title(re.compile("S.O.V.A"))
    expect(page).to_have_url(re.compile(r"https://school-sova.onrender.com/.*"))


def test_navbar_menu_to_be_visible(page: Page) -> None:
    """
    Checks if the navbar menu is visible on the page.
    Args:
        page (Page): The page object representing the web page to test.
    Returns:
        None
    """
    page.goto("https://school-sova.onrender.com/")
    expect(page.get_by_role("heading", name="УЧИЛИЩЕ ЗА ПСИХОЛОГИЯ")).to_be_visible()
    expect(page.locator("#home div").first).to_be_visible()
    expect(page.get_by_role("link", name="За нас")).to_be_visible()
    expect(page.get_by_role("link", name="Програма")).to_be_visible()
    expect(page.get_by_role("link", name="Контакти")).to_be_visible()
    expect(page.get_by_role("link", name="Login")).to_be_visible()
    expect(page.get_by_role("link", name="Sign Up")).to_be_visible()


def test_navbar_menu_home(page: Page) -> None:
    """
    A function that tests the navigation bar menu by clicking on the "Home" link.
    Args:
        page (Page): The page object representing the web page to be tested.
    Returns:
        None
    """
    page.goto("https://school-sova.onrender.com/")
    page.get_by_role("link", name="Прочети още", exact=True).click()
    expect(page.locator("body")).to_be_visible()

    page.get_by_role("link", name="Начало").click()
    expect(page).to_have_url(re.compile(r"https://school-sova.onrender.com/.*"))


def test_navbar_menu_more(page: Page) -> None:
    """
    Navigates to the homepage, clicks on a link with the name "Прочети още" to read more,
    and expects the body element to be visible.
    Args:
        page (Page): The page object used for navigation and interaction.
    Returns:
        None
    """
    page.goto("https://school-sova.onrender.com/")
    page.get_by_role("link", name="Прочети още", exact=True).click()
    expect(page.locator("body")).to_be_visible()


def test_navbar_menu_about_us(page: Page) -> None:
    """
    Perform a series of actions to test the 'About Us' link in the navbar menu.
    Args:
        page (Page): The page object representing the web page.
    Returns:
        None
    """
    page.goto("https://school-sova.onrender.com/")
    expect(page.get_by_role("link", name="За нас", exact=True)).to_be_visible()
    page.get_by_role("link", name="За нас").click()
    expect(page.locator("#team-carousel")).to_be_visible()
    expect(page.locator("#team-carousel")).to_contain_text(
        "Емилия Сотирова Психолог, фамилен терапевт, преподавател по психодрама. Светлана Сотирова Психолог, Терапевт, Семеен консултант. Росица Славова Психолог, Терапевт, Семеен консултант. Моника Ройдева Психолог магистър, ръководител на проекти.")


def test_navbar_menu_program(page: Page) -> None:
    """
    This function tests the navigation bar menu program. It takes a Page object as input and does the following:
    1. Navigates to the URL "http://127.0.0.1:8000/".
    2. Expects a link with the role "link" and name "Програма" to be visible.
    3. Clicks on the link with the name "Програма".
    4. Expects an element with the locator "h9" and text "КАКВО Е „УЧИЛИЩЕ ЗА ПСИХОЛОГИЯ“?" to be visible.
    This function does not return any value.
    """
    page.goto("https://school-sova.onrender.com/")
    expect(page.get_by_role("link", name="Програма", exact=True)).to_be_visible()
    page.get_by_role("link", name="Програма").click()
    expect(page.locator("h9").filter(has_text="КАКВО Е „УЧИЛИЩЕ ЗА ПСИХОЛОГИЯ“?")).to_be_visible()


def test_navbar_menu_contacts(page: Page) -> None:
    """
    Navigates to the contacts page in the navbar menu and performs a series of assertions to ensure the correct page is loaded.
    Args:
        page (Page): The page object representing the browser page.
    Returns:
        None
    """
    page.goto("https://school-sova.onrender.com/")
    expect(page.get_by_role("link", name="Контакти", exact=True)).to_be_visible()
    page.get_by_role("link", name="Контакти").click()
    expect(page.locator("#contact")).to_be_visible()
    expect(page.get_by_text(
        "Свържи се с нас! Училището по психология се намира в центъра на гр Варна, ул.Александър Дякович")).to_be_visible()


def test_login_page_to_be_visible(page: Page) -> None:
    """
    Navigates to the login page and verifies that all elements on the page are visible.
    Args:
        page (Page): The page object representing the browser page.
    Returns:
        None
    """
    page.goto("https://school-sova.onrender.com/")
    expect(page.get_by_role("link", name="Login")).to_be_visible()
    page.get_by_role("link", name="Login").click()
    expect(page.get_by_text("Login Login")).to_be_visible()
    expect(page.get_by_role("button", name="Login")).to_be_visible()
    expect(page.get_by_placeholder("Username")).to_be_visible()
    expect(page.get_by_placeholder("Password")).to_be_visible()


def test_sign_up_page_to_be_visible(page: Page) -> None:
    """
    Navigate to the sign-up page and verify that all the required elements are visible.
    Args:
        page (Page): The page object representing the web page.
    Returns:
        None
    """
    page.goto("https://school-sova.onrender.com/")
    expect(page.get_by_role("link", name="Sign Up")).to_be_visible()
    page.get_by_role("link", name="Sign Up").click()
    expect(page.locator("form").filter(has_text="Sign up Sign up").get_by_placeholder("Username")).to_be_visible()
    expect(page.get_by_placeholder("Email")).to_be_visible()
    expect(page.get_by_placeholder("Password", exact=True)).to_be_visible()
    expect(page.get_by_placeholder("Confirm Password")).to_be_visible()
    expect(page.get_by_role("button", name="Sign up")).to_be_visible()
