import random


class pdu_manager:
    def __init__(self):
        self._pdu_list = {}

    def verify_asset_id(self, asset_id):
        if asset_id in self._pdu_list:
            return True
        return False

    def initalize_pdu(self, asset_id, base_power_draw):
        if self.verify_asset_id(asset_id):
            return False

        self._pdu_list[asset_id] = PDU(asset_id, base_power_draw)
        return True

    def initalize_smart_pdu(self, asset_id, base_power_draw, efficency_rating):
        if self.verify_asset_id(asset_id):
            return False

        self._pdu_list[asset_id] = smart_pdu(asset_id, base_power_draw, efficency_rating)
        return True

    def get_all_pdus(self):
        if (len(self._pdu_list.values())) == 0:
            print("No PDUs to show!")
        else:
            print("PDU LIST:")
            for asset_id in self._pdu_list:
                print(f"Asset ID: {asset_id} : Base Power Draw: {self._pdu_list[asset_id].get_base_power_draw()}")

    def aggregated_power(self):
        if (len(self._pdu_list.values())) == 0:
            print("No PDUs to show!")
        else:
            result = 0
            for asset_id in self._pdu_list:
                result += self._pdu_list[asset_id].get_base_power_draw()
            print(f"CURRENT TOTAL POWER DRAW: {result} W")


class PDU:
    def __init__(self, asset_id: str, base_power_draw: int):
        self.asset_id = asset_id
        self.base_power_draw = base_power_draw

    def get_base_power_draw(self):
        return self.base_power_draw


class smart_pdu(PDU):
    def __init__(self, asset_id: str, base_power_draw: int, efficency_rating: float):
        super().__init__(asset_id, base_power_draw)
        self.efficency_rating = efficency_rating

    def get_base_power_draw(self):
        return self.base_power_draw * self.efficency_rating


def get_choices():
    return ("1. Create normal PDU\n2. Create Smart PDU\n3. View All PDUs\n4. Quit\n")


def main():
    manager = pdu_manager()
    while True:
        print(get_choices())
        while True:
            try:
                choice = int(input("Please enter a choice: "))
                if choice in range(1, 5):
                    break
                else:
                    print("Please enter a valid choice!")
            except ValueError:
                print("Please enter a integer option.")

        match choice:
            case 1:
                try:
                    num = int(input("Please enter the number of normal PDUs needed: "))
                    for i in range(num):
                        valid_id = True
                        while valid_id:
                            asset_id = random.randint(1000, 10000)
                            valid_id = manager.verify_asset_id(asset_id)
                        base_power_draw = int(input(f"Please enter the base power draw for PDU {i + 1}: "))
                        success = manager.initalize_pdu(str(asset_id), base_power_draw)
                        if success:
                            print(f"CREATED {asset_id}.")
                        else:
                            print(f"Something went wrong with {asset_id}, please try again.")
                except ValueError:
                    print("Incorrect Value Type. Please try again.")
            case 2:
                try:
                    num = int(input("Please enter the number of smart PDUs needed: "))
                    for i in range(num):
                        valid_id = True
                        while valid_id:
                            asset_id = random.randint(1000, 10000)
                            valid_id = manager.verify_asset_id(asset_id)
                        base_power_draw = int(input(f"Please enter the base power draw for PDU {i + 1}: "))
                        efficency_rating = float(input(f"Please enter the efficency rating for PDU {i + 1}: "))
                        success = manager.initalize_smart_pdu(str(asset_id), base_power_draw, efficency_rating)
                        if success:
                            print(f"CREATED {asset_id}.")
                        else:
                            print(f"Something went wrong with {asset_id}, please try again.")
                except ValueError:
                    print("Incorrect Value Type. Please try again.")
            case 3:
                manager.get_all_pdus()

            case 4:
                manager.aggregated_power()


main()