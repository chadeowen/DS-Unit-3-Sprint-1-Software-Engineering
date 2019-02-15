#!/usr/bin/env python
"""
Python methods for Acme Products random generation and summary reporting.
"""

import random

"""Creating result, a random product generator list."""
ADJECTIVES = ['Awesome ', 'Shiny ', 'Impressive ', 'Portable ', 'Improved ']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
result = []
for adjective in ADJECTIVES:
    for noun in NOUNS:
         result.append(adjective + noun)
sample = random.choices(result, k=30)

def generate_products(self = random.sample, name = random.choice(result), price = random.randint(5, 100), weight = random.randint(5, 100), 
flammability= random.uniform(0, 2.5)):
    """Randomly generates a given number of products (default 30), and returns a list."""
    return sample
### ToDo
### Fix Random Generator -- need to assign attributes to each variable in list sample

def inventory_report(self):
    """Prints a summary given a list of products."""
    mean_price = sum(Product.price for Product in sample) / len(sample)
    mean_weight = sum(Product.weight for Product in sample) / len(sample)
    mean_flam = sum(Product.flammability for Product in sample) / len(sample)
    return 'Unique Product Names: ', sample.unique, '/n Average Price: ', mean_price, 
    '/n Average Weight: ', mean_weight, '/n Average Flammability: ', mean_flam 


if __name__ == '__main__':
    inventory_report(generate_products())

