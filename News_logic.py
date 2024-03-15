from newsdataapi import NewsDataApiClient
import sys
sys.path.append("C:\\Users\\diyaa\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages")


class News:
    API_KEY = 'API KEY'
    """

    A class to interact with a news API and retrieve articles based on specific criteria.

    Attributes:
        API_KEY (str): The API key used to authenticate with the news API.
        api (NewsDataApiClient): An instance of the NewsDataApiClient class for making API requests.
    """

    def __init__(self, API_KEY):
        
        """
        Initializes the News class with the provided API key.

        Args:
            API_KEY (str): The API key used to authenticate with the news API.
        """
        self.api = NewsDataApiClient(apikey=API_KEY)

    def get_articles(self, query, country, lan ):
        """
        Retrieves articles from the news API based on the provided query, country, and language.

        Args:
            query (str): The search query used to filter articles.
            country (str): The country code (ISO 3166-1 alpha-2) for filtering articles by country.
            lan (str): The language code (ISO 639-1) for filtering articles by language.

        Returns:
            str: A formatted string containing information about the retrieved articles.
        """
        # Retrieve articles from the news API
        response = self.api.news_api(q=query, country=country, language=lan)
        result_string = ""
        articles = response.get('results', [])

        # Extract relevant information from each article
        article_info = [(art.get('title', ''), art.get('description', ''), art.get('content', ''), art.get('link', '')) for art in articles]
        
        # Format the retrieved article information into a string
        for title, description, content, link in article_info:
            result_string += f"Title: {title}\nDescription: {description}\nContent: {content}\nLink: {link}\n\n"

        return result_string

# # Instantiate the News class with the API key
news = News(API_KEY='API KEY')
# #q=input("Enter the query : ")
# # Retrieve and print articles based on the specified query, country, and language
print(news.get_articles(query = "top 10 most powerful militaries in the world", country = "us", lan = "en"))