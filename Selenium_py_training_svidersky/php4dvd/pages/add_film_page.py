from internal_page import InternalPage


class AddFilmPage(InternalPage):

    @property
    def film_title_field(self):
        return self.driver.find_element_by_name("name")

    @property
    def film_year_field(self):
        return self.driver.find_element_by_name("year")

    @property
    def add_film_submit(self):
        return self.driver.find_element_by_name("submit")

    @property
    def result_text(self):
        return self.driver.find_element_by_css_selector("h2").text

    @property
    def field_is_required(self):
        return self.driver.find_element_by_xpath("//form[@id='updateform']/table/tbody/tr[4]/td[2]/label").text

    @property
    def field_required_text(self):
        return "This field is required"