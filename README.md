# Create crawl_data and log folder
- crawl_data folder is for saving the datasets
- log folder is for logging crawling time
# Run the code
```python3 main.py```
# More information
- You can't use any Shopee API to get products by category, all of those are forbidden now. I get the products url by simply create a javascript code to get it from console. Foreach category i got about 180 - 200 products url. 
- Selenium and scrapy still can be used. But you need to make the code more like a human because Shopee has a bot detect system.
- The "get ratings" from a product url somehow still can be used without permisson.
