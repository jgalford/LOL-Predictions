# Download data from Oracle's Elixir

# Usefull links:
# https://oracleselixir.com/tools/downloads
# https://oracleselixir.com/definitions

import gdown

url = 'https://drive.google.com/drive/folders/1gLSw0RLjBbtaNy0dgnGQDAZOHIgCe-HH'
gdown.download_folder(url, quiet=False, use_cookies=False)