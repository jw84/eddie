from selenium import webdriver
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
        self.fail('Finish the test!')

        # She is invited to enter a schedule item straight away

# She types "8:00" into a text box (Pat needs to get up every morning at 9am)

# When she hits enter, the page updates, and now the page lists:
# "Day and Month" as an item on the screensaver

# There is still a text box inviting her to add another item.
# She types "11:00" into a text box (Pat needs to check SpoonRocket at that time)

# The page updates again, and now shows both items on her list

# Pat wonders whether the site will remember her schedule. Then she sees that the site has
# generated a unique URL fo rher -- there is some explanatory text to that effect.

# She visits that URL - her schedule is still there.

# Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main()
