import numpy as np
import os
from reportlab.pdfgen.canvas import Canvas
import json

ENGINE_VERSION = "beta mockup 0.1"

def write_pdf(output_file_directory, reactor_purpose, required_inductance, inductance_positive_tolerance_percent, inductance_negative_tolerance_percent, nominal_voltage, required_BIL, nominal_current, harmonic_current_amplitudes, pollution_class, base_frequency, warehouse_database, manufacturing_constraints, max_width, max_height, max_mass, max_n_cylinders):
    filepath = os.path.join(output_file_directory, "mockup_output.pdf")
    canvas = Canvas(filepath)
    canvas.drawString(72, 72, "output_file_directory=" + str(output_file_directory))
    canvas.drawString(72, 1.5*72, "reactor_purpose=" + str(reactor_purpose))
    canvas.drawString(72, 2*72, "required_inductance=" + str(required_inductance))
    canvas.drawString(72, 2.5*72, "nominal_voltage=" + str(nominal_voltage))
    canvas.drawString(72, 3*72, "required_BIL=" + str(required_BIL))
    canvas.drawString(72, 3.5*72, "nominal_current=" + str(nominal_current))
    canvas.drawString(72, 4*72, "pollution_class=" + str(pollution_class))
    canvas.drawString(72, 4.5*72, "base_frequency=" + str(base_frequency))
    canvas.save()
    return filepath

def generate_multi_cyl_reactors(output_file_directory, phi_df, reactor_purpose, required_inductance, inductance_positive_tolerance_percent, inductance_negative_tolerance_percent, nominal_voltage, required_BIL, nominal_current, harmonic_current_amplitudes, pollution_class, base_frequency, warehouse_database, manufacturing_constraints, max_width, max_height, max_mass, max_n_cylinders):
    output_pdf_filepath = write_pdf(output_file_directory, reactor_purpose, required_inductance, inductance_positive_tolerance_percent, inductance_negative_tolerance_percent, nominal_voltage, required_BIL, nominal_current, harmonic_current_amplitudes, pollution_class, base_frequency, warehouse_database, manufacturing_constraints, max_width, max_height, max_mass, max_n_cylinders)
    output_pdf_purpose = "mockupOutputPdf"
    output_pdf_type = "application/pdf"
    
    # Calculate placeholder values based on input parameters
    inductance_mH = required_inductance  # Assuming required_inductance is already in mH
    inductiveReactanceAtBaseFrequency_ohm = 2 * np.pi * base_frequency * (inductance_mH / 1000)  # Convert mH to H
    numberOfCylinders = min(max_n_cylinders, 3)  # Use constraint or default to 3
    totalHeight_m = min(max_height, 2.5)  # Use constraint or default to 2.5m
    totalWidth_m = min(max_width, 1.8)  # Use constraint or default to 1.8m
    totalMass_kg = min(max_mass, 500.0)  # Use constraint or default to 500kg
    materialCost = 15000.0  # Placeholder material cost
    totalLifetimeCost = 45000.0  # Placeholder total lifetime cost
    
    output = {
        "inductance_mH": inductance_mH,
        "inductiveReactanceAtBaseFrequency_ohm": inductiveReactanceAtBaseFrequency_ohm,
        "numberOfCylinders": numberOfCylinders,
        "totalHeight_m": totalHeight_m,
        "totalWidth_m": totalWidth_m,
        "totalMass_kg": totalMass_kg,
        "materialCost": materialCost,
        "totalLifetimeCost": totalLifetimeCost
    }
    metadata = {"service": "mock-reactor-designer", "version": "1.0.0"}
    output_json_str = json.dumps(obj={"output": output, "files": [{"filepath": output_pdf_filepath, "filetype": output_pdf_type, "purpose": output_pdf_purpose}], "metadata": metadata}, indent=4)
    return output_json_str