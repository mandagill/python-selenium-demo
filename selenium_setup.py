from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime


def setup():
	"""These should be run before kicking off any suite of related test cases."""
	# Would connect to DB and wipe all data for more complex suites
	# setup DB connections as needed "postgresql://localhost:5432/TestMigrate"
	global driver
	driver = webdriver.Firefox()
	
		

def teardown():
	# Would also close any open DB connections if they existed. 
	driver.close()




# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()	