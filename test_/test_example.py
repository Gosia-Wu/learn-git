from playwright.sync_api import Page, expect


def test_w_firma_page(page: Page):
    # page.set_viewport_size({"width": 980, "height": 600})
    page.goto("https://wfirma.pl")
    expect(page.locator("h1")).to_contain_text("Księgowość online dla Ciebie")
    signInButton = page.locator(".btn-custom-login")
    signInButton.click()
    emailField = page.locator("#UserLogin")
    emailField.click()
    emailField.fill("tinu@wp.pl")
    passwordField = page.locator("#UserPassword")
    passwordField.click()
    passwordField.fill("12345678")
    submitButton = page.locator('button[type="submit"].btn-login')
    submitButton.click()
    
    