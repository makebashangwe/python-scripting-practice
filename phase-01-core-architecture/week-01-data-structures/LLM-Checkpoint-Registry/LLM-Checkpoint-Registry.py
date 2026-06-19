import random

#The Requirements:
#Store: Register a new model checkpoint.
# It requires a checkpoint_id (e.g., "llama-v1"), a parameter_size_billion (int, e.g., 70), and a default status of "stored".

class LLM_Checkpoint:
    def __init__(self,checkpoint_id:str,parameter_size_billion:int,status="stored"):
        self.checkpoint_id = checkpoint_id
        self.parameter_size_billion = parameter_size_billion
        self.status = status #lowkey redundant if we track it in buckets tbh.
    def get_checkpoint_id(self):
        return self.checkpoint_id
    def get_parameter_size(self):
        return self.parameter_size_billion
    def get_status(self):
        return self.status

class LLM_Checkpoint_Registry:
    def __init__(self):
        self._active_checkpoints = {}
        self._archived_checkpoints = {}

    def verify_checkpoint(self,checkpoint_id):
        if checkpoint_id in self._active_checkpoints or checkpoint_id in self._archived_checkpoints:
            return True
        else:
            return False

    def verify_checkpoint_bucket(self,checkpoint_id):
        if checkpoint_id in self._active_checkpoints:
            return "active"
        if checkpoint_id in self._archived_checkpoints:
            return "archived"
        else:
            return None

    def deploy_checkpoint(self,checkpoint_id,parameter_size_billion):
        if self.verify_checkpoint(checkpoint_id):
            return False
        else:
            self._active_checkpoints[checkpoint_id] = LLM_Checkpoint(checkpoint_id,parameter_size_billion,"deployed")
            return True
    #Archive: Change a checkpoint's status to "archived" (moves it to cold storage like AWS S3 Glacier).
    def archive_checkpoint(self,checkpoint_id):
        if self.verify_checkpoint(checkpoint_id) and self.verify_checkpoint_bucket(checkpoint_id) != "archived":
            self._active_checkpoints[checkpoint_id].status = "archived"
            self._archived_checkpoints[checkpoint_id] = self._active_checkpoints[checkpoint_id]
            del self._active_checkpoints[checkpoint_id]
            return True
        else:
            return False
    #Delete: Completely remove the checkpoint from the registry ONLY IF it is currently "archived".
    # You cannot delete a "stored" or "deployed" model.
    def delete_checkpoint(self,checkpoint_id):
        if self.verify_checkpoint(checkpoint_id) and self.verify_checkpoint_bucket(checkpoint_id) == "archived":
            del self._archived_checkpoints[checkpoint_id]
            return True
        return False

    def view_archived_checkpoints(self):
        return self._archived_checkpoints

    def view_deployed_checkpoints(self):
        deployed_checkpoints = {}
        for checkpoint in self._active_checkpoints:
            if self._active_checkpoints[checkpoint].get_status() == "deployed":
                deployed_checkpoints[checkpoint] = self._active_checkpoints[checkpoint]
        return deployed_checkpoints

    def view_all_checkpoints(self):
        return self._active_checkpoints | self._archived_checkpoints

def show_choices():
    return (f"\n1. Create Checkpoint\n"
            f"2. Archive Checkpoint\n"
            f"3. Delete Checkpoint\n"
            f"4. See Deployed Checkpoints\n"
            f"5. See Archived Checkpoints\n"
            f"6. See All Checkpoints\n"
            f"7. Quit\n")
def main():
    registry = LLM_Checkpoint_Registry()
    while True:
        print(show_choices())
        while True:
            try:
                choice = int(input("Please enter a choice: "))
                if choice in range(1,8):
                    break
                else:
                    print("Please enter a valid choice")
            except ValueError:
                print("Please enter a integer in the range 1-7.")

        match choice:
            case 1:
                checkpoint_id = random.randint(10000,99999)
                while True:
                    try:
                        parameter_size_billion = float(input("Please enter the parameter size:"))
                        if parameter_size_billion > 0:
                            break
                        else:
                            print("Please enter a value greater than 0.")
                    except ValueError:
                        print("Please enter a valid float/ value.")
                success = registry.deploy_checkpoint(checkpoint_id,parameter_size_billion)
                if success:
                    print("Checkpoint created successfully!")
                else:
                    print("Checkpoint creation failed. Please try again.")

            case 2:
                deployed = registry.view_deployed_checkpoints()
                for checkpoint in deployed:
                    print(f"Checkpoint ID : {checkpoint} | Status: {deployed[checkpoint].get_status()}")
                while True:
                    try:
                        checkpoint_id = int(input("Please enter the checkpoint ID you'd like to archive: "))
                        break
                    except ValueError:
                        print("Please enter a valid checkpoint ID.")

                confirm = input(f"Are you sure you'd like to archive Checkpoint {checkpoint_id}? (Y/N) ").lower()
                if confirm == "y" or confirm == "yes":
                    registry.archive_checkpoint(checkpoint_id)
                else:
                    print("Aborted!")
                    continue
            case 3:
                archived = registry.view_archived_checkpoints()
                for checkpoint in archived:
                    print(f"Checkpoint ID : {checkpoint} | Status: {archived[checkpoint].get_status()}")
                while True:
                    try:
                        checkpoint_id = int(input("Please enter the checkpoint ID you'd like to delete: "))
                        break
                    except ValueError:
                        print("Please enter a valid checkpoint ID.")

                confirm = input(f"Are you sure you'd like to delete Checkpoint {checkpoint_id}? (Y/N) ").lower()
                if confirm == "y" or confirm == "yes":
                    registry.delete_checkpoint(checkpoint_id)
                else:
                    print("Aborted!")
                    continue
            case 4:
                deployed = registry.view_deployed_checkpoints()
                for checkpoint in deployed:
                    print(f"Checkpoint ID : {checkpoint} | Status: {deployed[checkpoint].get_status()}")
            case 5:
                archived = registry.view_archived_checkpoints()
                for checkpoint in archived:
                    print(f"Checkpoint ID : {checkpoint} | Status: {archived[checkpoint].get_status()}")
            case 6:
                all_checkpoints = registry.view_all_checkpoints()
                for checkpoint in all_checkpoints:
                    print(f"Checkpoint ID : {checkpoint} | Status: {all_checkpoints[checkpoint].get_status()}")
            case 7:
                quit()

main()