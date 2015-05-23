"""Contains actions that will be taken on the https://www.fitbit.com/store page."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium_setup as ss
from random import choice


# Were this case going to be run against the actual FitBit test env, I would pull this data
# out of a test DB. I'm saving myself the DB setup by hardcoding a small sample of test data here.
# The dictionary keys match the attribute names defined for the DOM element where the data will be input.
STATES = {'CA California': {'billing-address-line1': '300 San Pablo Ave', 'billing-address-city': 'Oakland', 'billing-address-postal-code': '94612'},
'MA Massachusetts': {'billing-address-line1': '200 Oxford Street', 'billing-address-city': 'Boston', 'billing-address-postal-code': '02111'},
'NJ New Jersey': {'billing-address-line1': '4039 Annandale Road', 'billing-address-city': 'Flemington', 'billing-address-postal-code': '08822'},
'NY New York': {'billing-address-line1': '21 Orchard St', 'billing-address-city': 'New York', 'billing-address-postal-code': '10002'},
'PA Pennsylvania': {'billing-address-line1': '400 South 2nd Street', 'billing-address-city': 'Harrisburg', 'billing-address-postal-code': '17101'}}

CREDIT_CARDS = {'Visa': '4111111111111111', 'MasterCard': '5111111111111111', 'Amex': '371111111111111'}


def go_to_store():
	"""Takes the browser API as parameter so the code can easily be 
	rerun when the suite is run for each supported browser."""
	
	ss.driver.get("https://www.fitbit.com/store")
	add_to_cart_btn = ss.driver.find_element_by_xpath("//div[@class='chargehr-buttons']//span[.='ADD TO CART']")
	add_to_cart_btn.click()
	# Ensure the page loads before proceeding:
	try:
	    product_img = WebDriverWait(ss.driver, 10).until(
	        EC.presence_of_element_located((By.Text, "Shopping cart"))
	    )
	except:
		# ideally, would also take a screencap
		return "Test failed"


def enter_credit_card(card_type='Visa'):
	"""Function completes billing information. Allows caller to specify what card type they
	would like to test with, using Visa as a default.

	For a larger/more extensive suite, I might also parameterize the expiration numbers to allow
	for negative test cases, e.g. ensuring an error is thrown if a user enters an expired card."""

	ccn_field = ss.driver.find_element_by_xpath('//*[@id="cart"]/div[1]/section[1]/div/label/input')
	ccn_field.send_keys(CREDIT_CARDS[card_type])
	exp_month_ddm = ss.driver.find_element_by_xpath('//*[@id="cart"]/div[1]/section[1]/div/div[2]/label[1]/select')
	exp_month_ddm.send_keys('05 May')
	exp_year_ddm = ss.driver.find_element_by_xpath('//*[@id="cart"]/div[1]/section[1]/div/div[2]/label[2]/select')
	exp_year_ddm.send_keys('2025') #Pick something far out so script won't break until 2025
	csc_field = ss.driver.find_element_by_xpath('//*[@id="cart"]/div[1]/section[1]/div/div[4]/label/input')
	csc_field.send_keys('123')


def enter_billing_address(state_to_enter=None):
	"""Function allows the caller to specify which state they wish to enter an address for;
	if no argument passed, function defaults to choosing a random state and enters its corresponding address."""

	billing_name_field = ss.driver.find_element_by_xpath('//*[@id="cart"]/form/div[1]/div[2]/fieldset/div[1]/label[1]/input')
	billing_name_field.send_keys("FitBit TestUser")
	state_ddm = ss.driver.find_element_by_xpath('//*[@id="cart"]/form/div[1]/div[2]/fieldset/div[1]/label[5]/select')
	if state_to_enter is None:
		options = STATES.keys()
		state_to_enter = choice(options)
	state_ddm.send_keys(state_to_enter)
	address_1_field = ss.driver.find_element_by_xpath('//*[@id="cart"]/form/div[1]/div[2]/fieldset/div[1]/label[2]/input')
	address_1_field.send_keys(STATES[state_to_enter]['billing-address-line1'])
	city_field = ss.driver.find_element_by_xpath('//*[@id="cart"]/form/div[1]/div[2]/fieldset/div[1]/label[4]/input')
	city_field.send_keys(STATES[state_to_enter]['billing-address-city'])
	zipcode_field = ss.driver.find_element_by_xpath('//*[@id="cart"]/form/div[1]/div[2]/fieldset/div[1]/label[6]/input')
	
	zipcode_field.send_keys(STATES[state_to_enter]['billing-address-postal-code'])


# def choose_shipping_option(ss.driver, shipping_type='FREE'):
# 	radio_buttons = find_elements(by='data-qa', value='shipping-method-name')

# 	if shipping_type == 'PAID':
# 		# randomly choose a ship type
# 	else:
# 		# allow shipping option to remain default
# 	pass


def proceed_to_next_page():
	next_button = ss.driver.find_element_by_xpath('//*[@id="review-next"]')












	