from internal_page import InternalPage


class FilmDescriptionPage(InternalPage):

    @property
    def film_remove_button(self):
        return self.driver.find_element_by_css_selector("img[alt=\"Remove\"]")

    @property
    def film_title_field(self):
        return self.driver.find_element_by_name("name")