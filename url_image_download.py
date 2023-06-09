import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

def download_images(url):
    # Create a directory to store the downloaded images
    directory = 'downloaded_images'
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Send a GET request to the specified URL
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <img> tags in the HTML
    img_tags = soup.find_all('img')

    # Download each image
    for img in img_tags:
        img_url = img['src']
        if img_url.startswith('http'):
            # If the image URL is an absolute URL
            image_url = img_url
        else:
            # If the image URL is a relative URL, convert it to an absolute URL
            base_url = '{uri.scheme}://{uri.netloc}'.format(uri=urlparse(url))
            image_url = urljoin(base_url, img_url)

        try:
            # Send a GET request to the image URL
            response = requests.get(image_url)
            # Extract the image file name
            filename = os.path.join(directory, os.path.basename(image_url))
            # Save the image file
            with open(filename, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded: {filename}")
        except Exception as e:
            print(f"Failed to download: {image_url}")
            print(str(e))

# Example usage
url = input("Enter the URL: ")
download_images(url)
