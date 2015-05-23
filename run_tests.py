# Equivalent of main.py or public static void main()
import tests.make_purchase
import selenium_setup

selenium_setup.setup()
tests.make_purchase.make_purchase()
tests.make_purchase.make_CA_purchase()
selenium_setup.teardown()
