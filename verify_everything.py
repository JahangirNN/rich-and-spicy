import json
import os
import re

print("=== VERIFYING CATALOGS ===")
catalogs = {
    'Barbecue': ('barbecue_products.json', 23),
    'Biryani': ('biryani_products.json', 5),
    'Deep Fry': ('deep_fry_products.json', 8),
    'Gravy': ('gravy_products.json', 28),
    'Starters': ('starters_products.json', 8),
    'Sweet Delight': ('sweet_delight_products.json', 2),
    'Veg Starters': ('veg_starters_products.json', 7),
    'Veg Main Course': ('veg_main_course_products.json', 19),
    'Kitchen Special': ('kitchen_special_products.json', 17),
    'Whole Spices': ('whole_spices_products.json', 33),
    'Others': ('others_products.json', 49)
}

total_products_count = 0
all_products_map = {}

for cat_name, (fname, expected_count) in catalogs.items():
    assert os.path.exists(fname), f"File {fname} missing!"
    with open(fname, 'r', encoding='utf-8') as f:
        data = json.load(f)
    assert data['category'] == cat_name, f"Category mismatch: expected {cat_name}, got {data['category']}"
    prods = data['products']
    assert len(prods) == expected_count, f"Count mismatch in {fname}: expected {expected_count}, got {len(prods)}"
    total_products_count += len(prods)
    for p in prods:
        pid = p['id']
        assert pid not in all_products_map, f"Duplicate product ID {pid}"
        all_products_map[pid] = p
        # verify image exists
        img_path = p['images']['primary']
        assert os.path.exists(img_path), f"Image not found on disk: {img_path}"

assert total_products_count == 199, f"Total products expected 199, got {total_products_count}"
print(f"All 11 JSON catalogs valid. Total products: {total_products_count}")

# Check specific fixed items
print("\n=== VERIFYING SPECIFIC HIGH-VALUE TARGETS ===")
dabba = all_products_map['gravy-dabba-gosht-50g']
assert dabba['regional_names']['gu'] == "ડબ્બા ગૌસ્ત", f"Dabba Gu fail: {dabba['regional_names']['gu']}"
assert "Shield-Cutout" in dabba['packaging_type'], f"Dabba packaging fail: {dabba['packaging_type']}"
assert "Dabba Ghosht" in dabba['name'], f"Dabba name fail: {dabba['name']}"

dal = all_products_map['gravy-dal-gosht-40g']
assert dal['regional_names']['gu'] == "દાલ ગૌસ્ત", f"Dal Gu fail: {dal['regional_names']['gu']}"

manda = all_products_map['gravy-manda-gosht-50g']
assert manda['regional_names']['gu'] == "માંડા ગૌસ્ત", f"Manda Gu fail: {manda['regional_names']['gu']}"
assert "Mannda Ghosht" in manda['name'], f"Manda name fail: {manda['name']}"

fish = all_products_map['gravy-fish-prawns-gravy-50g']
assert fish['regional_names']['gu'] == "મચ્છી જીંગા મસાલા", f"Fish Gu fail: {fish['regional_names']['gu']}"
assert fish['product_type'] == "Instant Mix", f"Fish product_type fail: {fish['product_type']}"

paya = all_products_map['gravy-paya-50g']
assert paya['pricing']['mrp'] == 15, f"Paya mrp fail: {paya['pricing']['mrp']}"
assert paya['net_weight']['value'] == 50, f"Paya net weight fail: {paya['net_weight']}"

crispy = all_products_map['deepfry-crispy-chicken-50g']
assert crispy['product_type'] == "Instant Mix", f"Crispy product_type fail: {crispy['product_type']}"

chilli = all_products_map['deepfry-chicken-chilli-paneer-chilli-50g']
assert "Shield-Cutout" in chilli['packaging_type'], f"Chilli packaging fail: {chilli['packaging_type']}"

samosa = all_products_map['deepfry-mutton-kheema-samosa-40g']
assert "Kheema Samosa Masala" in samosa['name'], f"Samosa name fail: {samosa['name']}"
assert samosa['product_type'] == "Dry Marinade / Spice Mix", f"Samosa product_type fail: {samosa['product_type']}"

# New items verification
bhuna = all_products_map['starters-bhuna-gosht-50g']
assert bhuna['regional_names']['gu'] == "ભુના ગૌસ્ત"
assert bhuna['category'] == "Starters"

coco = all_products_map['sweet-cold-coco-instant-mix-100g']
assert coco['regional_names']['gu'] == "કોલ્ડ કોકો"
assert coco['category'] == "Sweet Delight"

pani_puri = all_products_map['vegstarter-pani-puri-masala-50g']
assert pani_puri['regional_names']['gu'] == "પાણી પુરી"
assert pani_puri['category'] == "Veg Starters"

pav_bhaji = all_products_map['veg-bhaji-pav-50g']
assert pav_bhaji['regional_names']['gu'] == "ભાજીપાઉં"
assert pav_bhaji['category'] == "Veg Main Course"

tea_masala = all_products_map['ks-sp-tea-masala-50g']
assert tea_masala['regional_names']['gu'] == "સ્પે. ચાહ મસાલો"
assert tea_masala['category'] == "Kitchen Special"

cardamom = all_products_map['ws-green-cardamom-elaichi-50g']
assert cardamom['regional_names']['gu'] == "લીલી ઈલાયચી"
assert cardamom['category'] == "Whole Spices"

birista = all_products_map['others-fried-onions-birista-100g']
assert birista['regional_names']['gu'] == "તળેલી ડુંગળી / બિરિસ્તા"
assert birista['category'] == "Others"

print("All specific targets verified!")

# Verify catalog-data.js
print("\n=== VERIFYING CATALOG-DATA.JS ===")
assert os.path.exists('catalog-data.js')
with open('catalog-data.js', 'r', encoding='utf-8') as f:
    js_text = f.read()

assert js_text.startswith('window.CATALOG_DATA = '), "catalog-data.js missing window.CATALOG_DATA prefix"
json_part = js_text[len('window.CATALOG_DATA = '):].rstrip(';\n\r ')
bundle_data = json.loads(json_part)
assert bundle_data['total_products'] == 199, f"Bundle total_products fail: {bundle_data['total_products']}"
assert len(bundle_data['products']) == 199, f"Bundle products array length fail: {len(bundle_data['products'])}"
for cat_name, (_, exp_count) in catalogs.items():
    assert bundle_data['categories'][cat_name] == exp_count, f"Count for {cat_name} mismatch: {bundle_data['categories'][cat_name]} != {exp_count}"
print("catalog-data.js verified!")

# Verify index.html
print("\n=== VERIFYING INDEX.HTML ===")
assert os.path.exists('index.html')
with open('index.html', 'r', encoding='utf-8') as f:
    html_text = f.read()

assert 'id="categoryTabs"' in html_text, "Missing id=categoryTabs in index.html"
assert 'data-category="all"' in html_text, "Missing data-category=all in index.html"
for cat_name in catalogs.keys():
    assert f'data-category="{cat_name}"' in html_text, f"Missing data-category={cat_name} in index.html"

assert 'id="all-count"' in html_text
assert 'id="bbq-count"' in html_text
assert 'id="biryani-count"' in html_text
assert 'id="gravy-count"' in html_text
assert 'id="deepfry-count"' in html_text
assert 'id="starters-count"' in html_text
assert 'id="sweetdelight-count"' in html_text
assert 'id="vegstarters-count"' in html_text
assert 'id="vegmain-count"' in html_text
assert 'id="ks-count"' in html_text
assert 'id="wholespices-count"' in html_text
assert 'id="others-count"' in html_text
assert 'currentCategory' in html_text, "Missing currentCategory in index.html"

print("index.html verified!")
print("\n*** ALL SYSTEM VERIFICATIONS PASSED 100% ***")
