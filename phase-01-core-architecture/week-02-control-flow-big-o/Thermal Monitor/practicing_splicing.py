raw_pcie_speed = "Gen5 x16"
parts = raw_pcie_speed.split()
lane_count = int(parts[1].strip()[1::])
print(lane_count*2)

raw_fan_metric = "   SYS_FAN_01: 88%   "
raw_fan_metric = raw_fan_metric.strip()
parts = raw_fan_metric.split(":")
print(parts[1].strip()[:-1:])

raw_optical_power = "-3.45 dB"
optical_power = float(raw_optical_power.strip(" dB"))
print(optical_power)

pdu_stream = ["PDU_01: 120V", "PDU_02: ERROR_TIMEOUT", "PDU_03: 118V"]
for line in pdu_stream:
    parts = line.strip(" ").split(":")
    if "ERROR" in parts[1].upper():
        print("Skipping corrupt node log... ")
        continue
    else:
        voltage = parts[1].strip("V").strip()
        print(int(voltage))



