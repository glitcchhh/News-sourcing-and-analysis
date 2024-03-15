import requests
from bs4 import BeautifulSoup

def fetch_article_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # Extract text content from the parsed HTML
            text_content = ' '.join([p.get_text() for p in soup.find_all('p')])
            return text_content
        else:
            print(f"Failed to fetch content for URL: {url}. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred while fetching content for URL: {url}. Error: {str(e)}")
        return None

def fetch_news(api_key, query, count=10, country='us', search_lang='en', spellcheck=1):
    url = f"https://api.search.brave.com/res/v1/news/search"
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip",
        "X-Subscription-Token": api_key
    }
    params = {
        "q": query,
        "count": count,
        "country": country,
        "search_lang": search_lang,
        "spellcheck": spellcheck
    }
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        news_data = response.json()
        for item in news_data.get('results', []):
            article_url = item.get('url')
            if article_url:
                count=1
                content = fetch_article_content(article_url)
                item['content'] = content
                print(f"-------------------------{count}----------------------------")
                count=count+1
                print(content)                          #this will print the website content
        return news_data
    else:
        print(f"Failed to fetch news data. Status code: {response.status_code}")
        return None

# Example usage:
api_key = "API KEY"
query = "munich"
news_data = fetch_news(api_key, query)
print(news_data)  # This will print the JSON response from the API
