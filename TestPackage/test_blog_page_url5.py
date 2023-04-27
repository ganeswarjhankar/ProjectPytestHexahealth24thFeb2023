####Ok Tested####

import pytest


@pytest.mark.skip
def test_condition_page(driver, blog_page):
    blog_page.Contactwhatsaap()

