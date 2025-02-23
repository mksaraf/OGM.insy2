"""
This module defines the chunking of loaded data
"""

import os
from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_text(data: str, chunk_size: int = 1000, chunk_overlap: int = 0) -> list:
    """
    Split a large text into smaller chunks.

    Args:
        data (str): The text to be chunked.
        chunk_size (int, optional): The size of each chunk. Defaults to 1000.
        chunk_overlap (int, optional): The overlap between chunks. Defaults to 0.

    Returns:
        list: A list of chunked text.

    Raises:
        ValueError: If chunk_size or chunk_overlap is invalid.
        TypeError: If data is not a string.
    """

    try:
        # Check if data is a string
        if not isinstance(data, str):
            raise TypeError("Data must be a string.")

        # Check if chunk_size and chunk_overlap are valid
        if chunk_size <= 0 or chunk_overlap < 0:
            raise ValueError("Chunk size must be positive and chunk overlap must be non-negative.")

        # Create a text splitter with the specified chunk size and overlap
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

        # Split the text into chunks
        chunks = text_splitter.split_documents([data])

        return chunks

    except ValueError as ve:
        print(f"Invalid input: {ve}")
        return []
    except TypeError as te:
        print(f"Invalid data type: {te}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def chunking(data,chunk_size,chunk_overlap):
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    chunks=text_splitter.split_documents(data)
    return chunks  

# Text Splitter for Knowledge Graph
from langchain.text_splitter import CharacterTextSplitter

def chunking_kg(data_kg):
    text_splitter_kg = CharacterTextSplitter(
    separator="\n\n",
    chunk_size=1500,
    chunk_overlap=200,)   
    try:
        chunks_kg = text_splitter_kg.split_documents(data_kg)
        return chunks_kg
    except Exception as e:
        print(f"An error occurred while splitting documents: {e}")
        return None