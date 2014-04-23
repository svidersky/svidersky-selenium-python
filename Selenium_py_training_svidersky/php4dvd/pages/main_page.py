from internal_page import InternalPage


class MainPage(InternalPage):

    @property
    def film_search_field(self):
        return self.driver.find_element_by_id("q")

    @property
    def film_found(self):
        return self.driver.find_element_by_css_selector("div.nocover")