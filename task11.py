from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open the URL
driver.get("https://jqueryui.com/droppable/")

# Wait for the page to load completely
time.sleep(2)

# Switch to the iframe that contains the droppable elements
driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "demo-frame"))

# Locate the draggable and droppable elements
draggable = driver.find_element(By.ID, "draggable")
droppable = driver.find_element(By.ID, "droppable")

# Perform the drag and drop action
actions = ActionChains(driver)
actions.drag_and_drop(draggable, droppable).perform()

# Optional: Wait a bit to see the result
time.sleep(2)

# Close the driver
driver.quit()