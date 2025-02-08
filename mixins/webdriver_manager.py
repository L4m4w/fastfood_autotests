from selene import browser

class WebDriverManager:

    @staticmethod
    def browser_manager():
        browser.config.base_url = 'https://demoqa.com/automation-practice-form'
        browser.config.timeout = 4.0
        browser.config.type_by_js = True

        yield browser