import requests
import re

def get_huggingface_downloads():
    url = "https://huggingface.co/api/models/Seif-Yasser/bart-large-xsum-finetuned-xsum"
    response = requests.get(url)
    data = response.json()
    return data.get("downloads", "0")

def update_readme(downloads):
    with open("README.md", "r") as file:
        readme = file.read()

    # Find and replace download count in README
    updated_readme = re.sub(r"!\[Downloads\]\(.*?\)", 
                            f"![Downloads](https://img.shields.io/badge/downloads-{downloads}-brightgreen)", 
                            readme)

    with open("README.md", "w") as file:
        file.write(updated_readme)

if __name__ == "__main__":
    downloads = get_huggingface_downloads()
    update_readme(downloads)
