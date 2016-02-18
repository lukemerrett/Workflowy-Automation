import time
import settings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class WorkflowyScheduler(object):
    workflowy_url = "https://workflowy.com"
    browser = webdriver.Firefox()

    @classmethod
    def schedule_items_for_today(cls):
        todays_date_tag = cls.__get_todays_date_tag()

        cls.browser.get(cls.workflowy_url)

        cls.__login()
        cls.__search(todays_date_tag)
        cls.__mark_results_with_tag("#Focus")
        cls.__save_changes()

        cls.browser.close()

    @classmethod
    def __login(cls):
        cls.__click_button("div.header-bar a.button--top-right")
        cls.__wait_for_element_to_appear("#id_username")
        cls.__fill_text_box("#id_username", settings.workflowy_username)
        cls.__fill_text_box("#id_password", settings.workflowy_password)
        cls.__click_button("input.button--submit")

    @classmethod
    def __search(cls, search_term: str):
        cls.__wait_for_element_to_appear("#searchBox")
        cls.__fill_text_box("#searchBox", search_term)

    @classmethod
    def __mark_results_with_tag(cls, tag: str):
        for element in cls.browser.find_elements_by_css_selector("div.name.matches"):
            text = element.text
            if tag not in text:
                text_box = element.find_element_by_css_selector("div.content")
                text_box.click()
                text_box.send_keys(Keys.END)
                text_box.send_keys(" " + tag)

    @classmethod
    def __save_changes(cls):
        cls.browser.find_element_by_css_selector("div.saveButton").click()
        cls.__wait_for_element_to_appear("div.saveButton.saved")

    @classmethod
    def __click_button(cls, css_selector: str):
        cls.browser.find_element_by_css_selector(css_selector).click()

    @classmethod
    def __wait_for_element_to_appear(cls, css_selector):
        WebDriverWait(cls.browser, 10).until(lambda driver: driver.find_element_by_css_selector(css_selector))

    @classmethod
    def __fill_text_box(cls, css_selector: str, text_to_input: str):
        cls.browser.find_element_by_css_selector(css_selector).send_keys(text_to_input)

    @classmethod
    def __get_todays_date_tag(cls) -> str:
        return "#%s" % time.strftime("%Y-%m-%d")


if __name__ == "__main__":
    WorkflowyScheduler.schedule_items_for_today()
