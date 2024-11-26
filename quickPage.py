import requests
from bs4 import BeautifulSoup
import os

# Function to download the page
def download_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to retrieve the page")
        return None

# Function to process the HTML and update resource links
def process_html(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')
    
    # Update links for CSS, JS, and images to ensure they are absolute URLs
    for link in soup.find_all(['link', 'script', 'img']):
        if link.name == 'link' and link.get('href'):
            # Make href absolute URL for CSS or other linked files
            link['href'] = make_absolute_url(link['href'], base_url)
        elif link.name == 'script' and link.get('src'):
            # Make src absolute URL for JS files
            link['src'] = make_absolute_url(link['src'], base_url)
        elif link.name == 'img' and link.get('src'):
            # Make src absolute URL for images
            link['src'] = make_absolute_url(link['src'], base_url)
    
    # Return the modified HTML content
    return str(soup)

# Function to make relative URLs absolute
def make_absolute_url(relative_url, base_url):
    if relative_url.startswith(('http://', 'https://')):
        return relative_url
    elif relative_url.startswith('/'):
        return base_url + relative_url
    else:
        return os.path.join(base_url, relative_url)

# Main function
def main(url):
    print(f"Fetching the page: {url}")
    html = download_page(url)
    
    if html:
        base_url = url.rstrip('/')  # Ensure we have the base URL without trailing slashes
        updated_html = process_html(html, base_url)
        
        # Optionally, save to an HTML file
        with open("output_page.html", "w", encoding="utf-8") as f:
            f.write(updated_html)
        
        print("Page downloaded and links updated successfully!")

# Run the script with the URL you want to download
if __name__ == "__main__":
    page_url = "http://example.com"  # Replace with the URL you want to download
    main(page_url)
