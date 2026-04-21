# Initialize the dictionaries
Catalog_Prices = {'TV': 50000, 'Mouse': 500}
Sale_Updates = {'TV': 45000}

# Merge Sale_Updates into Catalog_Prices (overwrites on key conflict)
Catalog_Prices.update(Sale_Updates)

# Output the updated catalog
print(Catalog_Prices)
