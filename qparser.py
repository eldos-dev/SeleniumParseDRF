import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://finance.yahoo.com/?guccounter=1")
    time.sleep(2)

    search_box = driver.find_element_by_name('yfin-usr-qry')
    search_box.send_keys('ZUO')

    time.sleep(2)
    search_box.submit()
    driver.get("https://finance.yahoo.com/quote/ZUO/history?p=ZUO")
    time.sleep(2)
    driver.get('https://query1.finance.yahoo.com/v7/finance/download/ZUO?period1=1523491200&period2=1617235200&interval=1d&events=history&includeAdjustedClose=true').submit()


# if __name__ == "__main__":
#     main()