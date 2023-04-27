# def test_multiUrlMarketing_page(driver, multi_Marketing_url):
#    multi_Marketing_url.DoctorMarketingmethod()
#    multi_Marketing_url.HospitalMarketingmethod()
#    multi_Marketing_url.NormalMarketingmethod()
#    multi_Marketing_url.CostMarketingmethod()


# test_contact_us.py
# from page_objects import ContactUsPage
import pytest


def test_marketing_brand_url(driver,marketingbrand_url):
    marketingbrand_url.marketing_brand_method()

    # process the data and perform the contact us action
