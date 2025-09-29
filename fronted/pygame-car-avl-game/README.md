# pygame-car-avl-game

## Overview
This project is a 2D video game featuring a car that moves automatically on a configurable linear road. The game incorporates dynamic obstacles managed by an AVL Tree, providing an engaging gameplay experience.

## Features
- Automatic car movement along a linear road.
- Dynamic obstacle management using an AVL Tree.
- Graphical representation of the AVL Tree.
- Configurable game settings through a JSON configuration file.

## Project Structure
```
pygame-car-avl-game
├── src
│   ├── main.py                # Entry point of the game
│   ├── game
│   │   ├── __init__.py        # Initializes the game module
│   │   ├── car.py             # Manages car properties and movement
│   │   ├── road.py            # Manages road properties and rendering
│   │   ├── obstacle.py        # Represents obstacles on the road
│   │   ├── avl_tree.py        # Implements AVL Tree for obstacle management
│   │   ├── avl_visualizer.py  # Visualizes the AVL Tree structure
│   │   └── config.py          # Loads game configuration settings
│   └── assets
│       └── fonts
│           └── README.md      # Information about fonts used in the game
├── requirements.txt            # Lists project dependencies
└── README.md                   # Project documentation
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd pygame-car-avl-game
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the game:
   ```
   python src/main.py
   ```

## Game Mechanics
- The car moves automatically along the road.
- Obstacles are dynamically managed and displayed using an AVL Tree.
- Players can interact with the game through keyboard inputs.

## Future Enhancements
- Add more obstacle types and behaviors.
- Implement power-ups and collectibles.
- Enhance graphics and animations.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.