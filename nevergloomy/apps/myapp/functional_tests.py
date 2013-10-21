from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrive_it_late(self):
        # Pat has heard about a cool new online screensaver. She goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention screensaver
        self.assertIn('screensaver', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('never gloomy', header_text)

        # She is invited to enter a schedule item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a time'
        )

        # She types "8:00" into a text box (Pat needs to get up every morning at 9am)
        inputbox.send_keys('8:00')

        # When she hits enter, the page updates, and now the page lists:
        # "Day and Month" as an item on the screensaver
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '8:00' for row in rows)
        )

        # There is still a text box inviting her to add another item.
        # She types "11:00" into a text box (Pat needs to check SpoonRocket at that time)
        self.fail('Finish the test!')



# There is still a text box inviting her to add another item.
# She types "11:00" into a text box (Pat needs to check SpoonRocket at that time)

# The page updates again, and now shows both items on her list

# Pat wonders whether the site will remember her schedule. Then she sees that the site has
# generated a unique URL fo rher -- there is some explanatory text to that effect.

# She visits that URL - her schedule is still there.

# Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main()
