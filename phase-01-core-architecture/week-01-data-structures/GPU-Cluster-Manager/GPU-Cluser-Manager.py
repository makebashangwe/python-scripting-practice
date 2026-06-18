#The Model: GPUNode
class GPUNode:
    def __init__(self, node_id:str, vram_gb:int, status="idle"):
        self.node_id = node_id
        self.vram_gb = vram_gb
        self.status = status
    def get_node_id(self):
        return self.node_id
    def get_vram_gb(self):
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
    def get_idle_nodes(self):
        idle_nodes = []
        for node in self._available_gpus:
            if self._available_gpus[node].get_status != "draining":
                idle_nodes.append(self._available_gpus[node].node_id)


def main():
    pass