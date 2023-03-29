
import pytest

# test_contact_us.py
#from page_objects import ContactUsPage


@pytest.mark.xfail
def test_marketing_Index(driver,marketingindex_url):
    marketingindex_url.Marketing_Index_Method()
    pass









