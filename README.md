# Number Sense Game

This project is a simple game designed to test and experiment with human *number sense*—the ability to quickly estimate the number of objects in a visual field. It uses the Python `pygame` library for graphical rendering and interaction.

## Features
- Randomly generates a number of circles (1 to 9) with random sizes and positions.
- Briefly displays the circles, challenging the player to estimate the count.
- Records player responses, reaction times, and provides feedback based on accuracy.
- Tracks the best reaction times for each count.
- Includes a pause function for flexible gameplay.

## How to Play
1. Run the script using Python with `pygame` installed.
2. The game window will open, and a set of circles will flash briefly on the screen.
3. Use keys `1` to `9` to input your estimate of the number of circles.
4. The game will provide feedback:
   - **Purple**: New best time for this count.
   - **Green**: Close to the best time.
   - **Goldenrod**: Correct, but slower.
   - **Red**: Incorrect guess.
5. Press the `SPACE` key to pause or resume the game.

## System Requirements
- Python 3.x
- `pygame` library

To install `pygame`, run:
```bash
pip install pygame
```

## Code Structure
### Variables
- **Game State**:
  - `is_Start`: Indicates if the game has started.
  - `pauseing`: Tracks the pause state.
- **Timing**:
  - `interval_time`: Tracks game timer.
  - `dt`: Delta time for frame-independent timing.
- **Circle Properties**:
  - `circs`: List of circle objects with `x` and `y` coordinates.
  - `circ_size`: Size of the circles.
- **Player Input**:
  - `answer`: Stores the player's input.

### Game Loop
1. **Event Handling**: Detects quit and keypress events.
2. **Game Logic**:
   - Generates random circles.
   - Displays circles briefly.
   - Records and evaluates player responses.
   - Provides visual feedback.
3. **Display Updates**: Renders text and shapes on the screen.
4. **Timing**: Manages frame-independent updates and reaction time tracking.

## Potential Enhancements
- Expand the circle count range (e.g., 10–20).
- Introduce more complex layouts or visual distractions.
- Analyze player performance across different difficulty levels.
- Add a results summary after each session.

## Credits
This game was developed as an experimental tool to explore human cognition and number sense. Contributions and suggestions for improvement are welcome!

## License
This project is open-source and licensed under the MIT License.
