from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import base64

def save_poster():
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run in headless mode
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--window-size=1920,1080')  # Set a larger window size
    
    # For better PDF printing
    chrome_options.add_argument('--disable-software-rasterizer')
    chrome_options.add_argument('--print-to-pdf-no-header')
    chrome_options.add_argument('--disable-gpu-sandbox')
    
    # Initialize the Chrome driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        # Get the absolute path to the HTML file
        html_path = os.path.abspath('Clean_Theme.html')
        print(f"Loading HTML file from: {html_path}")
        
        # Load the local HTML file
        driver.get(f'file://{html_path}')
        
        # Wait for content to load
        print("Waiting for content to load...")
        time.sleep(5)  # Adjust this delay if needed
        
        # Ensure the output directory exists
        os.makedirs('output', exist_ok=True)
        
        # Save as PNG
        png_path = os.path.abspath('output/poster.png')
        driver.set_window_size(1920, 3000)  # Adjust height to fit your poster
        driver.save_screenshot(png_path)
        print(f"Saved screenshot to: {png_path}")
        
        # Save as PDF using Chrome's print to PDF
        print("Generating PDF...")
        pdf_path = os.path.abspath('output/poster.pdf')
        
        # Set up print options
        params = {
            'landscape': False,
            'paperWidth': 11.7,  # A3 width in inches
            'paperHeight': 16.5,  # A3 height in inches
            'scale': 0.8,
            'printBackground': True,
            'marginTop': 0,
            'marginBottom': 0,
            'marginLeft': 0,
            'marginRight': 0
        }
        
        try:
            # First try the standard CDP method
            result = driver.execute_cdp_cmd('Page.printToPDF', params)
            if 'data' in result:
                with open(pdf_path, 'wb') as f:
                    try:
                        f.write(base64.b64decode(result['data']))
                        print(f"Saved PDF to: {pdf_path}")
                    except Exception as e:
                        print(f"Error decoding PDF data: {str(e)}")
                        raise
            else:
                raise Exception("No data in PDF response")
                
        except Exception as e:
            print(f"CDP method failed, trying alternative method: {str(e)}")
            try:
                # Alternative method using print page
                from selenium.webdriver.common.print_page_options import PrintOptions
                
                print_options = PrintOptions()
                print_options.page_width = 11.7
                print_options.page_height = 16.5
                print_options.scale = 0.8
                print_options.background = True
                print_options.margin_top = 0
                print_options.margin_bottom = 0
                print_options.margin_left = 0
                print_options.margin_right = 0
                
                pdf_data = driver.print_page(print_options)
                with open(pdf_path, 'wb') as f:
                    f.write(pdf_data.encode('utf-8'))
                print(f"Saved PDF (alternative method) to: {pdf_path}")
                
            except Exception as e2:
                print(f"Alternative PDF method failed: {str(e2)}")
                print("Falling back to screenshot method...")
                driver.save_screenshot(pdf_path.replace('.pdf', '_fallback.png'))
                print(f"Saved fallback screenshot to: {pdf_path.replace('.pdf', '_fallback.png')}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        # Close the browser
        driver.quit()
        print("Done!")

if __name__ == "__main__":
    save_poster()