# random_sample_validation.py
import json
import random

random.seed(42) # Deterministic seed for reproducible reporting

catalogs = [
    ("biryani_products.json", 3),
    ("deep_fry_products.json", 3),
    ("gravy_products.json", 3)
]

for filename, k in catalogs:
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"\n=======================================================")
    print(f"=== RANDOM SAMPLE AUDIT: {data['category']} ({k} samples) ===")
    print(f"=======================================================")
    sample = random.sample(data["products"], k)
    for i, p in enumerate(sample, 1):
        print(f"\n[Sample {i}] ID: {p['id']}")
        print(f"  Name (EN): {p['name']}")
        print(f"  Name (GU): {p['regional_names']['gu']}")
        print(f"  Packaging: {p['packaging_type']}")
        print(f"  Net Weight: {p['net_weight']['value']}{p['net_weight']['unit']}")
        print(f"  Dietary: Vegetarian Mix={p['dietary']['is_vegetarian_mix']}, Proteins={p['dietary']['suggested_protein']}")
        print(f"  Image Path: {p['images']['primary']}")
        print(f"  Serves Portion: {p['recipe']['serves_portion']}")
        print(f"  Cooking Methods: {p['recipe']['cooking_methods']}")
        print(f"  Ingredients Count: {len(p['recipe']['required_ingredients'])}")
        print(f"  EN Instructions Preview: {p['recipe']['instructions']['en'][:100]}...")
        print(f"  GU Instructions Preview: {p['recipe']['instructions']['gu'][:100]}...")
