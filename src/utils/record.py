import os
import yaml

class Record:
    def __init__(self, config_path="config.yaml"):
        self.config_path = config_path
        self.config = self.load_config()
        self.record_everything = self.config.get("default", {}).get("record_everything", False)
        self.make_record_file = self.config.get("default", {}).get("make_record_file", False)
        if self.make_record_file:
            self.create_record_file()

    def load_config(self):
        try:
            with open(self.config_path, "r") as file:
                return yaml.safe_load(file)
        except Exception as e:
            print(f"Error loading config: {e}")
            return {}

    def create_record_file(self):
        try:
            with open("record.txt", "w") as file:
                file.write("Record File\n")
                file.write("===========\n\n")
        except Exception as e:
            print(f"Error creating record file: {e}")
            
    def record(self, data):
        if self.record_everything:
            try:
                with open("record.txt", "a") as file:
                    file.write(f"{data}\n")
            except Exception as e:
                print(f"Error recording data: {e}")
        else: 
            print(f"Recording is disabled. Data not recorded: {data}")
            
    def wipe(self):
        if self.record_everything:
            try:
                with open("record.txt", "r+") as file:
                    file.seek(0)
                    file.truncate(0)
            except Exception as e:
                print(f"Error wiping record file: {e}")
                