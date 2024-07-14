from playwright.sync_api import Page, Error
import os
import logging

logging.basicConfig(
    filename='boring_stuffs.log', 
    level=logging.INFO, 
    format='%(levelname)s - %(message)s', 
    filemode='w'
)

def navigate_to_page(page: Page, url: str):
    try:
        page.goto(url)
        page.wait_for_load_state('networkidle')
        logging.info(f"Page navigated to: {url}")
    except Error as e:
        logging.error(f"An error occurred while navigating to {url}: {e}")

def fill_field_by_id(page: Page, id: str, value: str):
    try:
        selector = f'#{id}'
        page.wait_for_selector(selector, timeout=5000)  # Wait for the selector to be available
        page.fill(selector, value)
        logging.info(f"Field found with ID '{id}' and filled with: '{value}'")
    except Error as e:
        logging.error(f"An error occurred while filling field with ID '{id}': {e}")

def fill_field_by_class(page: Page, class_name: str, value: str):
    try:
        selector = f'.{class_name}'
        page.wait_for_selector(selector, timeout=5000)  # Wait for the selector to be available
        page.fill(selector, value)
        logging.info(f"Field found with class '{class_name}' and filled with: '{value}'")
    except Error as e:
        logging.error(f"An error occurred while filling field with class '{class_name}': {e}")

def click_button_by_text(page: Page, text: str):
    try:
        selector = f"text={text}"
        page.wait_for_selector(selector, timeout=5000)
        page.click(selector)
        logging.info(f"Button found with text '{text}' and clicked")
    except Error as e:
        logging.error(f"An error occurred while clicking button with text '{text}': {e}")

def click_button_by_id(page: Page, id: str):
    try:
        selector = f"#{id}"
        page.wait_for_selector(selector, timeout=5000)
        page.click(selector)
        logging.info(f"Button found with ID '{id}' and clicked")
    except Error as e:
        logging.error(f"An error occurred while clicking button with ID '{id}': {e}")

def click_button_by_class(page: Page, class_name: str):
    try:
        selector = f".{class_name}"
        page.wait_for_selector(selector, timeout=5000)
        page.click(selector)
        logging.info(f"Button found with class '{class_name}' and clicked")
    except Error as e:
        logging.error(f"An error occurred while clicking button with class '{class_name}': {e}")

def wait_for_navigation(page: Page, url: str):
    try:
        page.wait_for_url(url, timeout=10000)
        logging.info(f"Page navigated to: {url}")
    except Error as e:
        logging.error(f"An error occurred while navigating to {url}: {e}")

def download_pdf(page: Page, download_button_selector: str, download_folder='contents', new_filename= str):
    # Wait for the download link to be available and click it
    logging.info("Waiting for the download link and clicking it...")
    page.wait_for_selector(download_button_selector)
    with page.expect_download() as download_info:
        page.click(download_button_selector)
    download = download_info.value
    download_path = os.path.join(download_folder, new_filename)
    if os.path.exists(download_path):
        os.remove(download_path)
    download.save_as(download_path)
    
    logging.info(f"File downloaded and saved to {download_path}")

def click_user_menu_button(page: Page, user_menu_button_selector: str):
    try:
        page.wait_for_selector(user_menu_button_selector, timeout=5000)
        page.click(user_menu_button_selector)
        logging.info(f"User menu button found and clicked: '{user_menu_button_selector}'")
    except Error as e:
        logging.error(f"An error occurred while clicking user menu button '{user_menu_button_selector}': {e}")

def click_my_profile(page: Page, my_profile_link_selector: str):
    try:
        page.wait_for_selector(my_profile_link_selector, timeout=5000)
        page.click(my_profile_link_selector)
        logging.info(f"My Profile link found and clicked: '{my_profile_link_selector}'")
    except Error as e:
        logging.error(f"An error occurred while clicking My Profile link '{my_profile_link_selector}': {e}")
