# calculation-of-short-transmission-line
import cmath
import math

# Short Transmission Line Calculations

# Inputs
Vr = float(input("Enter receiving-end line voltage (kV): "))
Ir = float(input("Enter receiving-end current (A): "))
pf = float(input("Enter receiving-end power factor (0 to 1): "))
length = float(input("Enter line length (km): "))

R_per_km = float(input("Enter resistance per km per phase (ohm/km): "))
X_per_km = float(input("Enter reactance per km per phase (ohm/km): "))

# Convert line voltage to phase voltage
Vr_phase = (Vr * 1000) / math.sqrt(3)

# Receiving-end power factor angle
phi = math.acos(pf)

# Assume lagging power factor
Ir_complex = Ir * cmath.exp(-1j * phi)

# Total series impedance per phase
Z = (R_per_km + 1j * X_per_km) * length

# Sending-end phase voltage
Vs_phase = Vr_phase + Ir_complex * Z

# Sending-end line voltage
Vs = abs(Vs_phase) * math.sqrt(3)

# Sending-end current
Is = abs(Ir_complex)

# Sending-end apparent power
S_sending = math.sqrt(3) * Vs * Is

# Sending-end real power
P_sending = 3 * (Vs_phase * Ir_complex.conjugate()).real

# Sending-end power factor
pf_sending = P_sending / S_sending

# Receiving-end power
P_receiving = math.sqrt(3) * (Vr * 1000) * Ir * pf

# Voltage regulation
voltage_regulation = ((Vs - Vr * 1000) / (Vr * 1000)) * 100

# Line losses
losses = 3 * Ir**2 * R_per_km * length

# Display results
print("\n----- SHORT TRANSMISSION LINE RESULTS -----")

print(f"Sending-end voltage       : {Vs / 1000:.3f} kV")
print(f"Sending-end current       : {Is:.3f} A")
print(f"Sending-end power         : {P_sending / 1000:.3f} kW")
print(f"Sending-end power factor  : {pf_sending:.4f}")
print(f"Receiving-end power       : {P_receiving / 1000:.3f} kW")
print(f"Line losses               : {losses / 1000:.3f} kW")
print(f"Voltage regulation        : {voltage_regulation:.3f} %")
