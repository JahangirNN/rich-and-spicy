# test_all_catalogs.py
import json
import os
import sys

catalogs = [
    ("biryani_products.json", "Biryani", 5),
    ("deep_fry_products.json", "Deep Fry", 8),
    ("gravy_products.json", "Gravy", 28)
]

all_passed = True

for filename, expected_cat, expected_count in catalogs:
    print(f"\n==========================================")
    print(f"Validating {filename}...")
    if not os.path.exists(filename):
        print(f"FAIL: File {filename} does not exist.")
        all_passed = False
        continue

    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Top-level checks
    assert data.get("category") == expected_cat, f"Category mismatch: {data.get('category')} != {expected_cat}"
    assert data.get("total_products") == expected_count, f"Count mismatch: {data.get('total_products')} != {expected_count}"
    assert len(data.get("products", [])) == expected_count, f"Products array mismatch: {len(data.get('products'))} != {expected_count}"
    assert data.get("brand") == "Rich 'n' SP!CY"
    assert "name" in data.get("manufacturer", {})
    assert "address" in data.get("manufacturer", {})
    assert "contact" in data.get("manufacturer", {})

    product_ids = set()

    for idx, p in enumerate(data["products"], 1):
        pid = p.get("id")
        assert pid, f"Product {idx} missing id"
        assert pid not in product_ids, f"Duplicate id {pid}"
        product_ids.add(pid)

        assert p.get("name"), f"Product {pid} missing name"
        assert p.get("brand") == "Rich 'n' SP!CY", f"Product {pid} brand mismatch"
        assert p.get("category") == expected_cat, f"Product {pid} category mismatch"
        assert p.get("product_type") in ["Instant Mix", "Dry Marinade / Spice Mix"], f"Product {pid} invalid product_type"
        assert isinstance(p.get("tags"), list) and len(p.get("tags")) > 0, f"Product {pid} invalid tags"

        # Regional
        assert p.get("regional_names", {}).get("gu"), f"Product {pid} missing Gujarati name"

        # Net weight
        nw = p.get("net_weight", {})
        assert isinstance(nw.get("value"), (int, float)) and nw.get("value") > 0, f"Product {pid} invalid net_weight value"
        assert nw.get("unit") == "g", f"Product {pid} net_weight unit must be 'g'"

        # Packaging
        assert p.get("packaging_type"), f"Product {pid} missing packaging_type"

        # Dietary
        dietary = p.get("dietary", {})
        assert dietary.get("is_vegetarian_mix") is True, f"Product {pid} is_vegetarian_mix must be true"
        assert isinstance(dietary.get("suggested_protein"), list) and len(dietary.get("suggested_protein")) > 0

        # Images
        img = p.get("images", {})
        primary_path = img.get("primary", "")
        filename_val = img.get("filename", "")
        assert os.path.exists(primary_path), f"Product {pid} image file missing at {primary_path}"
        assert os.path.basename(primary_path) == filename_val, f"Product {pid} filename mismatch"

        # Recipe
        recipe = p.get("recipe", {})
        assert recipe.get("serves_portion"), f"Product {pid} missing serves_portion"
        assert recipe.get("marination_time"), f"Product {pid} missing marination_time"
        assert isinstance(recipe.get("cooking_methods"), list) and len(recipe.get("cooking_methods")) > 0
        assert isinstance(recipe.get("required_ingredients"), list) and len(recipe.get("required_ingredients")) > 0

        instr = recipe.get("instructions", {})
        assert instr.get("en"), f"Product {pid} missing English instructions"
        assert instr.get("gu"), f"Product {pid} missing Gujarati instructions"

        # Manufacturer
        mfg = p.get("manufacturer", {})
        assert mfg.get("name") == "City Gruh Udhyog"

    print(f"SUCCESS: {filename} passed all schema and consistency checks! ({len(data['products'])} items)")

print("\n==========================================")
print("ALL CATALOGS VALIDATED SUCCESSFULLY!")
