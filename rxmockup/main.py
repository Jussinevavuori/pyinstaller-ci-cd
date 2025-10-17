import rxmockup.secret as secret
from rxmockup.inductance_calculation_coefficients import PHI_DF
import time
import numpy as np


def run(json_input_data, output_file_directory):
    print("Starting rxmockup...")
    reactor_purpose = json_input_data["reactorPurpose"]
    inductance = json_input_data["inductance_mH"] / 1000
    inductance_positive_tolerance_percent = json_input_data["inductancePositiveTolerance_percent"]
    inductance_negative_tolerance_percent = json_input_data["inductanceNegativeTolerance_percent"]
    base_frequency = json_input_data["baseFrequency_Hz"]
    nominal_voltage = json_input_data["nominalVoltage_kV"] * 1000
    required_BIL = json_input_data["basicImpulseLevel_kV"] * 1000
    nominal_current = json_input_data["nominalCurrent_A"]
    pollution_class = json_input_data["pollutionClass"] # A=very mild, B=mild, C=medium, D=heavy, E=very heavy
    harmonic_spectrum = json_input_data["harmonicSpectrum"]

    warehouse_database = json_input_data["snapshots"]["warehouse"]["items"]
    manufacturing_constraints = json_input_data["snapshots"]["constraintSet"]["constraints"]
    user_defined_max_height = json_input_data["maxHeight_m"]
    user_defined_max_width = json_input_data["maxWidth_m"]
    user_defined_max_mass = json_input_data["maxMass_kg"]

    start_time = time.time()
    output_json_str = secret.generate_multi_cyl_reactors(output_file_directory, PHI_DF, reactor_purpose, inductance, inductance_positive_tolerance_percent, inductance_negative_tolerance_percent, nominal_voltage, required_BIL, nominal_current, harmonic_spectrum, pollution_class, base_frequency, warehouse_database, manufacturing_constraints, user_defined_max_width, user_defined_max_height, user_defined_max_mass, 15)
    end_time = time.time()
    print("Reactor designs generated, time elapsed = " + str(np.ceil(end_time - start_time)) + " s.")
    print("Process output:")
    print(output_json_str)
    
