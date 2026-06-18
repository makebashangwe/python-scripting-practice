import random

class GPUNode:
    def __init__(self, node_id:str, vram_gb:int, status="idle"):
        self.node_id = node_id
        self.vram_gb = vram_gb
        self.status = status
    def get_node_id(self):
        return self.node_id
    def get_vram(self):
        return self.vram_gb
    def get_status(self):
        return self.status

class GPUClusterManager:
    def __init__(self):
        self._available_gpus = {}

    def verify_node_id(self,node_id):
        if node_id in self._available_gpus:
            return True
        return False
    def register_node(self,node_id,vram_gb):
        if self.verify_node_id(node_id):
            return False
        else:
            self._available_gpus[node_id] = GPUNode(node_id,vram_gb)
            return True

    def allocate_job(self,node_id):
        if self.verify_node_id(node_id) and self._available_gpus[node_id].get_status() == "idle":
            self._available_gpus[node_id].status = "training"
            return True
        else:
            return False

    def drain_node(self,node_id):
        if self.verify_node_id(node_id) and self._available_gpus[node_id].get_status() !="draining":
            self._available_gpus[node_id].status = "draining"
            return True
        else:
            return False

    def remove_node(self,node_id):
        if self.verify_node_id(node_id) and self._available_gpus[node_id].get_status() == "draining":
            del self._available_gpus[node_id]
            return True
        else:
            return False

    def get_all_nodes(self):
        return self._available_gpus #WHOLE DICTIONARY!

    def get_idle_nodes(self):
        idle_nodes = {}
        for node in self._available_gpus:
            if self._available_gpus[node].get_status != "draining":
                idle_nodes[self._available_gpus[node].get_node_id] = self._available_gpus[node]
        return idle_nodes

def show_choices():
    return (f"\n1. Register a GPU Node\n"
            f"2. Allocate a Training Job\n"
            f"3. Drain a Node\n"
            f"4. Remove a Node\n"
            f"5. View All Nodes\n"
            f"6. Exit\n")

def main():
    print("GPU Cluster Manager (GCM)")
    gpu_manager = GPUClusterManager()

    while True:
        print(show_choices()) #Print the choices

        while True:
            try:
                choice = int(input("Please make a choice: "))
                if choice >0 and choice <=6:
                    break
                else:
                    print("Please enter a valid choice.")
            except ValueError:
                print("Please enter a number.")

        match choice:
            case 1: #works
                GPU_count = int(input("How many GPUs would you like to create? "))
                for i in range(GPU_count):
                    node_id = random.randint(00000, 10000)

                    while True:
                        try:
                            vram_gb = int(input(f"Please enter the amount of RAM for GPU {i+1}: "))
                            if vram_gb >0:
                                break
                            else:
                                print("Please enter a valid non-zero integer.")

                        except ValueError:
                            print("Please enter a valid number.")
                    success = gpu_manager.register_node(node_id,vram_gb)
                    if success:
                        print("GPU created successfully.")
                    else:
                        print("GPU could not be created. Please try again.")
            case 2:
                idle_nodes = gpu_manager.get_idle_nodes()
                if len(idle_nodes) == 0:
                    print("There are no nodes to drain!")

                else:
                    for node in idle_nodes:
                        print(f"Node ID: {idle_nodes[node].get_node_id()} | VRAM: {idle_nodes[node].get_vram()} GB | Status: {idle_nodes[node].get_status()}")

                    node_id = int(input("Please enter the node_ID you'd like to allocate a job to: "))
                    success = gpu_manager.allocate_job(node_id)
                    if success:
                        print("GPU running...")
                    else:
                        print("GPU could not be allocated. Please try again.")

            case 3:
                idle_nodes = gpu_manager.get_idle_nodes()
                if len(idle_nodes) == 0:
                    print("There are no nodes to drain!")

                else:
                    for node in idle_nodes:
                        print(f"Node ID: {idle_nodes[node].get_node_id()} | VRAM: {idle_nodes[node].get_vram()} GB | Status: {idle_nodes[node].get_status()}")
                    node_id = int(input("Please enter the node_ID you'd like to drain: "))
                    success = gpu_manager.drain_node(node_id)
                    if success:
                        print("GPU drained...")
                    else:
                        print("GPU could not be drained. Please try again.")

            case 4:
                idle_nodes = gpu_manager.get_idle_nodes()
                if len(idle_nodes) == 0:
                    print("There are no nodes to delete!")

                else:
                    for node in idle_nodes:
                        print(f"Node ID: {idle_nodes[node].get_node_id()} | VRAM: {idle_nodes[node].get_vram()} GB | Status: {idle_nodes[node].get_status()}")
                    node_id = int(input("Please enter the node_ID you'd like to drain: "))
                    success = gpu_manager.remove_node(node_id)
                    if success:
                        print("GPU drained...")
                    else:
                        print("GPU could not be removed.\n"
                              "Note: GPU's cannot be removed unless they are drained!"
                              "\nPlease try again.")
            case 5:
                all_nodes = gpu_manager.get_all_nodes()
                if len(all_nodes) == 0:
                    print("There are no nodes to show!")

                else:
                    for node in all_nodes:
                        print(f"Node ID: {all_nodes[node].get_node_id()} | VRAM: {all_nodes[node].get_vram()} GB | Status: {all_nodes[node].get_status()}")

            case 6:
                break
    quit()

main()