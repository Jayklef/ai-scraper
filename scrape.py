import selenium.webdriver as webdriver
import time




def scrape_website(website):
    print("Launching chrome browser....")
    
    options = webdriver.ChromeOptions()
    
    
    # By leaving out the service parameter, Selenium Manager handles the driver automatically
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get(website)
        print("page loaded...")
        html = driver.page_source
        time.sleep(10)
        
        return html
    
    finally:
        driver.quit()