from playwright.sync_api import sync_playwright, Error
from playwright_helpers import *
from function_helpers import *
from dotenv import load_dotenv
import os

load_dotenv()

# Check if the folder exists
if not os.path.exists("contents"):
    os.makedirs("contents")

# GLOBAL VARIABLES
SIGNUP_URL = os.getenv('SIGNUP_URL')
USER_NAME = os.getenv('USER_NAME')
USER_EMAIL = generate_email(os.getenv('USER_EMAIL'))
USER_PASSWORD = os.getenv('USER_PASSWORD')
SECRET_KEY = ""

def extract_recovery_code(page):
    recovery_code_selector = '.code_code__pvdi7f7 .code-font'
    page.wait_for_selector(recovery_code_selector)
    RECOVERY_CODE = page.text_content(recovery_code_selector)
    print(f"Recovery Code: {RECOVERY_CODE}")
        
def auto_create_account(playwright):
    browser = None
    try:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Navigate to sign up page
        print("00.00 - Navigating to sign up page...")
        navigate_to_page(page, SIGNUP_URL)

        # 01 - Skip Adding Extention
        print("01.00 - Skipping adding extension...")
        click_button_by_text(page, "Add it later")
        click_button_by_text(page, "Skip")

        # 02 - Fill in user information
        print("02.00 - Filling in user information...")
        fill_field_by_id(page, "user-name", USER_NAME)
        fill_field_by_id(page, "email", USER_EMAIL)
        click_button_by_id(page, "submit")

        # 03 - Verify email code
        print("03.00 - Sending verification code...")
        code = input("03.01 - Input Code from Email: ")
        fill_field_by_id(page, "code", code)
        click_button_by_id(page, "submit")
        page.wait_for_timeout(1000)

        # 04 - Click next on security information page
        print("04.00 - Clicking next on security information page...")
        click_button_by_text(page, "Next")

        # 05 - Set password
        print("05.00 - Setting password...")
        # user_password = input("Input Password: ")
        USER_PASSWORD = "123456789x987654321"
        fill_field_by_id(page, "password", USER_PASSWORD)
        fill_field_by_id(page, "confirm-password", USER_PASSWORD)
        click_button_by_id(page, "submit")

        # 06 - Skip payment method
        print("06.00 - Skipping payment method...")
        click_button_by_class(page, "section.secondary-cta")

        # 07 - Download secret key
        print("07.00 - Downloading secret key...")
        page.wait_for_timeout(5000)
        click_button_by_text(page, "Generate Secret Key")
        download_button_selector = '.download-link--secret_key_gtdUP'
        download_pdf(page, download_button_selector, new_filename='PDF-KEY.pdf')
        click_button_by_text(page, "Next")

        # 08.01 - Click the user menu button
        print("08.01 - Clicking the user menu button...")
        user_menu_button_selector = 'button[data-testid="user-menu-button"]'
        click_user_menu_button(page, user_menu_button_selector)

        # 08.02 - Click the My Profile link
        print("08.02 - Clicking the My Profile link...")
        my_profile_link_selector = 'a[href="/profile"]'
        click_my_profile(page, my_profile_link_selector)

        # 09.00 - Extract Secret Key
        print("09.00 - Extracting Secret Key...")
        page.hover("div.detail.copy-box.rounded-section")
        page.click("button[aria-label='Show Secret Key']")
        page.wait_for_selector("p.secret-key")
        SECRET_KEY = page.text_content("p.secret-key")

        # 10.00 - PRINT INFORMATION
        print("10.00 - PRINT INFORMATION...")
        print("=========================================")
        print("Username:", USER_NAME)
        print("Email:", USER_EMAIL)
        print("Password:", USER_PASSWORD)
        print("Secret Key:", SECRET_KEY)
        

        # Close browser
        input("Press Enter to exit...")
        browser.close()

    except Error as e:
        print(e)
    
    finally:
        if browser:
            browser.close()

with sync_playwright() as playwright:
    auto_create_account(playwright)