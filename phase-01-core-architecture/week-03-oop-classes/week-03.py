# 1. The Blueprint
class ComputeNode:
    # The __init__ method is the "constructor".
    # It runs automatically the exact moment you rack (create) a new server.
    def __init__(self, hostname, ip_address):
        self.hostname = hostname
        self.ip_address = ip_address
        self.status = "Offline"     # All nodes start offline
        self.temperature = 25       # Default room temp in Celsius

    # This is a Method (an Action). It belongs to the node.
    def boot_up(self):
        self.status = "Online"
        print(f"[{self.hostname}] Boot sequence complete. Status: {self.status}")

    def shutdown(self):
        self.status = "Offline"
        print(f"{self.hostname} is shutdown successfully.\nStatus: {self.status}")

# ---------------------------------------------------------
# 2. The Implementation (The Data Center Floor)

# Here we rack two physical instances of our blueprint:
node_a = ComputeNode(hostname="Worker-01", ip_address="10.0.1.5")
node_b = ComputeNode(hostname="Worker-02", ip_address="10.0.1.6")

# Let's boot one up:
node_a.boot_up()

# Notice how their states are independent!
print(f"Node A is {node_a.status}") # Will print Online
print(f"Node B is {node_b.status}") # Will print Offline

node_a.shutdown()
