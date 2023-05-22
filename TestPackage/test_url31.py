"""This is under skip format as the website is redirecting to the Developement form"""



import pytest
@pytest.mark.skip
def test_marketing_Index(driver,marketingindex_url):
    marketingindex_url.Marketing_Index_Method()










