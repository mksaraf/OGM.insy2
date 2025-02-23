# Create New Venv
python3.12 -m venv .venv_p312
source .venv_p312/bin/activate
deactivate
# Python version (python3 --version)
Python 3.12.8

# Reach App directory
cd src/app

# Install jupyter lab
pip install jupyter lab
 # Run streamlit
streamlit run mainVectorIndex.p
## Github
# Check Current Remotes:
(.venv_p312) manishkumarsaraf@MacBookPro OGM.insy % git remote -v
origin  https://OGMWorldWide@dev.azure.com/OGMWorldWide/OGM.MLOPS.Azure/_git/OGM.insy (fetch)
origin  https://OGMWorldWide@dev.azure.com/OGMWorldWide/OGM.MLOPS.Azure/_git/OGM.insy (push)
# Add GitHub as a Remote
git remote add github <your-github-repo-url>
git remote add github https://github.com/mksaraf/ogm.insy2.git
# Verify Remote Version
(.venv_p312) manishkumarsaraf@MacBookPro OGM.insy % git remote -v
github  https://github.com/mksaraf/ogm.insy2.git (fetch)
github  https://github.com/mksaraf/ogm.insy2.git (push)
origin  https://OGMWorldWide@dev.azure.com/OGMWorldWide/OGM.MLOPS.Azure/_git/OGM.insy (fetch)
origin  https://OGMWorldWide@dev.azure.com/OGMWorldWide/OGM.MLOPS.Azure/_git/OGM.insy (push)
# Push to Both Remotes:
git push origin main
git push github main

# Pull
git pull github main

# Remove github remote
git remote remove github
# Push to new repo in github
git init
git add .
git commit -m "Initial commit with specific folders"
git remote add github https://github.com/mksaraf/ogm.insy2.git


###### Lession Learned #####
# Semantic Search
Semantic search aims to understand search phrases' intent and contextual meaning, rather than focusing on individual keywords.
Traditional keyword search often depends on exact-match keywords or proximity-based algorithms that find similar words.

## Numerous strategies for understanding context
    - Other information: What other information is included in the search? For example, if the search phrase contains bank and river, the search is likely about waterways, not financial institutions.
    - User information: What is known about the user? Their search history and location can provide information about the context of the search. If they are in the UK, a search for "football" is likely about soccer, not American football.
    - Scenario: What scenario is being presented to the user? If the search is on a website about cars, a search for dash is likely about dashboards, not running quickly.

## Semantic Search
The results of a semantic search are typically scored based on
    - The relevance of the result to the search
    - The popularity of the result
    - The quality of the result

## Challenges with Semantic Search
    - Understanding Context - Accurately grasping the context of queries can be difficult. Different users might use the same words to mean different things.
    - Language Ambiguity - Natural language is inherently ambiguous. Words can have multiple meanings, and different models may interpret sentences differently.
    - Fine tuning - To get the best result, you may need to invest significant effort in fine-tuning your model, data and search algorithms.
    - Transparency - The complexity behind semantic search can make understanding how a score is determined or why a particular result is returned difficult.

# Vector
Vectors are simply a list of numbers. For example, the vector [1, 2, 3] is a list of three numbers and could represent a point in three-dimensional space. You can use vectors to represent many different types of data, including text, images, and audio.

## Dimensionality 
The number of dimensions in a vector is called the dimensionality of the vector. For example, a vector with three numbers has a dimensionality of 3. A vector containing 100 numbers has a dimensionality of 100.

## Embedding
Converting words/doc into numbers.
Embeddings can represent more than just words. They can also represent entire documents, images, audio, or other data types.

## Embedding Models
- OpenAI’s text-embedding-ada-002. 1,536 dimensions.
    - Word2Vec - A model for generating word embeddings, turning words into vectors based on their context.
    - FastText - An extension of Word2Vec, FastText treats each word as composed of character n-grams, allowing it to generate embeddings for out-of-vocabulary words.
    - Node2Vec - An algorithm that computes embeddings based on random walks through a graph.
    - GPT (Generative Pre-trained Transformer) - A series of models (e.g. GPT-4) that use transformers for generating text that you can also use for generating embeddings.
    - Universal Sentence Encoder - Designed to convert sentences into embeddings.
    - Doc2Vec - An extension of the Word2Vec model to generate embeddings for entire documents or paragraphs, capturing the overall meaning.
    - ResNet (Residual Networks) - Primarily used in image processing, ResNet models can also be used to generate embeddings for images that capture visual features and patterns.
    - VGGNet - VGGNet models are used in image processing to generate embeddings for images, capturing various levels of visual information.
- Each embedding model is different and captures different aspects of the data. As such, you cannot compare embeddings created by different models. You need to use the same model to generate the embeddings for the data you want to compare.