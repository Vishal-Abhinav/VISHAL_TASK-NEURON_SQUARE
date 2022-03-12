# VISHAL_TASK-NEURON_SQUARE
Scripting and automation task - Neuron Square LLC
from contextlib import nullcontext
from gettext import NullTranslations


{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "4853a9d3",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (Temp/ipykernel_6832/1503958083.py, line 30)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"C:\\Users\\lenovo\\AppData\\Local\\Temp/ipykernel_6832/1503958083.py\"\u001b[1;36m, line \u001b[1;32m30\u001b[0m\n\u001b[1;33m    for product in response.css(\"div.product\"):\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "# importing the scrapy module\n",
    "import scrapy\n",
    "\n",
    "class ExtractUrls(scrapy.Spider):\n",
    "\tname = \"extract\"\n",
    "\n",
    "\t# request function\n",
    "\tdef start_requests(self):\n",
    "\t\turls = [ 'https://www.midsouthshooterssupply.com/dept/reloading/primers', ]\n",
    "\t\t\n",
    "\t\tfor url in urls:\n",
    "\t\t\tyield scrapy.Request(url = url, callback = self.parse)\n",
    "\n",
    "\t# Parse function\n",
    "\tdef parse(self, response):\n",
    "\t\t\n",
    "\t\t# Extra feature to get title\n",
    "\t\tproduct = response.css('product::text').extract_first()\n",
    "\t\t\n",
    "\t\t# Get anchor tags\n",
    "\t\tlinks = response.css('product::attr(href)').extract()\n",
    "        \n",
    "\t\t\n",
    "\t\tfor link in links:\n",
    "\t\t\tyield\n",
    "\t\t\t{\n",
    "\t\t\t\t'product': product,\n",
    "\t\t\t\t'links': link\n",
    "                \n",
    "                \n",
    "                for product in response.css(\"div.product\"):\n",
    "                 price = product.css(\"div.catalog-item-price::price\").get()\n",
    "                 title = product.css(\"div.catalog-item-brand::title\").get()\n",
    "                 status = product.css(\"div.out-of-stock::status\").getall()\n",
    "                 brand = product.css(\"div.manufacturer::brand\").getall()\n",
    "                 result = product.css(\"div.review-product::result\").getall()\n",
    "                 description = product.css(\"div.catlog.item-name::description\").getall()\n",
    "                 delievery = product.div(delivery_info.script).getall()\n",
    "                \n",
    "               print(dict(price=price, title=title, status=status, brand=brand, result=result, description=description, delivery=delivery))\n",
    "\t\t\t}\n",
    "\t\t\t\n",
    "\t\t\tif 'midsouthshooterssupply' in link:\t\t\n",
    "\t\t\t\tyield scrapy.Request(url = link, callback = self.parse)\n",
    "                \n",
    "                \n",
    "                "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": nullcontext,
   "id": "307bf6aa",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": NullTranslations,
   "id": "97e17d1f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
