## Auto Account Creator for 1Password

This script automates the account creation process for 1Password, including email verification, password setting, and secret key extraction.

**Table of Contents**

* [Prerequisites](#prerequisites)
* [Setup](#setup)
* [Usage](#usage)
* [Output](#output)
* [Notes](#notes)
* [Contributing](#contributing)

**Prerequisites**

* **Python 3.7 or higher:** Ensure you have Python installed on your system.
* **Playwright:** Install Playwright using pip: `pip install playwright`
* **dotenv:** Install dotenv for managing environment variables: `pip install python-dotenv`

**Setup**

1. **Create a virtual environment (recommended):**
   * It's best practice to use a virtual environment to isolate project dependencies.
   * Create a virtual environment using `python -m venv venv` (replace `venv` with your desired environment name).
   * Activate the virtual environment:
     * On Windows: `venv\Scripts\activate`
     * On macOS/Linux: `source venv/bin/activate`

2. **Install dependencies:**
   * Once the virtual environment is activated, install the required packages: `pip install -r requirements.txt`

3. **Create a `.env` file:**
   * Create a file named `.env` in the same directory as your Python script.
   * Add the following environment variables to the `.env` file, replacing the placeholders with your actual values:
     * `SIGNUP_URL`: The URL of the [Website Name] signup page.
     * `USER_NAME`: The desired username for the new account.
     * `USER_EMAIL`: The email address to use for registration.
     * `USER_PASSWORD`: The password for the new account.

**Usage**

1. **Run the script:**
   * Execute the `main.py` script from your terminal: `python main.py`
2. **Follow the prompts:**
   * The script will guide you through the process, including:
     * Entering the verification code sent to your email address.
     * Clicking buttons and filling in fields on the website.

**Output**

* The script will print the following information to the console:
    * Username
    * Email address
    * Password
    * Secret key (if available)
* A PDF file named "PDF-KEY.pdf" containing the secret key will be downloaded to the "contents" folder.

