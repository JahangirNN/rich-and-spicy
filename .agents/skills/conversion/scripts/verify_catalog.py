import json
import os
import random
import sys

def verify_catalog(json_path, sample_count=5):
    if not os.path.exists(json_path):
        print(f"Error: Catalog file not found at '{json_path}'")
        sys.exit(1)

    with open(json_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except Exception as e:
            print(f"Error parsing JSON: {e}")
            sys.exit(1)

    category = data.get("category", "Unknown")
    products = data.get("products", [])
    print(f"=== Catalog Validation: {category} ===")
    print(f"Total products recorded: {len(products)}")

    missing_images = []
    for p in products:
        img_rel = p.get("images", {}).get("primary", "")
        if not os.path.exists(img_rel):
            missing_images.append((p.get("id"), img_rel))

    if missing_images:
        print(f"WARNING: {len(missing_images)} products have missing image files:")
        for pid, img in missing_images:
            print(f"  - {pid}: {img}")
    else:
        print("All product image references verified on disk.")

    # Random sampling
    sample_size = min(sample_count, len(products))
    print(f"\n=== Random Sample Verification ({sample_size} products) ===")
    sample = random.sample(products, sample_size)
    for idx, p in enumerate(sample, 1):
        print(f"\n[{idx}] {p.get('name')}")
        print(f"     ID: {p.get('id')}")
        print(f"     Regional (Gujarati): {p.get('regional_names', {}).get('gu')}")
        print(f"     Net Weight: {p.get('net_weight', {}).get('value')}{p.get('net_weight', {}).get('unit')}")
        print(f"     Image: {p.get('images', {}).get('filename')}")
        print(f"     Ingredients: {len(p.get('recipe', {}).get('required_ingredients', []))} items")
        print(f"     EN Instruction: {p.get('recipe', {}).get('instructions', {}).get('en')[:80]}...")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "barbecue_products.json"
    verify_catalog(target)
