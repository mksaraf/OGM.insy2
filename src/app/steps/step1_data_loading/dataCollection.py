# Data collection from arXiv
import arxivloader
import json

def load_and_save_articles(keyword, prefix, columns, output_file):
    """
    Loads articles from arXiv using the arxivloader library and saves them to a JSON file.

    Parameters:
    keyword (str): The keyword to search for in the article titles.
    prefix (str): The prefix to use in the search query (e.g. "all", "astro-ph", etc.).
    columns (list): The columns to retrieve from the articles (e.g. ["id", "title", "authors"]).
    output_file (str): The file path to save the articles to.

    Returns:
    None
    """
    # Define the search query
    query = "search_query={pf}:{kw}".format(pf=prefix, kw=keyword)

    # Load the articles
    df = arxivloader.load(query, columns=columns)

    # Save the articles to a JSON file
    df.to_json(output_file, orient="records")

    print(f"Articles saved to {output_file}")


# Data Collection from Url as Text
import requests
import json

def load_and_save_text_url(output_file):
    """
    Loads the State of the Union data from a URL and saves it to a JSON file.
    Parameters:
    output_file (str): The file path to save the data to.
    Returns:
    dict: The loaded data.
    """
    # Define the URL
    url = "https://raw.githubusercontent.com/langchain-ai/langchainjs/refs/heads/main/examples/state_of_the_union.txt"

    try:
        # Load the data from the URL
        res = requests.get(url)
        res.raise_for_status()  # Raise an exception for HTTP errors
    except requests.exceptions.RequestException as e:
        print(f"Error loading data from URL: {e}")
        return None

    data = {"content": res.text}

    try:
        with open(output_file, "w") as f:
            json.dump(data, f, indent=4)  # Pretty-print the JSON with indentation
    except Exception as e:
        print(f"Error saving data to file: {e}")
        return None

    print(f"State of the Union data saved to {output_file}")
    return data

# Pinecone Dataset Loading
import json
import numpy as np
from pinecone_datasets import load_dataset


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

def load_pc_dataset(output_file):
    """
    Loads the Quora dataset, preprocesses it, and saves it to a JSON file.
    Parameters:
    output_file (str): The file path to save the data to.
    Returns:
    None
    """
    # Load the Quora dataset
    dataset = load_dataset('quora_all-MiniLM-L6-bm25')

    # Preprocess the dataset
    dataset.documents.drop(['metadata'], axis=1, inplace=True)
    dataset.documents.rename(columns={'blob': 'metadata'}, inplace=True)
    dataset.documents.drop(dataset.documents.index[320_000:], inplace=True)
    dataset.documents.drop(dataset.documents.index[:240_000], inplace=True)

    # Save the data to a JSON file in chunks
    chunk_size = 1000
    for i in range(0, len(dataset.documents), chunk_size):
        chunk = dataset.documents.iloc[i:i+chunk_size].to_dict(orient='records')
        with open(output_file, 'a') as f:
            for row in chunk:
                json.dump(row, f, cls=NumpyEncoder)
                f.write('\n')

    print(f"Quora dataset saved to {output_file}")

# Scraping a Website
import json
from langchain.document_loaders import WebBaseLoader

def scrape_website(url_path, output_file):
    """
    Scrapes all the pages of a website and saves the details to a JSON file.
    Parameters:
    url_path (str): The URL of the website to scrape.
    Returns:
    None
    """
    loader = WebBaseLoader(url_path)
    docs = loader.load()

    data = []
    for doc in docs:
        page_data = {
            "page_content": doc.page_content
        }
        data.append(page_data)
    with open(output_file, "w") as f:
        json.dump(data, f, indent=4)

    print(f"Website data saved to {output_file}")

import json
import logging
from langchain.document_loaders import WebBaseLoader

logging.basicConfig(level=logging.INFO)

# Multiple Website URLs to scrape
def scrape_websites_multiple(url_paths,output_file):
    """
    Scrapes multiple websites and saves the details to a JSON file.
    Parameters:
    url_paths (list): A list of URLs to scrape.
    Returns:
    None
    """
    data = []
    max_iterations = 10
    for url_path in url_paths:
        loader = WebBaseLoader(url_path)
        iteration = 0
        while iteration < max_iterations:
            try:
                docs = loader.load()
                logging.info(f"Loaded {len(docs)} documents from {url_path}")
                if not docs:
                    break
                for doc in docs:
                    page_data = {
                        "url": url_path,
                        "page_content": doc.page_content
                    }
                    data.append(page_data)
                iteration += 1
            except Exception as e:
                logging.error(f"Error loading data from {url_path}: {e}")
                break

    with open(output_file, "w") as f:
        json.dump(data, f, indent=4)

    logging.info(f"Website data saved to {output_file}")