# Web Page Downloader and Link Updater

This Python script downloads a webpage, updates resource links (CSS, JS, and images) to absolute URLs, and saves the updated HTML to a file.

---

## How It Works

- **Download Webpage:** Fetches the HTML content of a given URL.
- **Update Links:** Converts relative resource URLs to absolute ones.
- **Save Updated Page:** Outputs the modified HTML to `output_page.html`.

---

## Requirements

- Python 3.7+
- Install dependencies:
```
pip install requests beautifulsoup4
``` 

---

## How to Use

1. Update the `page_url` variable in the script with the desired URL.  
	Example:
	```
	page_url = "http://example.com"
	```
    
- Run the script:
```
python quickPage.py
```

The updated HTML will be saved to `output_page.html` in the current directory.

---