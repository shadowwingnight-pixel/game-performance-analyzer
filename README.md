# Game Performance Analyzer

A beginner-friendly command-line tool for recording and reviewing multiple game sessions. The analyzer reports session-level performance and calculates an overall performance score using average FPS and win rate.

## Key Features

- Records multiple game sessions in one run.
- Stores player, game, FPS, play time, wins, and losses for each session.
- Validates numeric input and rejects negative values.
- Calculates each session's win rate.
- Labels each session's FPS performance as `Good` or `Needs Improvement`.
- Identifies the best and worst sessions by win rate.
- Calculates an overall win rate and performance score from 0 to 100.
- Assigns an overall rating: `Excellent`, `Good`, `Average`, or `Needs Improvement`.
- Uses only Python standard library features.

## How It Works

1. Start the program from a terminal.
2. Enter the details for a game session:
   - Player name
   - Game name
   - Average FPS
   - Play time in hours
   - Number of wins
   - Number of losses
3. Choose whether to add another session.
4. After data entry is complete, the program prints:
   - A report for every session
   - Overall statistics
   - The best session by win rate
   - The worst session by win rate

A session with no recorded games has a win rate of `0%`.

## Performance Score Methodology

The overall score combines FPS performance and overall win rate with equal weighting.

### FPS score

The average FPS across all sessions is normalized against the target of 60 FPS:

```text
FPS score = min((average FPS / 60) * 100, 100)
```

An average of 60 FPS or higher contributes 100 points. The score is capped at 100.

### Overall win rate

The overall win rate uses all wins and losses across all sessions:

```text
Overall win rate = (total wins / (total wins + total losses)) * 100
```

When there are no recorded games, the overall win rate is `0%`.

### Final score

```text
Overall score = (FPS score * 0.5) + (Overall win rate * 0.5)
```

The final score is clamped to the range `0` to `100`.

### Rating thresholds

| Score | Rating |
| --- | --- |
| 90–100 | Excellent |
| 75–89.99 | Good |
| 50–74.99 | Average |
| 0–49.99 | Needs Improvement |

## Technologies Used

- Python 3
- `dataclasses` from the Python standard library
- Command-line input and output
- No external packages or dependencies

## Installation and Running

### Requirements

Python 3.7 or newer is recommended because the project uses the standard-library `dataclasses` module.

### Run the analyzer

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run:

```bash
python game_analyzer.py
```

On some systems, use:

```bash
python3 game_analyzer.py
```

## Example Usage

The following example enters two sessions:

```text
Enter your player name: Alice
Enter the game name: Game One
Enter average FPS: 60
Enter play time (hours): 2.5
Enter number of wins: 3
Enter number of losses: 1
Add another session? (y/n): y

Enter your player name: Bob
Enter the game name: Game Two
Enter average FPS: 45
Enter play time (hours): 1
Enter number of wins: 0
Enter number of losses: 2
Add another session? (y/n): n
```

## Example Output

```text
Session Reports
=========================

Performance Report
-------------------------
Player: Alice
Game: Game One
Average FPS: 60.0
Play Time: 2.5 hours
Wins: 3
Losses: 1
Win Rate: 75.0 %
Performance: Good

Performance Report
-------------------------
Player: Bob
Game: Game Two
Average FPS: 45.0
Play Time: 1.0 hours
Wins: 0
Losses: 2
Win Rate: 0.0 %
Performance: Needs Improvement

Overall Performance
=========================
Sessions Analyzed: 2
Average FPS: 52.5
Overall Win Rate: 50.0 %
Overall Performance Score: 68.75 / 100
Overall Rating: Average

Best Session
-------------------------
Player: Alice
Game: Game One
Win Rate: 75.0 %

Worst Session
-------------------------
Player: Bob
Game: Game Two
Win Rate: 0.0 %
```

## Project Structure

```text
.
├── game_analyzer.py   # Main command-line analyzer
├── README.md          # Project documentation
└── .gitignore         # Ignores Python cache files
```

## Future Improvements

- Save sessions to a file so they can be reviewed across program runs.
- Add support for loading previously saved sessions.
- Provide summaries grouped by game or player.
- Add automated tests for calculations and input validation.
- Offer command-line arguments in addition to interactive prompts.
- Track additional metrics such as frame-time consistency or minimum FPS.
