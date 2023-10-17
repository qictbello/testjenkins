from selenium import webdriver

# Set up the WebDriver
driver = webdriver.Firefox()  # You can use a different browser driver

# Navigate to localhost:5050
driver.get("http://localhost:5050")

# Find and click on the "about" link
about_link = driver.find_element_by_link_text("About")
about_link.click()

# Verify the response, e.g., check the title or content
assert "About Page" in driver.title

# Navigate back to the homepage
driver.get("http://localhost:5050")

# Find and click on the "works" link
works_link = driver.find_element_by_link_text("Works")
works_link.click()

# Verify the response for the "works" page
assert "Works Page" in driver.title

# Close the browser
driver.quit()
