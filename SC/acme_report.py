from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    for x in range(num_products):
        list1 = sample(ADJECTIVES, k=1)
        list2 = sample(NOUNS, k=1)
        for i in list1:
            for j in list2:
                products.append("{} {}".format(i, j))

    return products

def inventory_report(products):
    prices = []
    weights = []
    flammabilities = []
    for item in products:
        price = randint(5,100)
        prices.append(price)
        weight = randint(5,100)
        weights.append(weight)
        flammability = uniform(0.0, 2.5)
        flammabilities.append(flammability)
        
    s = f'ACME CORPORATION OFFICIAL INVENTORY REPORT, Unique product names: {len(products)}, Average price: {sum(prices)/len(prices)}, Average weight: {sum(weights)/len(weights)}, Average flammability: {sum(flammabilities)/len(flammabilities)}'
        
    return s


if __name__ == '__main__':
    inventory_report(generate_products())