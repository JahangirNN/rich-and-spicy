import json

files = [
    'barbecue_products.json',
    'biryani_products.json',
    'deep_fry_products.json',
    'gravy_products.json'
]

all_products = []
category_counts = {}

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
        cat = data['category']
        prods = data['products']
        category_counts[cat] = len(prods)
        all_products.extend(prods)

bundle = {
    'brand': "Rich 'n' SP!CY",
    'category': 'All',
    'total_products': len(all_products),
    'generated_at': '2026-11-20',
    'categories': category_counts,
    'manufacturer': {
        'name': 'City Gruh Udhyog',
        'address': '10/2573 City Masala Bhagatalao, opposite Hafiz Brothers, Surat-395003',
        'contact': '9898155726'
    },
    'products': all_products
}

with open('catalog-data.js', 'w', encoding='utf-8') as f:
    f.write('window.CATALOG_DATA = ' + json.dumps(bundle, indent=2, ensure_ascii=False) + ';\n')

print(f'Successfully wrote catalog-data.js with {len(all_products)} products across {len(category_counts)} categories: {category_counts}')
