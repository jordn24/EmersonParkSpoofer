from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Function to perform the booking steps
def perform_booking():
    numOfPeople = "4"
    selected_date = "Sunday, 15 October 2023"
    startTimeHr = "8"
    startTimeMin = "30"
    endTimeHr = "10"
    endTimeMin = "30"

    driver = webdriver.Chrome()

    driver.get("https://app.fairfieldcity.nsw.gov.au/bookingapp/futsal/")

    # Wait for the "Make Booking" button to be clickable
    makeBookingBtn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#app > div > div > div > div.v-col-sm-12.v-col-md-4.v-col.options-side > div > div:nth-child(1) > button"))
    )
    makeBookingBtn.click()

    newBookingBtn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#main > button > span.v-btn__content"))
    )
    newBookingBtn.click()

    # Find the input field for the number of people and send the number of people value
    numOfPeopleInput = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[3]/div/div/div[4]/div/div[1]/div[1]/div/div[1]/div/div[3]/input"))
    )
    numOfPeopleInput.send_keys(numOfPeople)

    # Find the date element and click on it
    date_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//span[@aria-label='{selected_date}']"))
    )
    date_element.click()

    # Start HR
    startHrElement = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="mySidenav"]/div/div/div[4]/div/div[1]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div[1]/select'))
    )
    select = Select(startHrElement)
    select.select_by_value(startTimeHr)

    # Start Min
    startMinElement = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="mySidenav"]/div/div/div[4]/div/div[1]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div[2]/select'))
    )
    select = Select(startMinElement)
    select.select_by_value("30")

        # Start Min
    startMinElement = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="mySidenav"]/div/div/div[4]/div/div[1]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div[2]/select'))
    )
    select = Select(startMinElement)
    select.select_by_value(startTimeMin)

    # End HR
    endHrElement = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="mySidenav"]/div/div/div[4]/div/div[1]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div[1]/select'))
    )
    select = Select(endHrElement)
    select.select_by_value(endTimeHr)

    # End Min
    endMinElement = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="mySidenav"]/div/div/div[4]/div/div[1]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div[2]/select'))
    )
    select = Select(endMinElement)
    select.select_by_value("30")

        # End Min
    endMinElement = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="mySidenav"]/div/div/div[4]/div/div[1]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div[2]/select'))
    )
    select = Select(endMinElement)
    select.select_by_value(endTimeMin)

    # Scroll to the search button
    searchBtn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="mySidenav"]/div/div/div[4]/div/div[1]/div[3]/button/span[3]'))
    )
    driver.execute_script("arguments[0].scrollIntoView();", searchBtn)
    searchBtn.click()


    try:
        # Scroll to the expand button
        expand = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mySidenav"]/div/div/div[4]/div/div[2]/div/div[2]/div/div/span'))
        )
        driver.execute_script("arguments[0].scrollIntoView();", expand)
        expand.click()
        
        # Scroll to the book button
        bookBtn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mySidenav"]/div/div/div[4]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[3]/div[3]/button/span[3]'))
        )
        driver.execute_script("arguments[0].scrollIntoView();", bookBtn)
        bookBtn.click()
        print("Blocked.")
        time.sleep(10)
    except Exception as e:
        print(f"Error: {str(e)}")
        print("Booking is already blocked.")  # If the 'expand' element is not found, continue without clicking it

    driver.quit()

# Run the script indefinitely
while True:
    try:
        perform_booking()
    except Exception as e:
        print(f"Error: {str(e)}")

    time.sleep(300)
