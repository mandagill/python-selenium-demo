import selenium_setup
import pages.fb_store


def make_purchase():
	pages.fb_store.go_to_store()
	# if "FitBit Store" in browser_api.title is False:
	#  	browser_api.get_screenshot_as_file('')
	#  	assert False

	pages.fb_store.enter_credit_card()
	pages.fb_store.enter_billing_address()
	pages.fb_store.proceed_to_next_page()
	
	# In a perfect world, would write the results to a file:
	# selenium_setup.results_file.write("make_purchase: passed")

