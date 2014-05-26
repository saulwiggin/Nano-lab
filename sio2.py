# -------------------------------------------------------------
# Bulk configuration
# -------------------------------------------------------------

# Set up lattice
lattice = FaceCenteredCubic(7.166*Angstrom)

# Define elements
elements = [Silicon, Silicon, Oxygen, Oxygen, Oxygen, Oxygen]

# Define coordinates
fractional_coordinates = [[ 0.125,  0.125,  0.125],
                          [ 0.875,  0.875,  0.875],
                          [ 0.   ,  0.   ,  0.   ],
                          [ 0.   ,  0.5  , -0.   ],
                          [ 0.5  ,  0.   , -0.   ],
                          [ 0.   ,  0.   ,  0.5  ]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )

# -------------------------------------------------------------
# Calculator
# -------------------------------------------------------------
numerical_accuracy_parameters = NumericalAccuracyParameters(
    k_point_sampling=(5, 5, 5),
    )

calculator = HuckelCalculator(
    numerical_accuracy_parameters=numerical_accuracy_parameters,
    )

bulk_configuration.setCalculator(calculator)
nlprint(bulk_configuration)
bulk_configuration.update()
nlsave('C:/Users/Wigglebrain/Documents/GitHub/Nano-lab/SiO2.nc', bulk_configuration)

# -------------------------------------------------------------
# Bandstructure
# -------------------------------------------------------------
bandstructure = Bandstructure(
    configuration=bulk_configuration,
    route=['G', 'X', 'W', 'L', 'G', 'K', 'X', 'U', 'W', 'K', 'L'],
    points_per_segment=100,
    bands_above_fermi_level=All
    )
nlsave('C:/Users/Wigglebrain/Documents/GitHub/Nano-lab/SiO2.nc', bandstructure)

# -------------------------------------------------------------
# Electrostatic difference potential
# -------------------------------------------------------------
electrostatic_difference_potential = ElectrostaticDifferencePotential(bulk_configuration)
nlsave('C:/Users/Wigglebrain/Documents/GitHub/Nano-lab/SiO2.nc', electrostatic_difference_potential)