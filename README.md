# Yocket Profile Scraper

This project is a web scraping script that extracts profile data from the Yocket website using Selenium and BeautifulSoup. The script automates the process of logging in, navigating through the website, and collecting information about student profiles.

## Prerequisites

- Python 3.11 or higher
- ChromeDriver (ensure it matches the version of your Chrome browser)
- Required Python libraries

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd my_project
   ```

2. **Set up a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # or `venv\Scripts\activate` on Windows
   ```

3. **Install the required Python packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Download ChromeDriver:**

   - Ensure that you download the version of ChromeDriver that matches your Chrome browser version from [here](https://sites.google.com/chromium.org/driver/).
   - Place the `chromedriver.exe` file in a suitable location and update the `service` path in the script accordingly.

## Usage

1. **Activate the virtual environment:**

   ```bash
   source venv/bin/activate  # or `venv\Scripts\activate` on Windows
   ```

2. **Run the script:**

   ```bash
   python yocket_profiles_scraping.py
   ```

   - You will be prompted to enter your OTP after the script navigates to the login page.

3. **Output:**

   - The script collects profile data and saves it to `yocket_profiles.csv` in the project directory.

## Script Overview

- **Configuration**: Configures Chrome options and initializes the ChromeDriver.
- **Login**: Automates the login process by entering the phone number and OTP.
- **Navigation**: Navigates through various sections of the Yocket website to apply filters.
- **Data Extraction**: Extracts profile details including names, intake years, universities applied to, and test scores.
- **Output**: Saves the collected data into a CSV file.

## Requirements

- `selenium`
- `beautifulsoup4`
- `pandas`

Ensure these are listed in the `requirements.txt` file:

```
selenium
beautifulsoup4
pandas
```

## Troubleshooting

- **Chromedriver Path**: Make sure the path to `chromedriver.exe` in the script matches the location where you have stored it.
- **Dependencies**: Ensure all required libraries are installed correctly. If you encounter issues, consider reinstalling the libraries or checking for version compatibility.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
