from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome in headless mode
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--start-maximized')

# Initialize the driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open the HTML file
file_path = 'file:///Users/divyadhole/Capstone-project/poster/Clean_Theme.html'
driver.get(file_path)

# Wait for the page to load
time.sleep(2)

# Set window size (adjust as needed)
driver.set_window_size(1400, 2000)

# Take screenshot
driver.save_screenshot('poster.png')
print("Screenshot saved as poster.png")

# Generate PDF (optional)
driver.execute_script('document.body.style.zoom = "100%"')  # Reset zoom
driver.execute_script('window.scrollTo(0, 0)')  # Scroll to top
pdf_data = driver.execute_cdp_cmd('Page.printToPDF', {
    'landscape': False,
    'printBackground': True,
    'paperWidth': 11.69,  # A4 width in inches
    'paperHeight': 16.53,  # A4 height in inches
    'marginTop': 0,
    'marginBottom': 0,
    'marginLeft': 0,
    'marginRight': 0
})

# Save PDF
import base64
with open('poster.pdf', 'wb') as f:
    f.write(base64.b64decode(pdf_data['data']))
    
print("PDF saved as poster.pdf")
driver.quit()