Task 1

Technologies: Python latest, Scrapy

In this task, you need to write a scrapy spider  for a website URL:  https://www.midsouthshooterssupply.com/dept/reloading/primers

Points to keep in mind
Make sure you scrape all pages and all items
It is possible you could not find values for a few data points, in that case, you shouldn't add the key to the final JSON.
If you are scraping a paragraph, make sure new lines must be replaced by '__ '. Multiple paras should be concatenated using '__'.

First, scrape the required fields that are listed below:
Price in dollars
Description
Review
Delivery Info
Title
Stock status i.e. in-stock or out-stock. If in-stock then the value would true and for out-stock value should be false.
Manufacturer i.e. Remington, Winchester, etc.
For this scraper, use rotating proxies from this website http://www.freeproxylists.net/ (only US )
The output should be in the list of dictionaries, finally represented in JSON.

[
    ...
    {
        'price': '', # type(float)
        'title': '', # type(string)
        'stock': '', # type(boolean)
        'manufacturer': '',  # type(string)
        'review' : '', # type(string)
        'description' : '', # type(string)
        'delivery_info' : '' # type(string)
    }
    ...
]
