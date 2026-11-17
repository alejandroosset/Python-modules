def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
    match unit:
        case "packets":
            print(seed_type,"seeds:", quantity, unit, "available")
        case "grams":
            print(seed_type,"seeds:",quantity, unit, "total")
        case "area":
            print(seed_type,"seeds: covers",quantity, unit, "square meters")
        case _:
            print("Unknown unit type")