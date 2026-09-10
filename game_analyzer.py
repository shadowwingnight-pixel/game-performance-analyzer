from dataclasses import dataclass


@dataclass
class GameSession:
    player: str
    game: str
    fps: float
    play_time: float
    wins: int
    losses: int


def get_nonnegative_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            print("Please enter a nonnegative number.")
        except ValueError:
            print("Please enter a valid number.")


def get_nonnegative_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            print("Please enter a nonnegative whole number.")
        except ValueError:
            print("Please enter a valid whole number.")


def collect_session():
    player = input("Enter your player name: ")
    game = input("Enter the game name: ")
    fps = get_nonnegative_float("Enter average FPS: ")
    play_time = get_nonnegative_float("Enter play time (hours): ")
    wins = get_nonnegative_int("Enter number of wins: ")
    losses = get_nonnegative_int("Enter number of losses: ")

    return GameSession(player, game, fps, play_time, wins, losses)


def calculate_win_rate(session):
    total_games = session.wins + session.losses

    if total_games > 0:
        return (session.wins / total_games) * 100
    return 0


def print_session_report(session):
    win_rate = calculate_win_rate(session)

    print("\nPerformance Report")
    print("-------------------------")
    print("Player:", session.player)
    print("Game:", session.game)
    print("Average FPS:", session.fps)
    print("Play Time:", session.play_time, "hours")
    print("Wins:", session.wins)
    print("Losses:", session.losses)
    print("Win Rate:", round(win_rate, 2), "%")

    if session.fps >= 60:
        print("Performance: Good")
    else:
        print("Performance: Needs Improvement")


def main():
    print("Game Performance Analyzer")
    print("-------------------------")

    sessions = []

    while True:
        print("\nEnter game session details")
        sessions.append(collect_session())

        add_another = input("Add another session? (y/n): ").strip().lower()
        if add_another != "y":
            break

    print("\nSession Reports")
    print("=========================")
    for session in sessions:
        print_session_report(session)


if __name__ == "__main__":
    main()