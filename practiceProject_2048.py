# Play the game 2048 at https://play2048.co/ and use the combination of arrows keys up, right, down and left to get a fairly high score.


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://gabrielecirulli.github.io/2048/')
# Play the game.
game = browser.find_element_by_tag_name('html')
while True:
    game.send_keys(Keys.UP)
    game.send_keys(Keys.RIGHT)
    game.send_keys(Keys.DOWN)
    game.send_keys(Keys.LEFT)