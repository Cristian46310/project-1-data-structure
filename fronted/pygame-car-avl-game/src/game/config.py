from pathlib import Path
import json

class Config:
    def __init__(self, config_file='config.json'):
        self.config_file = Path(__file__).parent / config_file
        self.total_distance = 0
        self.car_speed = 0
        self.jump_height = 0
        self.refresh_rate = 0
        self.initial_color = (0, 0, 0)
        self.obstacles = []

        self.load_config()

    def load_config(self):
        with open(self.config_file, 'r') as file:
            config_data = json.load(file)
            self.total_distance = config_data.get('total_distance', 1000)
            self.car_speed = config_data.get('car_speed', 5)
            self.jump_height = config_data.get('jump_height', 10)
            self.refresh_rate = config_data.get('refresh_rate', 60)
            self.initial_color = tuple(config_data.get('initial_color', [0, 0, 0]))
            self.obstacles = config_data.get('obstacles', [])

    def get_obstacles(self):
        return self.obstacles