from bs4 import BeautifulSoup
import pandas as pd
import os
import re
from datetime import datetime
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

class EccCollector:
    def __init__(self, pathtosave="") -> None:
        """
        Initialize the Chrome Driver and set the path to save the articles.
        Input: pathtosave: str
        """
        self.pathtosave = pathtosave
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--headless")
        self.options.add_argument('--enable-javascript')
        logging.info("Initializing Chrome Driver...")
        self.driver = webdriver.Chrome(options=self.options, service=ChromeService(ChromeDriverManager().install()))
        logging.info("Chrome Driver initialized.")

    def getArticleList(self, company_symbol, page_range=2) -> pd.DataFrame:
        """
        Get the list of ECC for a company.
        Input: company_symbol: str
               page_range: int (default: 2)
        Output: transcripts_df: pd.DataFrame
        """
        current_page = 1
        page = []
        next_page = True
        while next_page:
            time.sleep(10)
            articlesList = self._findArticleListOnPage(company_symbol, current_page)
            for i in articlesList:
                title = i.text.split('\n')[0]
                url = i.find_element(By.TAG_NAME, 'a').get_attribute('href').split('?')[0]
                year = self._findYear(title)
                quarter = self._findQuarter(title)
                logging.info(f"Getting article {title}...")
                page.append([title, url, year, quarter])
            current_page += 1
            next_page = True if current_page <= page_range and len(articlesList) > 0 else False
        logging.info(f"{len(page)} articles have been saved for {company_symbol}.")
        transcripts_df = pd.DataFrame(page, columns=['ecc_title', 'ecc_url', 'year', 'quarter'])
        transcripts_df.to_csv(f'{company_symbol}_transcripts.csv', index=False)
        logging.info(f"Article list for {company_symbol} saved as {company_symbol}_transcripts.csv.")
        return transcripts_df
    
    def _findArticleListOnPage(self, company_symbol, current_page) -> list:
        """
        helper function to find the list of articles on a page.
        Input: company_symbol: str
               current_page: int
        Output: articles_list: list
        """
        list_url = f"https://seekingalpha.com/symbol/{company_symbol}/earnings/transcripts?page={current_page}"
        self.driver.get(list_url)
        try:
            time.sleep(10)
            self.press_and_hold()
        except:
            pass
        path_of_list = '//*[@id="content"]/div[2]/div/div[3]/div/div[1]/div[2]/div/section/div/div/div/div[2]'
        path_list = self.driver.find_element(By.XPATH, path_of_list)
        articles_list = path_list.find_elements(By.TAG_NAME, 'article')
        return articles_list

    def _findYear(self, title) -> str:
        """
        helper function to find the year of the article.
        Input: title: str
        Output: year: str
        """
        year = re.search(r'\d{4}', title)
        return "N/A" if year is None else year.group()

    def _findQuarter(self, title) -> str:
        """
        helper function to find the quarter of the article.
        Input: title: str
        Output: quarter: str
        """
        quarter = re.search(r'Q\d', title)
        return "N/A" if quarter is None else quarter.group()

    def _extract_article_from_html(self, html, title, pathtosave=""):
        """
        helper function to extract the article from the html, and save the file to configured path.
        Input: html: str
                title: str
        Output: results: str
        """
        soup = BeautifulSoup(html, 'html.parser')
        # get where id = content
        content = soup.find(id='content')
        results = content.find_all('p')
        content = list(map(lambda p: p.text, results))
        results = '\n'.join(content)
        # with open(f"{pathtosave}/{title}.txt", "w", encoding='utf-8') as f:
        #     f.write(results)
        return results

    def getSingleArticle(self, articlelink: str, title, save=False, pathtosave="") -> str:
        """
        Get a single article from the article link.
        Input: articlelink: str
               title: str
        Output: content: str
        """
        logging.info(f"Getting article {title}...")
        self.driver.get(articlelink)
        html = self.driver.page_source
        content = self._extract_article_from_html(html, title)
        if save:
            with open(f"{pathtosave}/{title}.txt", "w", encoding='utf-8') as f:
                f.write(content)
                f.close()
            logging.info(f"Article {title} saved.")
        return content

    def getArticles(self, article_list: pd.DataFrame, number=5) -> pd.DataFrame:
        """
        Get articles from the article list.
        Input: article_list: pd.DataFrame
               number: int (default: 5)
        Output: article_list: pd.DataFrame
        """
        for index, row in article_list.iterrows():
            if index == number:
                break
            try:
                self.getSingleArticle(row['ecc_url'], row['ecc_title'])
            except Exception as e:
                logging.info(f"Verification Issues with {row['title']} {e}")
                self.press_and_hold()

    def press_and_hold(self):
        captcha_element = self.driver.find_element(
            By.ID, value='px-captcha-wrapper').find_element(
            By.XPATH, value='//div[@aria-label="Press & Hold"]'
        )

        ActionChains(self.driver).click_and_hold(on_element=captcha_element).perform()
        

if __name__ == "__main__":
    ecc = EccCollector(os.getcwd())
    # try:
    #     article_list = ecc.getArticleList("AAPL")
    # except:
    #     logging.info("Verification Issues")
    #     ecc.press_and_hold()

    ## Testing ##
    logging.info("Getting articles...")
    article_list = ecc.getArticleList("AMZN", 1)
    print(article_list)

    # article_list = pd.read_csv("AAPL_transcripts.csv")
    ecc.getArticles(article_list, 2)