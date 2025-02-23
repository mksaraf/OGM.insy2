import os
import json

# data_path_input = "data/input/Data_Insurance/NorthAmerica"
# check_datasouce_output_file = "data/output/data_source_check.json"

def check_data_source(data_path_input,check_datasouce_output_file):
    """
    Check if a directory exists and return a list of files and directories in the directory.

    Args:
        data_path_input (str): Path to the directory to check.

    Returns:
        dict: A dictionary with a "warning message" key containing a message indicating whether the directory exists,
              and a "files" key containing a list of files and directories in the directory.
    """
    dir_path = data_path_input
    dir_exists = os.path.exists(dir_path) and os.path.isdir(dir_path)

    # Get a list of files and directories in the directory
    files = []
    if dir_exists:
        for root, dirs, filenames in os.walk(data_path_input):
            for filename in filenames:
                files.append(os.path.join(root, filename))
            for dir in dirs:
                files.append(os.path.join(root, dir))

    response = {
        "warning message": f"Directory {'Exists' if dir_exists else 'Does not Exist'}",
        "files": files
    }

    # Save response to a JSON file
    try:
        with open(check_datasouce_output_file, "w") as f:
            json.dump(response, f, indent=4)
        response["save_status"] = "Success: Response saved to JSON file"
    except Exception as e:
        response["save_status"] = f"Error: Failed to save response to JSON file - {str(e)}"

    # Return the response dictionary
    return response

