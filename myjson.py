import os
import json
import matplotlib.pyplot as plt


class JSONDataModule:
    def __init__(self):
        # Define directory and file paths
        self.base_dir = 'data'
        self.static_dir = 'static'
        
        # Electricity
        self.electricity_dir = os.path.join(self.base_dir, 'electricity')
        self.electricity_json = os.path.join(self.electricity_dir, 'electricity_data.json')
        self.electricity_graph_dir = os.path.join(self.static_dir, 'electricity')
        self.electricity_graph = os.path.join(self.electricity_graph_dir, 'electricity_graph.png')

        # Water
        self.water_dir = os.path.join(self.base_dir, 'water')
        self.water_json = os.path.join(self.water_dir, 'water_data.json')
        self.water_graph_dir = os.path.join(self.static_dir, 'water')
        self.water_graph = os.path.join(self.water_graph_dir, 'water_graph.png')

    def ensure_directories(self):
        os.makedirs(self.electricity_dir, exist_ok=True)
        os.makedirs(self.water_dir, exist_ok=True)
        os.makedirs(self.electricity_graph_dir, exist_ok=True)
        os.makedirs(self.water_graph_dir, exist_ok=True)

    # ==================== ELECTRICITY DATA ====================
    def get_electricity_data(self):
        return {
            "jitwarr_purr_village": {
                "electricity_data": [
                    {"month": "January", "consumption_kwh": 1250, "bill_rupees": 9500, "power_cuts": 8},
                    {"month": "February", "consumption_kwh": 1180, "bill_rupees": 8900, "power_cuts": 6},
                    {"month": "March", "consumption_kwh": 1350, "bill_rupees": 10200, "power_cuts": 10},
                    {"month": "April", "consumption_kwh": 1420, "bill_rupees": 10700, "power_cuts": 12},
                    {"month": "May", "consumption_kwh": 1580, "bill_rupees": 11900, "power_cuts": 15},
                    {"month": "June", "consumption_kwh": 1620, "bill_rupees": 12200, "power_cuts": 18},
                    {"month": "July", "consumption_kwh": 1550, "bill_rupees": 11700, "power_cuts": 14},
                    {"month": "August", "consumption_kwh": 1480, "bill_rupees": 11200, "power_cuts": 11},
                    {"month": "September", "consumption_kwh": 1320, "bill_rupees": 10000, "power_cuts": 9},
                    {"month": "October", "consumption_kwh": 1280, "bill_rupees": 9700, "power_cuts": 7},
                    {"month": "November", "consumption_kwh": 1220, "bill_rupees": 9200, "power_cuts": 5},
                    {"month": "December", "consumption_kwh": 1300, "bill_rupees": 9800, "power_cuts": 4}
                ],
                "summary": {
                    "total_consumption_kwh": 15950,
                    "total_bill_rupees": 120200,
                    "average_power_cuts_per_month": 9.5
                }
            }
        }

    # ==================== WATER DATA ====================
    def get_water_data(self):
        return {
            "jitwarr_purr_village": {
                "water_supply_data": [
                    {"month": "January", "consumption_kl": 420, "bill_rupees": 2800, "supply_days": 28, "shortage_days": 3},
                    {"month": "February", "consumption_kl": 395, "bill_rupees": 2600, "supply_days": 26, "shortage_days": 2},
                    {"month": "March", "consumption_kl": 450, "bill_rupees": 3000, "supply_days": 29, "shortage_days": 2},
                    {"month": "April", "consumption_kl": 480, "bill_rupees": 3200, "supply_days": 27, "shortage_days": 3},
                    {"month": "May", "consumption_kl": 520, "bill_rupees": 3500, "supply_days": 25, "shortage_days": 6},
                    {"month": "June", "consumption_kl": 540, "bill_rupees": 3600, "supply_days": 23, "shortage_days": 7},
                    {"month": "July", "consumption_kl": 510, "bill_rupees": 3400, "supply_days": 26, "shortage_days": 5},
                    {"month": "August", "consumption_kl": 490, "bill_rupees": 3300, "supply_days": 27, "shortage_days": 4},
                    {"month": "September", "consumption_kl": 440, "bill_rupees": 2900, "supply_days": 28, "shortage_days": 2},
                    {"month": "October", "consumption_kl": 425, "bill_rupees": 2800, "supply_days": 29, "shortage_days": 2},
                    {"month": "November", "consumption_kl": 410, "bill_rupees": 2700, "supply_days": 28, "shortage_days": 2},
                    {"month": "December", "consumption_kl": 430, "bill_rupees": 2850, "supply_days": 29, "shortage_days": 2}
                ],
                "summary": {
                    "total_consumption_kl": 5510,
                    "total_bill_rupees": 36610,
                    "average_supply_days_per_month": 27.08,
                    "total_shortage_days": 40
                }
            }
        }

    # ==================== SAVE DATA ====================
    def save_electricity_data(self):
        self.ensure_directories()
        data = self.get_electricity_data()
        with open(self.electricity_json, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Saved electricity data to {self.electricity_json}")

    def save_water_data(self):
        self.ensure_directories()
        data = self.get_water_data()
        with open(self.water_json, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Saved water data to {self.water_json}")

    def save_all_data(self):
        self.save_electricity_data()
        self.save_water_data()

    # ==================== LOAD DATA ====================
    def load_electricity_data(self):
        with open(self.electricity_json, 'r') as f:
            return json.load(f)

    def load_water_data(self):
        with open(self.water_json, 'r') as f:
            return json.load(f)

    # ==================== PLOT ELECTRICITY ====================
    def plot_electricity(self):
        data = self.load_electricity_data()
        entries = data["jitwarr_purr_village"]["electricity_data"]

        months = [e["month"] for e in entries]
        consumption = [e["consumption_kwh"] for e in entries]
        power_cuts = [e["power_cuts"] for e in entries]

        plt.figure(figsize=(12, 6))
        plt.bar(months, consumption, color='skyblue', alpha=0.7, label="Consumption (kWh)")
        plt.plot(months, power_cuts, color='red', marker='o', linewidth=2, label="Power Cuts")
        plt.xlabel("Month")
        plt.ylabel("Value")
        plt.title("Electricity Consumption and Power Cuts per Month")
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(self.electricity_graph)
        plt.close()
        print(f"Electricity graph saved to {self.electricity_graph}")

    # ==================== PLOT WATER ====================
    def plot_water(self):
        data = self.load_water_data()
        entries = data["jitwarr_purr_village"]["water_supply_data"]

        months = [e["month"] for e in entries]
        consumption = [e["consumption_kl"] for e in entries]
        shortage_days = [e["shortage_days"] for e in entries]

        plt.figure(figsize=(12, 6))
        plt.bar(months, consumption, color='#1e90ff', alpha=0.7, label="Consumption (kL)")
        plt.plot(months, shortage_days, color='orange', marker='o', linewidth=2, label="Shortage Days")
        plt.xlabel("Month")
        plt.ylabel("Value")
        plt.title("Water Consumption and Shortage Days per Month")
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(self.water_graph)
        plt.close()
        print(f"Water graph saved to {self.water_graph}")

    # ==================== PLOT ALL ====================
    def plot_all(self):
        self.plot_electricity()
        self.plot_water()