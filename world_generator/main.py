import random

main_world_sizes = [
    {"size": 0, "unicode": "0", "diameter": "Less than 1000 km", "example": "Asteroid, Orbital Complex", "gravity": "Negligible", "common features": "Uninhabitable by most forms of life without technical support."},
    {"size": 1, "unicode": "1", "diameter": "1,600 km", "example": "Large Asteroid, Typical Moon", "gravity": "0.05 (Low gravity)", "common features": "Improbable-looking rock formations, thin and spindly lifeforms, and flying as a common form of locomotion."},
    {"size": 2, "unicode": "2", "diameter": "3,200 km", "example": "Typical Moon, Large Moon, Small Planet, Pluto", "gravity": "0.15 (Low gravity)", "common features": "Improbable-looking rock formations, thin and spindly lifeforms, and flying as a common form of locomotion."},
    {"size": 3, "unicode": "3", "diameter": "4,800 km", "example": "Large Moon, Small Planet, Mercury", "gravity": "0.25 (Low gravity)", "common features": "Improbable-looking rock formations, thin and spindly lifeforms, and flying as a common form of locomotion."},
    {"size": 4, "unicode": "4", "diameter": "6,400 km", "example": "Small Planet, Typical Planet, Mars", "gravity": "0.35 (Low gravity)", "common features": "Improbable-looking rock formations, thin and spindly lifeforms, and flying as a common form of locomotion."},
    {"size": 5, "unicode": "5", "diameter": "8,000 km", "example": "Typical Planet", "gravity": "0.45 (Low gravity)", "common features": "Improbable-looking rock formations, thin and spindly lifeforms, and flying as a common form of locomotion."},
    {"size": 6, "unicode": "6", "diameter": "9,600 km", "example": "Typical Planet", "gravity": "0.7 (Low gravity)", "common features": "Improbable-looking rock formations, thin and spindly lifeforms, and flying as a common form of locomotion."},
    {"size": 7, "unicode": "7", "diameter": "11,200 km", "example": "Typical Planet, Venus", "gravity": "0.9 (Earth-like gravity)", "common features": "Variable"},
    {"size": 8, "unicode": "8", "diameter": "12,800 km", "example": "Typical Planet, Earth", "gravity": "1.0 (Earth-like gravity)", "common features": "Variable"},
    {"size": 9, "unicode": "9", "diameter": "14,400 km", "example": "Typical Planet, Larger than Earth", "gravity": "1.25 (Earth-like gravity)", "common features": "Variable"},
    {"size": 10, "unicode": "A", "diameter": "Greater than 16,000 km", "example": "Large Planet", "gravity": "1.4 (High gravity)", "common features": "Wide rocky plains, squat, muscular creatures and plant life that spreads out like lichen instead of growing up. Crawling, burrowing or swimming are the most common forms of locomotion."}
]

main_world_atmospheres = [
    {"atmos": 0, "unicode": "0", "composition": "None", "pressure": "0.00", "gear": "Vacc Suit"},
    {"atmos": 1, "unicode": "1", "composition": "Trace", "pressure": "0.001-0.09", "gear": "Vacc Suit"},
    {"atmos": 2, "unicode": "2", "composition": "Very Thin, Tainted - Contain elements harmful to humans, such as unusually high proportion of CO2.", "pressure": "0.1-0.42", "gear": "Respirator, Filter"},
    {"atmos": 3, "unicode": "3", "composition": "Very Thin", "pressure": "0.1-0.42", "gear": "Respirator"},
    {"atmos": 4, "unicode": "4", "composition": "Thin, Tainted - Contain elements harmful to humans, such as unusually high proportion of CO2.", "pressure": "0.43-0.7", "gear": "Filter"},
    {"atmos": 5, "unicode": "5", "composition": "Thin", "pressure": "0.43-0.7", "gear": "None"},
    {"atmos": 6, "unicode": "6", "composition": "Standard", "pressure": "0.71-1.49", "gear": "None"},
    {"atmos": 7, "unicode": "7", "composition": "Standard, Tainted - Contain elements harmful to humans, such as unusually high proportion of CO2.", "pressure": "0.71-1.49", "gear": "Filter"},
    {"atmos": 8, "unicode": "8", "composition": "Dense", "pressure": "1.5-2.49", "gear": "None"},
    {"atmos": 9, "unicode": "9", "composition": "Dense, Tainted - Contain elements harmful to humans, such as unusually high proportion of CO2.", "pressure": "1.5-2.49", "gear": "Filter"},
    {"atmos": 10, "unicode": "A", "composition": "Exotic - Unbreathable by humans but not otherwise hazardous.", "pressure": "Varies", "gear": "Air Supply"},
    {"atmos": 11, "unicode": "B", "composition": "Corrosive - Highly dangerous! Do not breathe!", "pressure": "Varies", "gear": "Vacc Suit"},
    {"atmos": 12, "unicode": "C", "composition": "Insidious - Highly dangerous! Do not breathe! Toxic gasses may destroy the seals and filters on protective gear.", "pressure": "Varies", "gear": "Vacc Suit"},
    {"atmos": 13, "unicode": "D", "composition": "Very Dense - High pressure nitrogen and oxygen. Deadly to humans. Pressure decreases with increasing altitudes.", "pressure": "2.5+", "gear": "None"},
    {"atmos": 14, "unicode": "E", "composition": "Low - Thin nitrogen and oxygen atmospheres that settle in lowlands and depressions, only breathable there. Pressure drops rapidly to a vaccum at higher altitudes.", "pressure": "0.5 or less", "gear": "None"},
    {"atmos": 15, "unicode": "F", "composition": "Unusual - Erratic, Changeable atmosphere.", "pressure": "Varies", "gear": "Varies"}
]

main_world_temperatures = [
    {"roll": 2, "type": "Frozen", "avg-temp": "Lower than -51°C", "description": "No liquid water. Very dry atmosphere."},
    {"roll": 3, "type": "Cold", "avg-temp": "-51°C to 0°C", "description": "Icy. Little liquid water, extensive ice caps, few clouds."},
    {"roll": 4, "type": "Cold", "avg-temp": "-51°C to 0°C", "description": "Icy. Little liquid water, extensive ice caps, few clouds."},
    {"roll": 5, "type": "Temperate", "avg-temp": "0°C to 30°C", "description": "Liquid, vaporised water, and ice caps may be present."},
    {"roll": 6, "type": "Temperate", "avg-temp": "0°C to 30°C", "description": "Liquid, vaporised water, and ice caps may be present."},
    {"roll": 7, "type": "Temperate", "avg-temp": "0°C to 30°C", "description": "Liquid, vaporised water, and ice caps may be present."},
    {"roll": 8, "type": "Temperate", "avg-temp": "0°C to 30°C", "description": "Liquid, vaporised water, and ice caps may be present."},
    {"roll": 9, "type": "Temperate", "avg-temp": "0°C to 30°C", "description": "Liquid, vaporised water, and ice caps may be present."},
    {"roll": 10, "type": "Hot", "avg-temp": "31°C to 80°C", "description": "Small or no ice caps, little liquid water. Most water in the form of clouds."},
    {"roll": 11, "type": "Hot", "avg-temp": "31°C to 80°C", "description": "Small or no ice caps, little liquid water. Most water in the form of clouds."},
    {"roll": 12, "type": "Boiling", "avg-temp": "81°C or higher", "description": "No ice caps, little liquid water."}
]

main_world_hydrographics = [
    {"hydro": 0, "unicode": "0", "percent": "0-5%", "description": "Desert"},
    {"hydro": 1, "unicode": "1", "percent": "6-15%", "description": "Dry"},
    {"hydro": 2, "unicode": "2", "percent": "16-25%", "description": "A few small seas"},
    {"hydro": 3, "unicode": "3", "percent": "26-35%", "description": "Small seas and oceans"},
    {"hydro": 4, "unicode": "4", "percent": "36-45%", "description": "Wet"},
    {"hydro": 5, "unicode": "5", "percent": "46-55%", "description": "A large ocean"},
    {"hydro": 6, "unicode": "6", "percent": "56-65%", "description": "Large oceans"},
    {"hydro": 7, "unicode": "7", "percent": "66-75%", "description": "Earth-like"},
    {"hydro": 8, "unicode": "8", "percent": "76-85%", "description": "A few islands and archipelagos"},
    {"hydro": 9, "unicode": "9", "percent": "86-95%", "description": "Almost entirely water"},
    {"hydro": 10, "unicode": "A", "percent": "96-100%", "description": "Water"}
]

main_world_populations = [
    {"roll": 0, "unicode": "0", "inhabs": "None", "range": "0", "description": "No people"},
    {"roll": 1, "unicode": "1", "inhabs": "Few", "range": "1+", "description": "A tiny farmstead or single family"},
    {"roll": 2, "unicode": "2", "inhabs": "Hundreds", "range": "100+", "description": "A hamlet"},
    {"roll": 3, "unicode": "3", "inhabs": "Thousands", "range": "1,000+", "description": "A village"},
    {"roll": 4, "unicode": "4", "inhabs": "Tens of Thousands", "range": "10,000+", "description": "Small town"},
    {"roll": 5, "unicode": "5", "inhabs": "Hundreds of Thousands", "range": "100,000+", "description": "Average city"},
    {"roll": 6, "unicode": "6", "inhabs": "Millions", "range": "1,000,000+", "description": "Medium city"},
    {"roll": 7, "unicode": "7", "inhabs": "Tens of Millions", "range": "10,000,000+", "description": "Large city"},
    {"roll": 8, "unicode": "8", "inhabs": "Hundreds of Millions", "range": "100,000,000+", "description": "Megalopolis"},
    {"roll": 9, "unicode": "9", "inhabs": "Billions", "range": "1,000,000,000+", "description": "Present day Earth"},
    {"roll": 10, "unicode": "A", "inhabs": "Tens of Billions", "range": "10,000,000,000+", "description": "Very crowded world"},
    {"roll": 11, "unicode": "B", "inhabs": "Hundreds of Billions", "range": "100,000,000,000+", "description": "Incredibly crowded world"},
    {"roll": 12, "unicode": "C", "inhabs": "Trillions", "range": "1,000,000,000,000+", "description": "World-city"}
]

main_world_governments = [
    {"roll": 0, "unicode": "0", "type": "None", "description": "No government structure. In many cases, family bonds predominate.", "examples": "Family, Clan, Anarchy", "contraband": "None"},
    {"roll": 1, "unicode": "1", "type": "Company / Corporation", "description": "Ruling functions are assumed by a company managerial elite and most citizenry are company employees or dependants.", "examples": "Corporate outpost, Asteroid mine, Feudal domain", "contraband": "Weapons, Drugs, Travellers"},
    {"roll": 2, "unicode": "2", "type": "Participating Democracy", "description": "Ruling functions are reached by the advice and consent of the citizenry directly.", "examples": "Collective, Tribal council, Comm-linked consensus", "contraband": "Drugs"},
    {"roll": 3, "unicode": "3", "type": "Self-Perpetuating Oligarcy", "description": "Ruling functions are performed by a restricted minority, with little or no input from the mass of citizenry.", "examples": "Plutocracy, Hereditary ruling caste", "contraband": "Technology, Weapons, Travellers"},
    {"roll": 4, "unicode": "4", "type": "Representative Democracy", "description": "Ruling functions are performed by elected representatives.", "examples": "Republic, Democracy", "contraband": "Drugs, Weapons"},
    {"roll": 5, "unicode": "5", "type": "Feudal Technocracy", "description": "Ruling functions are performed by specific individuals for persons who agree to be ruled by them. Relationships are based on the performance of technical activities that are mutually beneficial.", "examples": "Those with access to advanced technology tend to have higher social status", "contraband": "Technology, Weapons, Computers"},
    {"roll": 6, "unicode": "6", "type": "Captive Government", "description": "Ruling functions are performed by an imposed leadership answerable to an outside group.", "examples": "A colony, Conquered area", "contraband": "Weapons, Technology, Travellers"},
    {"roll": 7, "unicode": "7", "type": "Balkanisation", "description": "No central authority exists; rival governments compete for control. Law Level refers to the government nearest the starport.", "examples": "Multiple governments, Civil war", "contraband": "Varies"},
    {"roll": 8, "unicode": "8", "type": "Civil Service Bureaucracy", "description": "Ruling functions are performed by government agencies employing individuals selected for their expertise.", "examples": "Technocracy, Communism", "contraband": "Drugs, Weapons"},
    {"roll": 9, "unicode": "9", "type": "Impersonal Bureaucracy", "description": "Ruling functions are performed by agencies that have become insulated from the governed citizens.", "examples": "Entrenched castes of bureaucrats, Decaying empire", "contraband": "Technology, Weapons, Drugs, Travellers"},
    {"roll": 10, "unicode": "A", "type": "Charismatic Dictator", "description": "Ruling functions are performed by agencies directed by a single leader who enjoys the overwhelming confidence of the citizens.", "examples": "Revolutionary leader, Messiah, Emperor", "contraband": "None"},
    {"roll": 11, "unicode": "B", "type": "Non-Charismatic Leader", "description": "A previous charismatic dictator has been replaced by a leader through normal channels.", "examples": "Military dictatorship, Hereditary kingship", "contraband": "Weapons, Technology, Computers"},
    {"roll": 12, "unicode": "C", "type": "Charismatic Oligarchy", "description": "Ruling functions are performed by a select group of members of an organisation or class that enjoys the overwhelming confidence of the citizenry.", "examples": "Junta, Revolutionary council", "contraband": "Weapons"},
    {"roll": 13, "unicode": "D", "type": "Religious Dictatorship", "description": "Ruling functions are performed by a religious organisation without regard to the specific individual needs of the citizenry.", "examples": "Cult, Transcendent philosophy, Psionic group mind", "contraband": "Varies"},
    {"roll": 14, "unicode": "E", "type": "Religious Autocracy", "description": "Government by a single religious leader having absolute power over the citizenry.", "examples": "Messiah", "contraband": "Varies"},
    {"roll": 15, "unicode": "F", "type": "Totalitarian Oligarchy", "description": "Government by an all-powerful minority that maintains absolute control through widespread coercion and oppression.", "examples": "World church, Ruthless corporation", "contraband": "Varies"},
]

main_world_law_level = [
    {"law_level": 0, "banned_weapons": "No restrictions. Heavy armor and a weapon are recommended...", "banned_armor": "None"},
    {"law_level": 1, "banned_weapons": "Poison gas, explosives, undetectable weapons, WMD", "banned_armor": "Battle dress"},
    {"law_level": 2, "banned_weapons": "Portable energy and laser weapons", "banned_armor": "Battle dress, Combat armor"},
    {"law_level": 3, "banned_weapons": "Military weapons", "banned_armor": "Battle dress, Combat armor, Flak Jacket"},
    {"law_level": 4, "banned_weapons": "Light assault weapons and submachine guns", "banned_armor": "Battle dress, Combat armor, Flak Jacket, Cloth"},
    {"law_level": 5, "banned_weapons": "Personal concealable weapons", "banned_armor": "Battle dress, Combat armor, Flak Jacket, Cloth, Mesh"},
    {"law_level": 6, "banned_weapons": "All firearms except shotguns and stunners; carrying weapons discouraged", "banned_armor": "Battle dress, Combat armor, Flak Jacket, Cloth, Mesh"},
    {"law_level": 7, "banned_weapons": "Shotguns", "banned_armor": "Battle dress, Combat armor, Flak Jacket, Cloth, Mesh"},
    {"law_level": 8, "banned_weapons": "All bladed weapons, stunners", "banned_armor": "All visible armor"},
    {"law_level": 9, "banned_weapons": "All weapons", "banned_armor": "All armor (visible or concealed)"}
]

main_world_starports = [
    {"value": 2, "class": "X", "quality": "No Starport", "berth_cost": "n/a", "fuel": "n/a", "facilities": "n/a", "bases": "n/a"},
    {"value": 3, "class": "E", "quality": "Frontier", "berth_cost": "0", "fuel": "n/a", "facilities": "n/a", "bases": "n/a"},
    {"value": 4, "class": "E", "quality": "Frontier", "berth_cost": "0", "fuel": "n/a", "facilities": "n/a", "bases": "n/a"},
    {"value": 5, "class": "D", "quality": "Poor", "berth_cost": "1D x Cr10", "fuel": "Unrefined", "facilities": "Limited Repair, Highport 12+", "bases": "Scout 8+"},
    {"value": 6, "class": "D", "quality": "Poor", "berth_cost": "1D x Cr10", "fuel": "Unrefined", "facilities": "Limited Repair, Highport 12+", "bases": "Scout 8+"},
    {"value": 7, "class": "C", "quality": "Routine", "berth_cost": "1D x Cr100", "fuel": "Unrefined", "facilities": "Shipyard (small craft), Repair, Highport 10+", "bases": "Scout 9+"},
    {"value": 8, "class": "C", "quality": "Routine", "berth_cost": "1D x Cr100", "fuel": "Unrefined", "facilities": "Shipyard (small craft), Repair, Highport 10+", "bases": "Scout 9+"},
    {"value": 9, "class": "B", "quality": "Good", "berth_cost": "1D x Cr500", "fuel": "Refined", "facilities": "Shipyard (spacecraft), Repair, Highport 8+", "bases": "Naval 8+, Scout 9+"},
    {"value": 10, "class": "B", "quality": "Good", "berth_cost": "1D x Cr500", "fuel": "Refined", "facilities": "Shipyard (spacecraft), Repair, Highport 8+", "bases": "Naval 8+, Scout 9+"},
    {"value": 11, "class": "A", "quality": "Excellent", "berth_cost": "1D x Cr1000", "fuel": "Refined", "facilities": "Shipyard (all), Repair, Highport 6+", "bases": "Naval 8+, Scout 10+"}
]

tech_level_mods = {
    "starport": {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "A":6, "B":4, "C":2, "D":0, "E":0, "F":0, "X":-4},
    "size": {"0":2, "1":2, "2":1, "3":1, "4":1, "5":0, "6":0, "7":0, "8":0, "9":0, "A":0, "B":0, "C":0, "D":0, "E":0, "F":0, "X":0},
    "atmosphere": {"0":1, "1":1, "2":1, "3":1, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "A":1, "B":1, "C":1, "D":1, "E":1, "F":1, "X":0},
    "hydrographics": {"0":1, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":1, "A":2, "B":0, "C":0, "D":0, "E":0, "F":0, "X":0},
    "population": {"0":0, "1":1, "2":1, "3":1, "4":1, "5":1, "6":0, "7":0, "8":1, "9":2, "A":4, "B":0, "C":0, "D":0, "E":0, "F":0, "X":0},
    "government": {"0":1, "1":0, "2":0, "3":0, "4":0, "5":1, "6":0, "7":2, "8":0, "9":0, "A":0, "B":0, "C":0, "D":-2, "E":-2, "F":0, "X":0}
}

def build_lookup(table, key):
    return {row[key]: row for row in table}

# LOOKUP TABLES
size_lookup = build_lookup(main_world_sizes, "size")
atmosphere_lookup = build_lookup(main_world_atmospheres, "atmos")
temp_lookup = build_lookup(main_world_temperatures, "roll")
hydro_lookup = build_lookup(main_world_hydrographics, "hydro")
pop_lookup = build_lookup(main_world_populations, "roll")
gov_lookup = build_lookup(main_world_governments, "roll")
law_lookup = build_lookup(main_world_law_level, "law_level")
starport_lookup = build_lookup(main_world_starports, "value")

HEX = "0123456789ABCDEF"

def roll(dice, sides=6):
    return sum(random.randint(1, sides) for _ in range(dice))

def clamp(value, low, high):
    return max(low, min(high, value))

def to_hex(value):
    return HEX[value]

def generate_size():
    value = roll(2) -2
    return size_lookup[value]

def generate_atmosphere(size):
    value = clamp(roll(2) - 7 + size, 0, 15)
    return atmosphere_lookup[value]

def generate_temperature(atmos):
    
    dm_table = {
        (0,1): 0,
        (2,3): -2,
        (4,5,14): -1,
        (6,7): 0,
        (8,9): 1,
        (10,13,15): 2,
        (11,12): 6
    }

    dm = next(v for k,v in dm_table.items() if atmos in k)

    value = clamp(roll(2) + dm, 2, 12)

    #return temp_lookup[value]
    return temp_lookup[value]


def generate_hydro(size, atmos, temp):

    if size < 2:
        value = 0
    else:
        atmos_dm = -4 if atmos in (0, 1, 10, 11, 12) else 0

        if atmos in (13, 15):
            temp_dm = 0
        elif temp == "Hot":
            temp_dm = -2
        elif temp == "Boiling":
            temp_dm = -6
        else:
            temp_dm = 0

        value = clamp(roll(2) - 7 + atmos + atmos_dm + temp_dm, 0, 10)

    return hydro_lookup[value]

def generate_population():
    value = clamp(roll(2) -2, 0, 12)
    return pop_lookup[value]

def generate_government(pop):
    value = clamp(roll(2) -7 + pop, 0, 15)
    if pop < 1:
        value = 0

    return gov_lookup[value]

def generate_law_level(gov):
    value = clamp(roll(2) -7 + gov, 0, 9)
    return law_lookup[value]

def generate_starport(pop):
    
    dm = 0
    if pop >= 8: dm += 1
    if pop >= 10: dm += 2
    if pop <= 4: dm -= 1
    if pop <= 2: dm -= 2

    value = clamp(roll(2) + dm, 2, 11)
    return starport_lookup[value]

def generate_tech_level(chars):
    
    tech_roll = roll(1)

    mods = (
        tech_level_mods["starport"][chars["starport"]] +
        tech_level_mods["size"][chars["size"]] +
        tech_level_mods["atmosphere"][chars["atmosphere"]] +
        tech_level_mods["hydrographics"][chars["hydrographics"]] +
        tech_level_mods["population"][chars["population"]] +
        tech_level_mods["government"][chars["government"]]
    )

    return max(0, tech_roll + mods)

def world():
    world_size = generate_size()
    size = world_size["size"]
    unicode_size = world_size['unicode']
    diameter = world_size["diameter"]
    example = world_size["example"]
    gravity = world_size['gravity']
    common_features = world_size['common features']

    world_atmosphere = generate_atmosphere(size)
    atmos = world_atmosphere['atmos']
    unicode_atmos = world_atmosphere['unicode']
    composition = world_atmosphere['composition']
    pressure = world_atmosphere['pressure']
    gear = world_atmosphere['gear']

    world_temperature = generate_temperature(atmos)
    temp = world_temperature["type"]
    avg_temp = world_temperature["avg-temp"]
    temp_description = world_temperature['description']

    world_hydro = generate_hydro(size, atmos, temp)
    unicode_hydro = world_hydro['unicode']
    hydro_percent = world_hydro['percent']
    hydro_description = world_hydro['description']

    world_population = generate_population()
    pop = world_population['roll']
    unicode_population = world_population['unicode']
    population_inhabs = world_population['inhabs']
    population_range = world_population['range']
    population_description = world_population['description']

    world_government = generate_government(pop)
    gov = world_government['roll']
    unicode_gov = world_government['unicode']
    gov_type = world_government['type']
    gov_description = world_government['description']
    gov_examples = world_government['examples']
    gov_contraband = world_government['contraband']

    world_law_level = generate_law_level(gov)
    law_level = world_law_level['law_level']
    law_weapons_banned = world_law_level['banned_weapons']
    law_armor_banned = world_law_level['banned_armor']

    world_starport = generate_starport(pop)
    starport_value = world_starport['value']
    starport_class = world_starport['class']
    starport_quality = world_starport['quality']
    starport_berth_cost = world_starport['berth_cost']
    starport_fuel = world_starport['fuel']
    starport_facilities = world_starport['facilities']
    starport_bases = world_starport['bases']

    planetCharacteristicLabels = {
        "starport": starport_class, 
        "size": unicode_size, 
        "atmosphere": unicode_atmos,
        "hydrographics": unicode_hydro,
        "population": unicode_population,
        "government": unicode_gov
        }
    
    tech_level = generate_tech_level(planetCharacteristicLabels)

    print("\nWORLD SUMMARY")
    print(f"Name 0101 {starport_class}{unicode_size}{unicode_atmos}{unicode_hydro}{unicode_population}{unicode_gov}{law_level}-{tech_level}")
    print()
    print(f"STARPORT ({starport_class}) {starport_quality}, Fuel: {starport_fuel}")
    print("Berthing Cost:", starport_berth_cost)
    print("Facilities:", starport_facilities)
    print("Bases:", starport_bases)
    print()
    print(f"SIZE ({unicode_size}) {diameter}, {gravity}")
    print("Examples:", example)
    print("Common Features:", common_features)
    print()
    print(f"ATMOSPHERE ({unicode_atmos})")
    print(composition)
    print("Pressure:", pressure)
    print("Required Protection:", gear)
    print()
    print(f"TEMPERATURE {avg_temp}, {temp}")
    print(temp_description)
    print()
    print(f"HYDROGRAPHICS ({unicode_hydro}) {hydro_percent}, {hydro_description}")
    print()
    print(f"POPULATION ({unicode_population}) {population_range} ({population_inhabs}), {population_description}")
    print()
    print(f"GOVERNMENT ({unicode_gov}) {gov_type}")
    print(f"{gov_description}\nExamples: {gov_examples}.")
    print("Possible Contraband:", gov_contraband)
    print()
    print(f"LAW LEVEL ({law_level})")
    print("Banned Weapons:", law_weapons_banned)
    print("Banned Armor:", law_armor_banned)
    print()
    print(f"TECH LEVEL ({tech_level})")


if __name__ == "__main__":
    world()