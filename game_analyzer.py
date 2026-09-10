from dataclasses import dataclass


TARGET_FPS = 60
FPS_WEIGHT = 0.5
WIN_RATE_WEIGHT = 0.5


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


def find_best_session(sessions):
    return max(sessions, key=calculate_win_rate)


def find_worst_session(sessions):
    return min(sessions, key=calculate_win_rate)


def calculate_overall_win_rate(sessions):
    total_wins = sum(session.wins for session in sessions)
    total_games = sum(session.wins + session.losses for session in sessions)

    if total_games > 0:
        return (total_wins / total_games) * 100
    return 0


def calculate_overall_score(sessions):
    average_fps = sum(session.fps for session in sessions) / len(sessions)
    fps_score = min((average_fps / TARGET_FPS) * 100, 100)
    win_rate_score = calculate_overall_win_rate(sessions)
    score = (fps_score * FPS_WEIGHT) + (win_rate_score * WIN_RATE_WEIGHT)
    return max(0, min(score, 100))


def get_performance_rating(score):
    if score >= 90:
        return "Excellent"
    if score >= 75:
        return "Good"
    if score >= 50:
        return "Average"
    return "Needs Improvement"


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

    if session.fps >= TARGET_FPS:
        print("Performance: Good")
    else:
        print("Performance: Needs Improvement")


def print_overall_report(sessions):
    best_session = find_best_session(sessions)
    worst_session = find_worst_session(sessions)
    average_fps = sum(session.fps for session in sessions) / len(sessions)
    overall_win_rate = calculate_overall_win_rate(sessions)
    overall_score = calculate_overall_score(sessions)

    print("\nOverall Performance")
    print("=========================")
    print("Sessions Analyzed:", len(sessions))
    print("Average FPS:", round(average_fps, 2))
    print("Overall Win Rate:", round(overall_win_rate, 2), "%")
    print("Overall Performance Score:", round(overall_score, 2), "/ 100")
    print("Overall Rating:", get_performance_rating(overall_score))

    print("\nBest Session")
    print("-------------------------")
    print("Player:", best_session.player)
    print("Game:", best_session.game)
    print("Win Rate:", round(calculate_win_rate(best_session), 2), "%")

    print("\nWorst Session")
    print("-------------------------")
    print("Player:", worst_session.player)
    print("Game:", worst_session.game)
    print("Win Rate:", round(calculate_win_rate(worst_session), 2), "%")


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

    print_overall_report(sessions)


if __name__ == "__main__":
    main()