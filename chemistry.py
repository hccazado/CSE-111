from formula import parse_formula

# Indexes for inner lists in the periodic table
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1
ATOMIC_NUMBER_INDEX = 2

# Indexes for inner lists in a symbol_quantity_list
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1

#Dictionary of know molecules
known_molecules_dict = {
        "Al2O3": "aluminum oxide",
        "CH3OH": "methanol",
        "C2H6O": "ethanol",
        "C2H5OH": "ethanol",
        "C3H8O": "isopropyl alcohol",
        "C3H8": "propane",
        "C4H10": "butane",
        "C6H6": "benzene",
        "C6H14": "hexane",
        "C8H18": "octane",
        "CH3(CH2)6CH3": "octane",
        "C13H18O2": "ibuprofen",
        "C13H16N2O2": "melatonin",
        "Fe2O3": "iron oxide",
        "FeS2": "iron pyrite",
        "H2O": "water"
}

def make_periodic_table():
    """make and return a compound list containing the 94 naturally occuring elements."""
    
    periodic_table_list = {
        #[symbol, name, atomic mass, atomic number]
        "Ac": [	"Actinium",	227, 89],
        "Ag": [	"Silver",	107.8682, 47],
        "Al": [	"Aluminum",	26.9815386, 13],
        "Ar": [	"Argon",	39.948, 18],
        "As": [	"Arsenic",	74.9216, 33],
        "At": [	"Astatine",	210, 85],
        "Au": [	"Gold",	196.966569, 79],
        "B": ["Boron",	10.811, 5],
        "Ba": [	"Barium",	137.327, 56],
        "Be": [	"Beryllium",	9.012182, 4],
        "Bi": [	"Bismuth",	208.9804, 83],
        "Br": [	"Bromine",	79.904, 35],
        "C": ["Carbon",	12.0107, 6],
        "Ca": [	"Calcium",	40.078, 20],
        "Cd": [	"Cadmium",	112.411, 48],
        "Ce": [	"Cerium",	140.116, 58],
        "Cl": [	"Chlorine",	35.453, 17],
        "Co": [	"Cobalt",	58.933195, 27],
        "Cr": [	"Chromium",	51.9961, 24],
        "Cs": [	"Cesium",	132.9054519, 55],
        "Cu": [	"Copper",	63.546, 29],
        "Dy": [	"Dysprosium",	162.5, 66],
        "Er": [	"Erbium",	167.259, 68],
        "Eu": [	"Europium",	151.964, 63],
        "F": ["Fluorine",	18.9984032, 9],
        "Fe": [	"Iron",	55.845, 26],
        "Fr": [	"Francium",	223, 87],
        "Ga": [	"Gallium",	69.723, 31],
        "Gd": [	"Gadolinium",	157.25, 64],
        "Ge": [	"Germanium",	72.64, 32],
        "H": ["Hydrogen",	1.00794, 1],
        "He": [	"Helium",	4.002602, 2],
        "Hf": [	"Hafnium",	178.49, 72],
        "Hg": [	"Mercury",	200.59, 80],
        "Ho": [	"Holmium",	164.93032, 67],
        "I": ["Iodine",	126.90447, 53],
        "In": [	"Indium",	114.818, 49],
        "Ir": [	"Iridium",	192.217, 77],
        "K": ["Potassium",	39.0983, 19],
        "Kr": [	"Krypton",	83.798, 36],
        "La": [	"Lanthanum",	138.90547, 57],
        "Li": [	"Lithium",	6.941, 3],
        "Lu": [	"Lutetium",	174.9668, 71],
        "Mg": [	"Magnesium",	24.305, 12],
        "Mn": [	"Manganese",	54.938045, 25],
        "Mo": [	"Molybdenum",	95.96, 42],
        "N": ["Nitrogen",	14.0067, 7],
        "Na": [	"Sodium",	22.98976928, 11],
        "Nb": [	"Niobium",	92.90638, 41],
        "Nd": [	"Neodymium",	144.242, 60],
        "Ne": [	"Neon",	20.1797, 10],
        "Ni": [	"Nickel",	58.6934, 28],
        "Np": [	"Neptunium",	237, 93],
        "O": ["Oxygen",	15.9994, 8],
        "Os": [	"Osmium",	190.23, 76],
        "P": ["Phosphorus",	30.973762, 15],
        "Pa": [	"Protactinium",	231.03588, 91],
        "Pb": [	"Lead",	207.2, 82],
        "Pd": [	"Palladium",	106.42, 46],
        "Pm": [	"Promethium",	145, 61],
        "Po": [	"Polonium",	209, 84],
        "Pr": [	"Praseodymium",	140.90765, 59],
        "Pt": [	"Platinum",	195.084, 78],
        "Pu": [	"Plutonium",	244, 94],
        "Ra": [	"Radium",	226, 88],
        "Rb": [	"Rubidium",	85.4678, 37],
        "Re": [	"Rhenium",	186.207, 75],
        "Rh": [	"Rhodium",	102.9055, 45],
        "Rn": [	"Radon",	222, 86],
        "Ru": [	"Ruthenium",	101.07, 44],
        "S": ["Sulfur",	32.065, 16],
        "Sb": [	"Antimony",	121.76, 51],
        "Sc": [	"Scandium",	44.955912, 21],
        "Se": [	"Selenium",	78.96, 34],
        "Si": [	"Silicon",	28.0855, 14],
        "Sm": [	"Samarium",	150.36, 62],
        "Sn": [	"Tin",	118.71, 50],
        "Sr": [	"Strontium",	87.62, 38],
        "Ta": [	"Tantalum",	180.94788, 73],
        "Tb": [	"Terbium",	158.92535, 65],
        "Tc": [	"Technetium",	98, 43],
        "Te": [	"Tellurium",	127.6, 52],
        "Th": [	"Thorium",	232.03806, 90],
        "Ti": [	"Titanium",	47.867, 22],
        "Tl": [	"Thallium",	204.3833, 81],
        "Tm": [	"Thulium",	168.93421, 69],
        "U": ["Uranium",	238.02891, 92],
        "V": ["Vanadium",	50.9415, 23],
        "W": ["Tungsten",	183.84, 74],
        "Xe": [	"Xenon",	131.293, 54],
        "Y": ["Yttrium",	88.90585, 39],
        "Yb": [	"Ytterbium",	173.054, 70],
        "Zn": [	"Zinc",	65.38, 30],
        "Zr": [	"Zirconium",	91.224, 40]
    }
    
    return periodic_table_list


def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total molar mass of all the
    elements listed in symbol_quantity_list.

    Parameters
        symbol_quantity_list is a compound list returned
            from the parse_formula function. Each small
            list in symbol_quantity_list has this form:
            ["symbol", quantity].
        periodic_table_dict is the compound dictionary
            returned from make_periodic_table.
    Return: the total molar mass of all the elements in
        symbol_quantity_list.

    For example, if symbol_quantity_list is [["H", 2], ["O", 1]],
    this function will calculate and return
    atomic_mass("H") * 2 + atomic_mass("O") * 1
    1.00794 * 2 + 15.9994 * 1
    18.01528
    """
    
    total_molar_mass = 0
    
    #iterating the list of symbols and quantities    
    for inner_list in symbol_quantity_list:
        #destructuing each inner list
        symbol = inner_list[NAME_INDEX]
        quantity = inner_list[QUANTITY_INDEX]
        
        #getting element's data from the periodic table
        element = periodic_table_dict[symbol]
        element_mass = element[ATOMIC_MASS_INDEX]
        
        #calculating the molar mass of the current element
        molar_mass = element_mass * quantity
        
        total_molar_mass += molar_mass
        
    # Returning the total molar mass
    return total_molar_mass

def get_formula_name(formula, known_molecules_dict):
    """Try to find formula in the known_molecules_dict.
    If formula is in the known_molecules_dict, return
    the name of the chemical formula; otherwise return
    "unknown compound".

    Parameters
        formula is a string that contains a chemical formula
        known_molecules_dict is a dictionary that contains
            known chemical formulas and their names
    Return: the name of a chemical formula
    """
    
    formula_name = "Unknown Formula"
    
    #Verifying if the formula exists in the dictionary of known formulas
    if formula in known_molecules_dict:
        #replacing variable's default string with the returned value with the known formula's name
        formula_name = known_molecules_dict[formula]
        
    return formula_name

def sum_protons(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total number of protons in
    all the elements listed in symbol_quantity_list.

    Parameters
        symbol_quantity_list is a compound list returned
            from the parse_formula function. Each small
            list in symbol_quantity_list has this form:
            ["symbol", quantity].
        periodic_table_dict is the compound dictionary
            returned from make_periodic_table.
    Return: the total number of protons of all
        the elements in symbol_quantity_list.
    """
    
    total_num_protons = 0
    
    #iterating the list of symbols and quantities  
    for inner_list in symbol_quantity_list:
        symbol = inner_list[NAME_INDEX]
        quantity = inner_list[QUANTITY_INDEX]
        #getting the respective symbol's data from periodic table
        element = periodic_table_dict[symbol]
        #calculating the number of protons
        protons = element[ATOMIC_NUMBER_INDEX] * quantity
        
        #summing up formula's total number of protons
        total_num_protons += protons
        
    # Returning formula's number of protons
    return total_num_protons
    
    

def main ():
    """will ask the user for a chemical formula and weight of chemical sample.
    Then, computes the molar mass of a substance, and the number of moles of that
    substance.
    """
    
    chemical_formula = input("Type the chemical formula: ")
    
    mass = float(input("Type the mass in gr of a chemical sample: "))
    
    #getting a new instance of the periodic table
    periodic_table = make_periodic_table()
    
    #getting the symbol list from user's typed formula
    symbol_list = parse_formula(chemical_formula, periodic_table)
    
    #calculating formula's molar mass
    molar_mass = compute_molar_mass(symbol_list,periodic_table)
    
    #calculating number of moles based on user typed mass of chemical sample
    number_moles = mass / molar_mass
    
    #getting formula's name from dictionary of names
    formula_name = get_formula_name(chemical_formula, known_molecules_dict)
    
    #calculating formula's number of protons
    protons = sum_protons(symbol_list, periodic_table)
    
    print(f"{molar_mass} grams/mole")
    print(f"{number_moles:.5f} moles")
    print(f"Number of protons: {protons}")
    print(f"Formula name: {formula_name}")
    
        

#Executing the main function in case the program is being executed rather than imported
if __name__ == "__main__":
    main()