# 1. The Configuration (O(1) Lookups)

thermal_thresholds = {
    "Grace_CPU": 85,
    "Blackwell_GPU_1": 90,
    "Blackwell_GPU_2": 90,
    "Network_NIC": 70
}

# 2. The Incoming Data Stream (O(N) Processing)
incoming_telemetry = [
    "Grace_CPU: 65C",
    "Blackwell_GPU_1: 82C",
    "Blackwell_GPU_2: 88C",
    "Grace_CPU: 86C",        # <- ALARM: CPU is over 85!
    "Network_NIC: 68C",
    "Blackwell_GPU_1: 91C",  # <- ALARM: GPU_1 is over 90!
    "Blackwell_GPU_2: 89C"
]

# 3.  Engine Goes Here

for line in incoming_telemetry:
    parts = line.strip().split(":")
    component = parts[0].strip()
    try:
        temp = int(parts[1].strip()[:-1:])
    except ValueError:
        print(f"WARNING: Malformed telemetry dropped for {component}.")
        continue

    try:
        if temp>thermal_thresholds[component]:
            print(f"ALERT on {component}! {temp} C is over threshold, {thermal_thresholds[component]} C..")

    except KeyError:
        print("Component not present in dictionary!")
        continue



