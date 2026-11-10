import selenium.webdriver as webdriver
import time
from bs4 import BeautifulSoup




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
        
        

def extract_content(html_content):
    soup = BeautifulSoup(html_content, 'html_parser')
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""


def clean_data(body_content):
    soup = BeautifulSoup(body_content, 'html.parser')
    
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()
        
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )
    
    return cleaned_content