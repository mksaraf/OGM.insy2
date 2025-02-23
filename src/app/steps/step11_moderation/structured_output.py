# Function to structure the output
def structure_output(response):
    """
    Formats the LLM response into a structured output.

    Args:
    response (str): The LLM response to be formatted.

    Returns:
    str: The formatted response.
    """
    # Split the response into individual sentences
    sentences = response.split(". ")

    # Initialize an empty list to store the formatted response
    formatted_response = []

    # Loop through each sentence and format it
    for sentence in sentences:
        # Remove any leading or trailing whitespace
        sentence = sentence.strip()

        # If the sentence is empty, skip it
        if not sentence:
            continue

        # Add the sentence to the formatted response list
        formatted_response.append(sentence)

    # Join the formatted response list into a single string
    formatted_response = ". ".join(formatted_response)

    # Add a final period to the end of the response if it's not already there
    if not formatted_response.endswith("."):
        formatted_response += "."

    # Return the formatted response
    return formatted_response