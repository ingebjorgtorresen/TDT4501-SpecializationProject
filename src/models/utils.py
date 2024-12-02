import os

def ensure_directory_exists(dir_path):
    """
    Ensure the given directory exists, creating it if necessary.
    """
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
