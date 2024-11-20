def check_compatibility(components):
    """
    Перевірка сумісності компонентів ПК.
    """
    issues = []

    # Перевірка наявності компонентів
    required_components = ["CPU", "Motherboard", "GPU", "RAM", "SSD", "Power Supply"]
    for comp in required_components:
        if not components.get(comp):
            issues.append(f"{comp} не вибрано.")

    if not issues:
        try:
            # Сокети CPU і Motherboard
            cpu_socket = {
                "Intel i5-12400": "LGA1200",
                "AMD Ryzen 5 5600X": "AM4",
                "Intel i7-12700K": "LGA1700",
                "AMD Ryzen 7 5800X": "AM4",
                "Intel i3-12100F": "LGA1700",
                "AMD Ryzen 3 3300X": "AM4",
                "Intel i9-12900K": "LGA1700",
                "AMD Ryzen 9 5900X": "AM4",
                "Intel i5-12600KF": "LGA1700",
                "AMD Ryzen 5 5500": "AM4",
                "Intel Pentium Gold G7400": "LGA1700",
                "AMD Athlon 3000G": "AM4",
                "Intel i7-11700": "LGA1200",
                "AMD Ryzen Threadripper 3960X": "sTRX4",
                "Intel Celeron G6900": "LGA1700",
                "AMD Ryzen 5 3600": "AM4",
                "Intel i9-10900K": "LGA1200",
                "AMD Ryzen 7 3700X": "AM4",
                "Intel i5-11400": "LGA1200",
                "AMD Ryzen 9 5950X": "AM4",
                "Intel Xeon W-1290P": "LGA1200",
                "AMD Ryzen Threadripper PRO 3995WX": "sWRX8",
                "Intel i7-12700": "LGA1700",
                "AMD Ryzen 5 PRO 4650G": "AM4",
                "Intel i3-10300": "LGA1200",
                "AMD Ryzen 3 3100": "AM4",
                "Intel Pentium Gold G6600": "LGA1200",
                "AMD Ryzen 7 2700": "AM4",
                "Intel i9-11900K": "LGA1200",
                "AMD Ryzen 9 3950X": "AM4",
                "AMD Ryzen 7 7800X": "AM5",
                "AMD FX-9590": "AM3+",
                "AMD Phenom II X6 1090T": "AM3",
                "AMD A8-3850": "FM1",
                "AMD A10-5800K": "FM2",
                "Intel Core i7-4770K": "LGA1150",
                "Intel Core i5-4460": "LGA1150",
                "Intel Core i7-7700K": "LGA1151",
                "Intel Core i5-7600": "LGA1151",
                "Intel Core i7-9700K": "LGA1151v2",
                "Intel Core i5-9600K": "LGA1151v2",
                "Intel Core i9-10900X": "LGA2066",
                "Intel Core i7-7820X": "LGA2066",
                "AMD Ryzen 9 7950X": "AM5",
                "AMD Ryzen 5 7600X": "AM5",
                "AMD FX-6300": "AM3+",
                "Intel Core i3-8350K": "LGA1151",
                "Intel Core i5-3570K": "LGA1150",
                "AMD A10-7850K": "FM2",
                "Intel Core i7-3770": "LGA1150",
                "AMD FX-4100": "AM3+",
                "Intel Core i5-2500K": "LGA1151",
                "AMD A6-5400K": "FM2",
                "Intel Core i7-6800K": "LGA2066",
                "AMD Ryzen 7 7700X": "AM5",
                "Intel Core i9-7920X": "LGA2066",
                "AMD Ryzen 5 7500": "AM5",
                "Intel Core i7-4960X": "LGA1151",
                "AMD FX-6100": "AM3+",
                "Intel Core i5-4570": "LGA1150"
                }.get(components["CPU"], None)

            motherboard_socket = {
                "MSI B450 TOMAHAWK MAX AM4 DDR4": "AM4",
                "ASUS ROG STRIX Z690-A LGA1700 DDR5": "LGA1700",
                "Gigabyte B550 AORUS ELITE V2 AM4 DDR4": "AM4",
                "ASUS TUF GAMING X570-PLUS AM4 DDR4": "AM4",
                "MSI Z490-A PRO LGA1200 DDR4": "LGA1200",
                "ASRock B660 Steel Legend LGA1700 DDR5": "LGA1700",
                "Gigabyte X570 AORUS ELITE AM4 DDR4": "AM4",
                "MSI MPG Z590 GAMING EDGE LGA1200 DDR4": "LGA1200",
                "ASUS PRIME B660-PLUS LGA1700 DDR5": "LGA1700",
                "Gigabyte Z690 UD AX LGA1700 DDR5": "LGA1700",
                "ASRock B450M PRO4 AM4 DDR4": "AM4",
                "MSI MAG B550M MORTAR AM4 DDR4": "AM4",
                "ASUS ROG CROSSHAIR VIII FORMULA AM4 DDR4": "AM4",
                "Gigabyte B660M DS3H DDR4 LGA1700 DDR4": "LGA1700",
                "ASRock X570 Taichi AM4 DDR4": "AM4",
                "MSI Z690 CARBON WIFI LGA1700 DDR5": "LGA1700",
                "ASUS TUF GAMING B550M-PLUS AM4 DDR4": "AM4",
                "Gigabyte Z590 AORUS MASTER LGA1200 DDR4": "LGA1200",
                "ASRock B560M Steel Legend LGA1200 DDR4": "LGA1200",
                "MSI MPG B650 CARBON WIFI AM5 DDR5": "AM5",
                "ASUS ROG STRIX B450-F GAMING AM4 DDR4": "AM4",
                "Gigabyte B650 AORUS PRO AM5 DDR5": "AM5",
                "MSI PRO Z690-A DDR4 LGA1700 DDR4": "LGA1700",
                "ASUS PRIME H610M-E D4 LGA1700 DDR4": "LGA1700",
                "Gigabyte X670 AORUS XTREME AM5 DDR5": "AM5",
                "ASRock B760 PRO RS D4 LGA1700 DDR4": "LGA1700",
                "MSI MEG Z790 GODLIKE LGA1700 DDR5": "LGA1700",
                "ASUS TUF GAMING B760M-PLUS WIFI D4 LGA1700 DDR4": "LGA1700",
                "Gigabyte B760 AORUS ELITE AX LGA1700 DDR4": "LGA1700",
                "ASRock H670 Steel Legend LGA1700 DDR4": "LGA1700",
                "ASUS PRIME A320M-K AM3+ DDR3": "AM3+",
                "Gigabyte GA-970A-DS3P AM3+ DDR3": "AM3+",
                "MSI 970 GAMING AM3+ DDR3": "AM3+",
                "ASRock FM2A88M-HD+ FM2 DDR3": "FM2",
                "ASUS TUF GAMING B550-PLUS AM4 DDR4": "AM4",
                "Gigabyte GA-F2A68HM-S1 FM2+ DDR3": "FM2+",
                "MSI A68HM-E33 FM2+ DDR3": "FM2+",
                "ASUS ROG STRIX Z390-E GAMING LGA1151 DDR4": "LGA1151",
                "Gigabyte Z370 AORUS ULTRA GAMING LGA1151 DDR4": "LGA1151",
                "MSI Z370 GAMING PRO CARBON LGA1151 DDR4": "LGA1151",
                "ASRock Z270 Extreme4 LGA1151 DDR4": "LGA1151",
                "ASUS TUF X299 MARK 1 LGA2066 DDR4": "LGA2066",
                "Gigabyte X299 UD4 PRO LGA2066 DDR4": "LGA2066",
                "MSI X299 SLI PLUS LGA2066 DDR4": "LGA2066",
                "ASRock X299 Taichi LGA2066 DDR4": "LGA2066",
                "ASUS ROG Maximus XI Hero LGA1151 DDR4": "LGA1151",
                "Gigabyte H310M S2H LGA1151 DDR4": "LGA1151",
                "MSI B450 GAMING PLUS MAX AM4 DDR4": "AM4",
                "ASRock FM2A55M-DGS FM2 DDR3": "FM2",
                "Gigabyte GA-970-Gaming AM3+ DDR3": "AM3+"
            }.get(components["Motherboard"], None)

            if cpu_socket and motherboard_socket:
                if cpu_socket != motherboard_socket:
                    issues.append(
                        f"Роз'єм проце́сора ({cpu_socket}) не відповідає роз'єму материнської плати ({motherboard_socket})."
                    )

            # Тип пам'яті RAM
            ram_type = {
                "Kingston Fury Beast DDR4 16GB 3200MHz": "DDR4",
                "Corsair Vengeance LPX DDR4 8GBx2 3000MHz": "DDR4",
                "G.Skill Trident Z RGB DDR4 32GB 3600MHz": "DDR4",
                "Crucial Ballistix DDR4 16GB 2666MHz": "DDR4",
                "Team T-Force Vulcan DDR4 8GBx2 3000MHz": "DDR4",
                "Kingston HyperX Predator DDR4 16GB 4000MHz": "DDR4",
                "Corsair Dominator Platinum DDR4 64GB 3200MHz": "DDR4",
                "G.Skill Ripjaws V DDR4 16GB 3600MHz": "DDR4",
                "Patriot Viper Steel DDR4 8GBx2 3000MHz": "DDR4",
                "ADATA XPG Spectrix D60G DDR4 16GB 3200MHz": "DDR4",
                "Kingston Fury Renegade DDR4 32GB 3600MHz": "DDR4",
                "Corsair Vengeance RGB Pro DDR4 16GBx2 3200MHz": "DDR4",
                "G.Skill Trident Z Neo DDR4 16GB 3600MHz": "DDR4",
                "Crucial DDR4 16GB 2400MHz": "DDR4",
                "TeamGroup Elite DDR4 8GB 2666MHz": "DDR4",
                "ADATA Premier DDR4 8GB 2400MHz": "DDR4",
                "Patriot Signature DDR4 16GB 3200MHz": "DDR4",
                "Kingston ValueRAM DDR4 4GB 2133MHz": "DDR4",
                "G.Skill Aegis DDR4 8GB 3000MHz": "DDR4",
                "Corsair LPX DDR4 16GB 3200MHz": "DDR4",
                "Crucial Ballistix RGB DDR4 32GB 3600MHz": "DDR4",
                "Team T-Force Dark DDR4 8GBx2 3200MHz": "DDR4",
                "Kingston HyperX Fury DDR4 8GB 2400MHz": "DDR4",
                "ADATA XPG Flame DDR4 16GB 3000MHz": "DDR4",
                "G.Skill Trident Z Royal DDR4 64GB 4000MHz": "DDR4",
                "Patriot Viper RGB DDR4 16GB 3200MHz": "DDR4",
                "Corsair Dominator RGB DDR4 32GB 3600MHz": "DDR4",
                "Kingston Fury Impact DDR4 8GB 2666MHz": "DDR4",
                "G.Skill Flare X DDR4 16GB 3200MHz": "DDR4",
                "Corsair Vengeance Pro DDR4 8GBx2 3000MHz": "DDR4",
                "Kingston HyperX Fury DDR3 8GB 1600MHz": "DDR3",
                "Corsair Vengeance DDR3 4GBx2 1600MHz": "DDR3",
                "G.Skill Ripjaws X DDR3 16GB 1866MHz": "DDR3",
                "Crucial Ballistix DDR3 8GB 1600MHz": "DDR3",
                "ADATA XPG V2 DDR3 8GBx2 2400MHz": "DDR3",
                "Team Elite DDR3 4GB 1333MHz": "DDR3",
                "Patriot Signature DDR3 8GB 1600MHz": "DDR3",
                "Mushkin Enhanced Silverline DDR3 4GBx2 1600MHz": "DDR3",
                "Samsung DDR3 4GB 1333MHz": "DDR3",
                "Hynix DDR3 8GB 1600MHz": "DDR3",
                "Corsair Dominator DDR3 8GBx2 2133MHz": "DDR3",
                "G.Skill Ares DDR3 16GB 1600MHz": "DDR3",
                "Crucial DDR3 8GB 1333MHz": "DDR3",
                "ADATA Premier DDR3 4GB 1600MHz": "DDR3",
                "Patriot Viper III DDR3 8GBx2 1866MHz": "DDR3",
                "Kingston ValueRAM DDR3 4GB 1600MHz": "DDR3",
                "Corsair XMS3 DDR3 8GB 1600MHz": "DDR3",
                "Team Vulcan DDR3 4GBx2 2133MHz": "DDR3",
                "Mushkin Redline DDR3 8GBx2 2400MHz": "DDR3",
                "Kingston HyperX Genesis DDR3 4GBx2 1600MHz": "DDR3"
            }.get(components["RAM"], None)

            motherboard_ram_type = {
                "Kingston Fury Beast DDR4 16GB 3200MHz": "DDR4",
                "Corsair Vengeance LPX DDR4 8GBx2 3000MHz": "DDR4",
                "G.Skill Trident Z RGB DDR4 32GB 3600MHz": "DDR4",
                "Crucial Ballistix DDR4 16GB 2666MHz": "DDR4",
                "Team T-Force Vulcan DDR4 8GBx2 3000MHz": "DDR4",
                "Kingston HyperX Predator DDR4 16GB 4000MHz": "DDR4",
                "Corsair Dominator Platinum DDR4 64GB 3200MHz": "DDR4",
                "G.Skill Ripjaws V DDR4 16GB 3600MHz": "DDR4",
                "Patriot Viper Steel DDR4 8GBx2 3000MHz": "DDR4",
                "ADATA XPG Spectrix D60G DDR4 16GB 3200MHz": "DDR4",
                "Kingston Fury Renegade DDR4 32GB 3600MHz": "DDR4",
                "Corsair Vengeance RGB Pro DDR4 16GBx2 3200MHz": "DDR4",
                "G.Skill Trident Z Neo DDR4 16GB 3600MHz": "DDR4",
                "Crucial DDR4 16GB 2400MHz": "DDR4",
                "TeamGroup Elite DDR4 8GB 2666MHz": "DDR4",
                "ADATA Premier DDR4 8GB 2400MHz": "DDR4",
                "Patriot Signature DDR4 16GB 3200MHz": "DDR4",
                "Kingston ValueRAM DDR4 4GB 2133MHz": "DDR4",
                "G.Skill Aegis DDR4 8GB 3000MHz": "DDR4",
                "Corsair LPX DDR4 16GB 3200MHz": "DDR4",
                "Crucial Ballistix RGB DDR4 32GB 3600MHz": "DDR4",
                "Team T-Force Dark DDR4 8GBx2 3200MHz": "DDR4",
                "Kingston HyperX Fury DDR4 8GB 2400MHz": "DDR4",
                "ADATA XPG Flame DDR4 16GB 3000MHz": "DDR4",
                "G.Skill Trident Z Royal DDR4 64GB 4000MHz": "DDR4",
                "Patriot Viper RGB DDR4 16GB 3200MHz": "DDR4",
                "Corsair Dominator RGB DDR4 32GB 3600MHz": "DDR4",
                "Kingston Fury Impact DDR4 8GB 2666MHz": "DDR4",
                "G.Skill Flare X DDR4 16GB 3200MHz": "DDR4",
                "Corsair Vengeance Pro DDR4 8GBx2 3000MHz": "DDR4",
                 "Kingston HyperX Fury DDR3 8GB 1600MHz": "DDR3",
                "Corsair Vengeance DDR3 4GBx2 1600MHz": "DDR3",
                "G.Skill Ripjaws X DDR3 16GB 1866MHz": "DDR3",
                "Crucial Ballistix DDR3 8GB 1600MHz": "DDR3",
                "ADATA XPG V2 DDR3 8GBx2 2400MHz": "DDR3",
                "Team Elite DDR3 4GB 1333MHz": "DDR3",
                "Patriot Signature DDR3 8GB 1600MHz": "DDR3",
                "Mushkin Enhanced Silverline DDR3 4GBx2 1600MHz": "DDR3",
                "Samsung DDR3 4GB 1333MHz": "DDR3",
                "Hynix DDR3 8GB 1600MHz": "DDR3",
                "Corsair Dominator DDR3 8GBx2 2133MHz": "DDR3",
                "G.Skill Ares DDR3 16GB 1600MHz": "DDR3",
                "Crucial DDR3 8GB 1333MHz": "DDR3",
                "ADATA Premier DDR3 4GB 1600MHz": "DDR3",
                "Patriot Viper III DDR3 8GBx2 1866MHz": "DDR3",
                "Kingston ValueRAM DDR3 4GB 1600MHz": "DDR3",
                "Corsair XMS3 DDR3 8GB 1600MHz": "DDR3",
                "Team Vulcan DDR3 4GBx2 2133MHz": "DDR3",
                "Mushkin Redline DDR3 8GBx2 2400MHz": "DDR3",
                "Kingston HyperX Genesis DDR3 4GBx2 1600MHz": "DDR3"
            }.get(components["Motherboard"], None)

            if ram_type and motherboard_ram_type:
                if ram_type != motherboard_ram_type:
                    issues.append(
                        f"Тип оперативної пам'яті ({ram_type}) не відповідає підтримуваному типу материнської плати ({motherboard_ram_type})."
                    )

        except Exception as e:
            issues.append(f"An error occurred during compatibility check: {str(e)}")

    if not issues:
        return {"compatible": True, "message": "Всі компоненти сумісні!"}

    return {"compatible": False, "issues": issues}
