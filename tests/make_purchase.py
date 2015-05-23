import selenium_setup
import pages.fb_store


def make_purchase():
	"""Makes a purchase with a random billing/shipping address."""
	pages.fb_store.go_to_store()
	if "FitBit Store" in selenium_setup.driver.title is False:
	 	selenium_setup.driver.get_screenshot_as_file('make_purchase_url_possibly_broken')
	 	assert False

	pages.fb_store.enter_credit_card()
	pages.fb_store.enter_billing_address()
	pages.fb_store.proceed_to_next_page()
	# Would add an assertion, but the fake CC (naturally) doesn't validate when I test with prod. 

	# In a perfect world, would write the results to a file:
	# selenium_setup.results_file.write("make_purchase: passed")
