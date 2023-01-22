# domaingen

Under construction! Not ready for use yet! Currently experimenting and planning!

Developed by Jeffery Mandrake from GoInfosystems.com (c) 2023

## Examples of How To Use (Alpha Version)

Create a domaingen object and input keywords

```python

from domaingen.domains import DomainGenerator

keywords = ["recipe","dinner","cooking","spices","food","apples"] # List of keywords
tlds = ['com'] # List of top level domain extensions (optional, default is com)

domaingen = DomainGenerator(keywords,tlds)
domains = domaingen.get_keyword_combinations()
for domain in domains:
    print(domain)


>>>
recipedinnercooking.com
recipedinnerspices.com
recipecookingspicesfood.com
dinnercookingfood.com
dinnercookingspices.com
spicesfood.com
cookingfood.com
recipespicesfood.com
dinnercookingspicesfood.com
recipedinnercookingspices.com
recipedinner.com
recipedinnercookingspicesfood.com
recipespices.com
recipedinnerfood.com
cookingspicesfood.com
recipecookingfood.com
dinnercooking.com
dinnerspices.com
dinnerfood.com
recipedinnercookingfood.com
recipecookingspices.com
recipefood.com
recipecooking.com
recipedinnerspicesfood.com
dinnerspicesfood.com
cookingspices.com

```

## Thesaurus (English)
This is a json dataset of synonyms for english words.
Source:
https://www.kaggle.com/datasets/behcetsenturk/englishengen-synonyms-json-thesaurus
