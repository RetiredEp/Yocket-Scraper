from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time

# Configure Chrome options
options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--headless')  # Uncomment if you need headless mode

# Initialize ChromeDriver
service = Service(executable_path=r"C:\Users\DELL\Desktop\Web_Scraping\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

# Initialize a list to store profile data
data = []

try:
    # Navigate to the Yocket login page
    driver.get("https://yocket.com/login")
    print("IN THE YOCKET LOGIN PAGE\n")
    
    # Wait and enter phone number
    time.sleep(3)
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#mobileInput'))
    ).send_keys("9247946789")
    
    # Wait and click the next button
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#__nuxt > div > div > div.flex.flex-col.grow.w-\[44\%\].shadow-2xl.bg-white.h-full.overflow-y-scroll.overflow-x-hidden > div > div.flex.flex-col.justify-between.h-full > div > div.px-4.md\:px-0 > form > div.mt-6.sticky.z-10 > button'))
    ).click()
    print("ENTERED THE MOBILE NUMBER. OTP EXPECTED ....\n")

    # Input OTP 
    otp = input("ENTER OTP:\n")
    time.sleep(30)
    # WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, '#firstinput'))
    # ).send_keys(otp[0])
    # print(otp[0])
    # WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, '#secondinput'))
    # ).send_keys(otp[1])
    # WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, '#thirdinput'))
    # ).send_keys(otp[2])
    # WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, '#fourthinput'))
    # ).send_keys(otp[3])
    # WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, '#fifthinput'))
    # ).send_keys(otp[4])
    # WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, '#sixthinput'))
    # ).send_keys(otp[5])
    
    # for index, digit in enumerate(otp):
    #     WebDriverWait(driver, 20).until(
    #         EC.presence_of_element_located((By.XPATH, f'/html/body/div[1]/div/div/div[2]/div/form/div[1]/div[1]/div[1]/input[{index+1}]'))
    #     ).send_keys(digit)

    # # Click the submit button
    # WebDriverWait(driver, 20).until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, '#verify-otp > button'))
    # ).click()
    # print("OTP SUBMITTED \n")

    # Clicking "Admits & Rejects"
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#connect-feature > span'))
    ).click()
    print("INSIDE THE ADMITS AND REJECTS\n")

    # clicking on course
    WebDriverWait(driver,20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'#Course-filter-toggle > div > div.flex.flex-row.w-full > p.text-sm.select-none.whitespace-nowrap.grow.border-black'))
    ).click()
    # clicking on clear
    WebDriverWait(driver,20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'#__nuxt > div > main > div > div > div.bg-white.py-8.rounded-md.shadow-md.lg\:px-12 > div.filter-bar.flex.grid-cols-2.gap-y-4.gap-x-3.w-full.mt-5.overflow-y-auto.px-2.lg\:px-0 > div.Course-filter-component.mx-auto.lg\:mx-0 > div:nth-child(2) > div > div > div.mt-2.flex.flex-row.justify-between.p-4.lg\:px-2.border-t.border-yocket-neutral-300.border-opacity-100.absolute.lg\:relative.bottom-0.lg\:bottom-auto.w-full > button.font-bold.text-sm.text-yocket-red-400'))
    ).click()
    # clicking on apply
    WebDriverWait(driver,20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'#__nuxt > div > main > div > div > div.bg-white.py-8.rounded-md.shadow-md.lg\:px-12 > div.filter-bar.flex.grid-cols-2.gap-y-4.gap-x-3.w-full.mt-5.overflow-y-auto.px-2.lg\:px-0 > div.Course-filter-component.mx-auto.lg\:mx-0 > div:nth-child(2) > div > div > div.mt-2.flex.flex-row.justify-between.p-4.lg\:px-2.border-t.border-yocket-neutral-300.border-opacity-100.absolute.lg\:relative.bottom-0.lg\:bottom-auto.w-full > button.text-yocket-neutral-0.bg-yocket-orange-700.w-20.py-2.inline-flex.items-center.justify-center.border.border-transparent.shadow-sm.text-sm.rounded-md.font-semibold'))
    ).click()
    print("ENABLED THE RESET ALL OPTION IN FILTERS\n")

    # clicking on reset all
    WebDriverWait(driver,20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,r'#__nuxt > div > main > div > div > div.bg-white.py-8.rounded-md.shadow-md.lg\:px-12 > div.filter-bar.flex.grid-cols-2.gap-y-4.gap-x-3.w-full.mt-5.overflow-y-auto.px-2.lg\:px-0 > div.reset-component.mx-auto.lg\:mx-0 > button > div > p'))
    ).click()

    # clicking on application status
    WebDriverWait(driver,20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'#Application-Status-filter-toggle > div > div.flex.flex-row.w-full > p.text-sm.select-none.whitespace-nowrap.grow.border-yocket-neutral-500'))
    ).click()

    # clicking on admitted 
    WebDriverWait(driver,20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'#__nuxt > div > main > div > div > div.bg-white.py-8.rounded-md.shadow-md.lg\:px-12 > div.filter-bar.flex.grid-cols-2.gap-y-4.gap-x-3.w-full.mt-5.overflow-y-auto.px-2.lg\:px-0 > div.Application-Status-filter-component.mx-auto.lg\:mx-0 > div:nth-child(2) > div > div > div.flex.flex-col > div.px-4.lg\:px-0 > div > div:nth-child(5)'))
    ).click()
   
    # clicking on apply
    WebDriverWait(driver,20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'#__nuxt > div > main > div > div > div.bg-white.py-8.rounded-md.shadow-md.lg\:px-12 > div.filter-bar.flex.grid-cols-2.gap-y-4.gap-x-3.w-full.mt-5.overflow-y-auto.px-2.lg\:px-0 > div.Application-Status-filter-component.mx-auto.lg\:mx-0 > div:nth-child(2) > div > div > div.mt-2.flex.flex-row.justify-between.p-4.lg\:px-2.border-t.border-yocket-neutral-300.border-opacity-100 > button.text-yocket-neutral-0.bg-yocket-orange-700.w-20.py-2.inline-flex.items-center.justify-center.border.border-transparent.shadow-sm.text-sm.rounded-md.font-semibold'))
    ).click()
    # clicking on country
    WebDriverWait(driver,20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'#Country-filter-toggle > div > div.flex.flex-row.w-full > p.text-sm.select-none.whitespace-nowrap.grow.border-yocket-neutral-500'))
    ).click()
    # clicking on search
    WebDriverWait(driver,20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'#search_Country'))
    ).click()
    # clicking usa
    WebDriverWait(driver,20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'#__nuxt > div > main > div > div > div.bg-white.py-8.rounded-md.shadow-md.lg\:px-12 > div.filter-bar.flex.grid-cols-2.gap-y-4.gap-x-3.w-full.mt-5.overflow-y-auto.px-2.lg\:px-0 > div.Country-filter-component.mx-auto.lg\:mx-0 > div:nth-child(2) > div > div > div.flex.flex-col > div.px-4.lg\:px-0 > div > div.list-component.hidden.lg\:block > div > div > div:nth-child(1) > div > p'))
    ).click()

    # clicking apply
    WebDriverWait(driver,20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'#__nuxt > div > main > div > div > div.bg-white.py-8.rounded-md.shadow-md.lg\:px-12 > div.filter-bar.flex.grid-cols-2.gap-y-4.gap-x-3.w-full.mt-5.overflow-y-auto.px-2.lg\:px-0 > div.Country-filter-component.mx-auto.lg\:mx-0 > div:nth-child(2) > div > div > div.mt-2.flex.flex-row.justify-between.p-4.lg\:px-2.border-t.border-yocket-neutral-300.border-opacity-100.absolute.lg\:relative.bottom-0.lg\:bottom-auto.w-full > button.text-yocket-neutral-0.bg-yocket-orange-700.w-20.py-2.inline-flex.items-center.justify-center.border.border-transparent.shadow-sm.text-sm.rounded-md.font-semibold'))
    ).click()

    # clicking on course
    WebDriverWait(driver,20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'#Course-filter-toggle > div > div.flex.flex-row.w-full > p.text-sm.select-none.whitespace-nowrap.grow.border-black'))
    ).click()

    # clicking on search
    WebDriverWait(driver,20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'#search_Course'))
    ).click()
    # clicking on computer science
    WebDriverWait(driver,20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'#__nuxt > div > main > div > div > div.bg-white.py-8.rounded-md.shadow-md.lg\:px-12 > div.filter-bar.flex.grid-cols-2.gap-y-4.gap-x-3.w-full.mt-5.overflow-y-auto.px-2.lg\:px-0 > div.Course-filter-component.mx-auto.lg\:mx-0 > div:nth-child(2) > div > div > div.flex.flex-col > div.px-4.lg\:px-0 > div > div.list-component.hidden.lg\:block > div > div > div:nth-child(1) > div > p'))
    ).click()
    # clicking on apply
    WebDriverWait(driver,20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'#__nuxt > div > main > div > div > div.bg-white.py-8.rounded-md.shadow-md.lg\:px-12 > div.filter-bar.flex.grid-cols-2.gap-y-4.gap-x-3.w-full.mt-5.overflow-y-auto.px-2.lg\:px-0 > div.Course-filter-component.mx-auto.lg\:mx-0 > div:nth-child(2) > div > div > div.mt-2.flex.flex-row.justify-between.p-4.lg\:px-2.border-t.border-yocket-neutral-300.border-opacity-100.absolute.lg\:relative.bottom-0.lg\:bottom-auto.w-full > button.text-yocket-neutral-0.bg-yocket-orange-700.w-20.py-2.inline-flex.items-center.justify-center.border.border-transparent.shadow-sm.text-sm.rounded-md.font-semibold'))
    ).click()
    
    # clicking on intake
    WebDriverWait(driver,20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'#Intake-filter-toggle'))
    ).click()

    # clicking on 2025
    WebDriverWait(driver,20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'#__nuxt > div > main > div > div > div.bg-white.py-8.rounded-md.shadow-md.lg\:px-12 > div.filter-bar.flex.grid-cols-2.gap-y-4.gap-x-3.w-full.mt-5.overflow-y-auto.px-2.lg\:px-0 > div.Intake-filter-component.mx-auto.lg\:mx-0 > div:nth-child(2) > div > div > div.flex.flex-col > div.px-4.lg\:px-0 > div.grid.gap-3.justify-center.items-center.py-4.grid-cols-5 > div:nth-child(6)'))
    ).click()

    # clicking on apply
    WebDriverWait(driver,20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'#__nuxt > div > main > div > div > div.bg-white.py-8.rounded-md.shadow-md.lg\:px-12 > div.filter-bar.flex.grid-cols-2.gap-y-4.gap-x-3.w-full.mt-5.overflow-y-auto.px-2.lg\:px-0 > div.Intake-filter-component.mx-auto.lg\:mx-0 > div:nth-child(2) > div > div > div.mt-2.flex.flex-row.justify-between.p-4.lg\:px-2.border-t.border-yocket-neutral-300.border-opacity-100.absolute.lg\:relative.bottom-0.lg\:bottom-auto.w-full > button.text-yocket-neutral-0.bg-yocket-orange-700.w-20.py-2.inline-flex.items-center.justify-center.border.border-transparent.shadow-sm.text-sm.rounded-md.font-semibold'))
    ).click()

    ############################################################

    # Clicking "Load more" to show all profiles
    for _ in range(1,50 ):
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#__nuxt > div > main > div > div > div:nth-child(2) > div > div:nth-child(2) > div.flex.justify-center.items-center.mt-6.mb-4 > button'))
        ).click()

    # Extract data from each profile card on the main page
    for i in range(1,401):  # Adjust the range as needed
        profile_xpath = f'/html/body/div[1]/div/main/div/div/div[2]/div/div[2]/div[1]/div[{i}]'

        # Extract data from the profile card
        try:
            name = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, f'{profile_xpath}/div[1]/div/div[2]/div[1]/div/div/span'))
            ).text
            intake_year = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, f'{profile_xpath}/div[1]/div/div[2]/div[2]/div/span[3]'))
            ).text
            intake_sem = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, f'{profile_xpath}/div[1]/div/div[2]/div[2]/div/span[2]'))
            ).text
            university_applied = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, f'{profile_xpath}/div[2]/div[2]/span/div/a'))
            ).text
            course_applied = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, f'{profile_xpath}/div[2]/div[2]/div/span/div/a'))
            ).text

            # Initialize test scores dictionary with default values
            test_scores = {"GRE": "-1", "IELTS": "-1", "TOEFL": "-1"}

            test_scores_xpath = f'{profile_xpath}/div[3]/div/div'

            # Check for single test name and score pair
            test_elements = driver.find_elements(By.XPATH, f'{test_scores_xpath}')
            if len(test_elements) == 1:
                test_name_xpath = f'{test_scores_xpath}/div/p/span[1]'
                test_score_xpath = f'{test_scores_xpath}/div/p/span[2]'
                test_name = driver.find_element(By.XPATH, test_name_xpath).text
                test_score = driver.find_element(By.XPATH, test_score_xpath).text
                if test_name in test_scores:
                    test_scores[test_name] = test_score
            else:
                # Handle multiple test name and score pairs
                for index in range(1, 4):  # Adjust the range if needed
                    test_name_xpath = f'{test_scores_xpath}/div[{index}]/p/span[1]'
                    test_score_xpath = f'{test_scores_xpath}/div[{index}]/p/span[2]'
                    if driver.find_elements(By.XPATH, test_name_xpath):
                        test_name = driver.find_element(By.XPATH, test_name_xpath).text
                        test_score = driver.find_element(By.XPATH, test_score_xpath).text
                        if test_name in test_scores:
                            test_scores[test_name] = test_score
            print(f"GOT THE PROFILE CARD DETAILS OF STUDENT {i}\n")
        except Exception as e:
            print(f"Error extracting profile details: {e}")
            continue

        # Compile all data into a dictionary and append it to the list
        profile_data = {
            "Name": name,
            "Intake Year": intake_year,
            "Intake Sem": intake_sem,
            "University Applied": university_applied,
            "Course Applied": course_applied,
            "GRE": test_scores.get("GRE", "-"),
            "IELTS": test_scores.get("IELTS", "-"),
            "TOEFL": test_scores.get("TOEFL", "-"),
        }
        data.append(profile_data)

finally:
    # Close the browser
    driver.quit()

    # Create a DataFrame from the collected data and save it to a CSV file
    df = pd.DataFrame(data)
    df.to_csv('yocket_profiles_new.csv', index=False)
