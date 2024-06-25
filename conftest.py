import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import ChromeOptions

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Choose browser: chrome or firefox')

    parser.addoption('--language', action='store', default='en', help='write language')



@pytest.fixture
def command_line_args(request):
    args = {}
    args['browser_name'] = request.config.getoption('--browser_name')
    args['language'] = request.config.getoption('--language')
    return args


@pytest.fixture(scope="function")
def browser(command_line_args):
    browser_name = command_line_args['browser_name']
    user_language = command_line_args['language']
    browser = None
    optionsC = ChromeOptions()
    optionsF = Options()


    if browser_name == 'chrome':
        print('\nstart chrome browser for test..')
        optionsC.add_experimental_option("prefs", {'intl.accept.languages': user_language})
        browser = webdriver.Chrome(options=optionsC)

    elif browser_name == 'firefox':
        print('\nstart firefox browser for test..')
        optionsF.set_preference('intl.accept.languages', user_language)
        browser = webdriver.Firefox(options=optionsF)
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')

    yield browser
    browser.quit()
    print('\nquit browser..')








# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
#
# def pytest_addoption(parser):
#     parser.addoption(
#         "--language", action="store", default="en", help="Language for the browser"
#     )
#
# @pytest.fixture
# def browser(request):
#     language = request.config.getoption("--language")
#     options = Options()
#     options.add_experimental_option('prefs', {'intl.accept_languages': language})
#     browser = webdriver.Chrome(options=options)
#     yield browser
#     browser.quit()


# def pytest_addoption(parser):
#     parser.addoption('--browser_name', action='store', default=None,
#                      help="Choose browser: chrome or firefox")
#
#
# @pytest.fixture(scope="function")
# def browser(request):
#     browser_name = request.config.getoption("browser_name")
#     browser = None
#     if browser_name == "chrome":
#         print("\nstart chrome browser for test..")
#         browser = webdriver.Chrome()
#     elif browser_name == "firefox":
#         print("\nstart firefox browser for test..")
#         browser = webdriver.Firefox()
#     else:
#         raise pytest.UsageError("--browser_name should be chrome or firefox")
#     yield browser
#     print("\nquit browser..")
#     browser.quit()



