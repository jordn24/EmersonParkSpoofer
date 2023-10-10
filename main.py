from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Function to perform the booking steps
def perform_booking():
    numOfPeople = "4"
    selected_date = "Sunday, 15 October 2023"
    startTimeHr = "15"
    startTimeMin = "0"
    endTimeHr = "17"
    endTimeMin = "0"

    driver = webdriver.Chrome()

    # Maximize the browser window
    # driver.maximize_window()

    driver.get("https://app.fairfieldcity.nsw.gov.au/bookingapp/futsal/")

    makeBookingBtn = driver.find_element(by=By.CSS_SELECTOR, value="#app > div > div > div > div.v-col-sm-12.v-col-md-4.v-col.options-side > div > div:nth-child(1) > button")
    makeBookingBtn.click()

    # Add a delay of, for example, 5 seconds before proceeding
    time.sleep(10)

    newBookingBtn = driver.find_element(by=By.CSS_SELECTOR, value="#main > button > span.v-btn__content")
    newBookingBtn.click()

    # Add a delay of, for example, 5 seconds before proceeding
    time.sleep(10)

    # Find the input field for the number of people by its CSS selector and send the number of people value
    numOfPeopleInput = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div/div[3]/div/div/div[4]/div/div[1]/div[1]/div/div[1]/div/div[3]/input")
    numOfPeopleInput.send_keys(numOfPeople)

    # Find the date element and click on it
    date_element = driver.find_element(by=By.XPATH, value=f"//span[@aria-label='{selected_date}']")
    date_element.click()

    time.sleep(2)

    # Start HR
    startHrElement = driver.find_element(by=By.XPATH, value='//*[@id="mySidenav"]/div/div/div[4]/div/div[1]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div[1]/select')
    select = Select(startHrElement)
    select.select_by_value(startTimeHr)
    
    time.sleep(5)

    # Start Min
    startMinElement = driver.find_element(by=By.XPATH, value='//*[@id="mySidenav"]/div/div/div[4]/div/div[1]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div[2]/select')
    select = Select(startMinElement)
    select.select_by_value("30")

    # Start Min
    startMinElement = driver.find_element(by=By.XPATH, value='//*[@id="mySidenav"]/div/div/div[4]/div/div[1]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div[2]/select')
    select = Select(startMinElement)
    select.select_by_value(startTimeMin)

    time.sleep(5)

    # End HR
    endHrElement = driver.find_element(by=By.XPATH, value='//*[@id="mySidenav"]/div/div/div[4]/div/div[1]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div[1]/select')
    select = Select(endHrElement)
    select.select_by_value(endTimeHr)

    time.sleep(5)

    # End Min
    endMinElement = driver.find_element(by=By.XPATH, value='//*[@id="mySidenav"]/div/div/div[4]/div/div[1]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div[2]/select')
    select = Select(endMinElement)
    select.select_by_value("30")

    # End Min
    endMinElement = driver.find_element(by=By.XPATH, value='//*[@id="mySidenav"]/div/div/div[4]/div/div[1]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div[2]/select')
    select = Select(endMinElement)
    select.select_by_value(endTimeMin)

    time.sleep(2)

    # Scroll to the search button
    searchBtn = driver.find_element(by=By.XPATH, value='//*[@id="mySidenav"]/div/div/div[4]/div/div[1]/div[3]/button/span[3]')
    driver.execute_script("arguments[0].scrollIntoView();", searchBtn)
    searchBtn.click()
    
    time.sleep(2)

    try:
        # Scroll to the expand button
        expand = driver.find_element(by=By.XPATH, value='//*[@id="mySidenav"]/div/div/div[4]/div/div[2]/div/div[2]/div/div/span')
        driver.execute_script("arguments[0].scrollIntoView();", expand)
        expand.click()
        # Scroll to the book button
        bookBtn = driver.find_element(by=By.XPATH, value='//*[@id="mySidenav"]/div/div/div[4]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[3]/div[3]/button/span[3]')
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
