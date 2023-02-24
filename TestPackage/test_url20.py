#def test_multiUrlMarketing_page(driver, multi_Marketing_url):
#    multi_Marketing_url.DoctorMarketingmethod()
#    multi_Marketing_url.HospitalMarketingmethod()
#    multi_Marketing_url.NormalMarketingmethod()
#    multi_Marketing_url.CostMarketingmethod()


# test_contact_us.py
from page_objects import ContactUsPage

def test_contact_us_with_excel_data(driver):
    contact_us_page = ContactUsPage(driver)
    contact_us_page.open()
    data = contact_us_page.read_data_from_excel("data.xlsx")
    # process the data and perform the contact us action
    contact_us_page.ContactUs()




