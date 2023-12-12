

from LiDoS import LicenseManager




# https://docs.google.com/spreadsheets/d/1oszKytFOQs4jpq_8rYD-1rha_4ah6AQxVGYxGjA_RzE/edit#gid=0

url_id = "1oszKytFOQs4jpq_8rYD-1rha_4ah6AQxVGYxGjA_RzE"

lic = LicenseManager(
    url_id=url_id,
    sheet_id=0
)

lic_key = lic.get_license("1234567890")
print(lic_key)
print(lic_key.is_active())
print(lic_key.is_valid())
print(lic_key.is_expired())


