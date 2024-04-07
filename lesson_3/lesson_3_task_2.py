from smartphone import Smartphone
catalog = []
catalog.append(Smartphone("Apple", "iPhone X", "+79000000000"))
catalog.append(Smartphone("Samsung", "Galaxy S21", "+79213333535"))
catalog.append(Smartphone("Apple", "iPhone 13", "+79616766666"))
catalog.append(Smartphone("Apple", "iPhone 7", "+79152222222"))
catalog.append(Smartphone("Huawei", "Honor X9b", "+79999999999"))

for phone in catalog:
    print(f"{phone.phone_maker} - {phone.model}. {phone.phone_number}")