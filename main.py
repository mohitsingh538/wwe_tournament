import random
import subprocess
import sys
import threading
import time
from typing import List

def ensure_package_installed(package_name):
    try:
        __import__(package_name)

    except ImportError:
        print(f"{package_name} is not installed. Installing now...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

ensure_package_installed("colorama")

from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

wwe_finishing_moves = {
    "Brock Lesnar": "F-5",
    "John Cena": "Attitude Adjustment",
    "Kurt Angle": "Angle Slam",
    "The Undertaker": "Tombstone Piledriver",
    "Triple H": "Pedigree",
    "Shawn Michaels": "Sweet Chin Music",
    "Stone Cold Steve Austin": "Stone Cold Stunner",
    "The Rock": "Rock Bottom",
    "Hulk Hogan": "Leg Drop",
    "Ric Flair": "Figure-Four Leglock",
    "Randy Savage": "Elbow Drop",
    "Batista": "Batista Bomb",
    "Edge": "Spear",
    "Jeff Hardy": "Swanton Bomb",
    "Matt Hardy": "Twist of Fate",
    "Kane": "Chokeslam",
    "Goldberg": "Spear",
    "Chris Jericho": "Codebreaker",
    "Booker T": "Book End",
    "Eddie Guerrero": "Frog Splash",
    "Rey Mysterio": "619",
    "Roman Reigns": "Superman Punch",
    "Seth Rollins": "Curb Stomp",
    "Cody Rhodes": "Cross Rhodes",
    "Drew McIntyre": "Claymore Kick",
    "AJ Styles": "Styles Clash",
    "Finn Bálor": "Coup de Grâce",
    "Kevin Owens": "Pop-up Powerbomb",
    "Sami Zayn": "Helluva Kick",
    "Gunther": "Powerbomb",
    "LA Knight": "BFT (Blunt Force Trauma)",
    "Sheamus": "Brogue Kick",
    "Randy Orton": "RKO",
    "The Miz": "Skull Crushing Finale",
    "Big Show": "Chokeslam",
    "Mark Henry": "World’s Strongest Slam",
    "Christian Cage": "Killswitch",
    "RVD (Rob Van Dam)": "Five-Star Frog Splash",
    "CM Punk": "Go to Sleep",
    "Daniel Bryan (Bryan Danielson)": "Yes Lock",
    "Mick Foley": "Mandible Claw",
    "Ted DiBiase": "Dream Street",
    "JBL (John Bradshaw Layfield)": "Clothesline from Hell",
    "Big E": "Big Ending",
    "Kofi Kingston": "Trouble in Paradise",
    "Xavier Woods": "Honor Roll"
}


class Player:
    def __init__(self, name: str, energy: int, finishing_move: str):
        self.name = name
        self.energy = energy
        self.finishing_move = finishing_move

    def replenish_energy(self):
        bonus_energy = random.randint(10, 50)
        self.energy += bonus_energy
        battery_symbol = "🔋" if self.energy > 0 else "🪫"

        print(f"{Fore.GREEN}🎉 {self.name} replenished with {bonus_energy} energy points! Total Energy: {self.energy} {battery_symbol}")

class Match:
    def __init__(self, all_players: List[Player], match_type: str, event_name: str):
        self.players = all_players
        self.match_type = match_type  # '1v1' or 'triple-threat'

        self.state = {
            "event_name": event_name,
            "winner": None,
            "match_duration": 0,
            "players": self.players
        }

    def generate_victory_message(self, winner, losers):
        if self.match_type == '1v1':
            loser = losers[0]
            messages = [
                f"{winner.name} (⚡ {winner.energy}) obliterates {loser.name} with a killer {winner.finishing_move}!",
                f"DOWN GOES {loser.name}! {winner.name} (⚡ {winner.energy}) finishes it with the {winner.finishing_move}!",
                f"ONE. TWO. THREE! {winner.name} (⚡ {winner.energy}) takes out {loser.name} with the unstoppable {winner.finishing_move}!",
                f"{loser.name} had no chance—{winner.name} (⚡ {winner.energy}) ends it with a brutal {winner.finishing_move}!",
                f"GAME OVER! {winner.name} (⚡ {winner.energy}) floors {loser.name} with the epic {winner.finishing_move}!",
                f"{winner.name} (⚡ {winner.energy}) makes quick work of {loser.name} using the devastating {winner.finishing_move}!",
                f"BOOM! {winner.name} (⚡ {winner.energy}) annihilates {loser.name} with the thunderous {winner.finishing_move}!",
                f"Lights out for {loser.name}! {winner.name} (⚡ {winner.energy}) seals the deal with a legendary {winner.finishing_move}!",
                f"TOTAL DOMINATION! {winner.name} (⚡ {winner.energy}) destroys {loser.name} with the unstoppable {winner.finishing_move}!",
                f"{winner.name} (⚡ {winner.energy}) stands tall, ending {loser.name}'s hopes with the crushing {winner.finishing_move}!"
            ]

        else:
            losers_names = " and ".join([p.name for p in losers])
            messages = [
                f"{winner.name} (⚡ {winner.energy}) crushes {losers_names} with the unstoppable {winner.finishing_move}!",
                f"{winner.name} (⚡ {winner.energy}) reigns supreme, dropping {losers_names} with a brutal {winner.finishing_move}!",
                f"Lights out for {winner.name} (⚡ {winner.energy}) as {winner.name} seals the win with the {winner.finishing_move}!",
                f"{winner.name} (⚡ {winner.energy}) takes the crown, smashing {losers_names} with a legendary {winner.finishing_move}!",
                f"{winner.name} (⚡ {winner.energy}) never stood a chance—{winner.name} ends it with a devastating {winner.finishing_move}!",
                f"Victory for {winner.name} (⚡ {winner.energy}), who flattens {losers_names} with the epic {winner.finishing_move}!",
                f"{winner.name} (⚡ {winner.energy}) leaves no doubt, wrecking {losers_names} with the incredible {winner.finishing_move}!",
                f"Dominance! {winner.name} (⚡ {winner.energy}) takes out {losers_names} with a thunderous {winner.finishing_move}!",
                f"{winner.name} (⚡ {winner.energy}) steals the show, defeating {losers_names} with an iconic {winner.finishing_move}!",
                f"Game over! {winner.name} (⚡ {winner.energy}) buries {losers_names} with the unstoppable {winner.finishing_move}!"
            ]

        return random.choice(messages)

    @staticmethod
    def punch_players(players_list: List[Player]):
        player = random.choice(players_list)
        energy_lost = random.randint(10, 50)
        player.energy -= energy_lost

        print(f"🥊 {player.name} got punched! (-{energy_lost})   |   ⚡ {player.energy}")

    def query_match_state(self):
        print("\n=== MATCH STATE ===")
        print(f"Round: {self.state['event_name']}")
        print("🤼 Players:")

        for player in self.players:
            print(f"  {player.name}: Energy: {player.energy}")
        print(f"⏱️ Match duration: {self.state['match_duration']} seconds")

        if self.state["winner"]:
            print(f"🏅 Winner: {self.state['winner']}")

    def conduct(self):
        start_time = time.time()

        if self.match_type == '1v1':
            print(f"{Fore.YELLOW}\n🔥 SINGLES MATCH: {self.players[0].name} ({self.players[0].energy}) vs {self.players[1].name} ({self.players[1].energy}) 🔥")

        else:
            print(f"{Fore.YELLOW}\n🔥 TRIPLE THREAT MATCH: {self.players[0].name} ({self.players[0].energy}) vs {self.players[1].name} ({self.players[1].energy}) vs {self.players[2].name} ({self.players[2].energy}) 🔥")

        while time.time() - start_time < 30:
            time.sleep(random.uniform(0.5, 1.0))
            self.state["match_duration"] = time.time() - start_time
            min_players = 1 if self.match_type == '1v1' else 2
            punched_players = random.choices(self.players, k=min_players)
            self.punch_players(punched_players)

            if random.choice([True, False]):
                self.query_match_state()

            if random.random() < 0.2:
                break

        winner = max(self.players, key=lambda x: x.energy)
        self.state["winner"] = (winner.name, winner.energy)
        losers = [p for p in self.players if p != winner]
        self.query_match_state()

        victory_message = self.generate_victory_message(winner, losers)
        print(f"\n{Fore.RED}💥 {victory_message}")
        print(f"{Fore.CYAN}⏱️ Match Duration: {self.state["match_duration"]:.4f} seconds\n")

        return winner


class TournamentOrchestrator:

    def __init__(self, players_list: List[Player]):
        self.players = players_list
        self.round_winners = []
        self.final_winner = None
        self.lock = threading.Lock()

    def run_first_round(self):
        print(f"{Fore.MAGENTA}\n=== FIRST ROUND (1v1 Matches) ===")
        matches = []
        match_round = "First Round (1v1 Matches)"
        for i in range(0, len(self.players), 2):
            match_players = [self.players[i], self.players[i + 1]]
            matches.append(Match(match_players, '1v1', match_round))

        threads = [threading.Thread(target=self.conduct_match, args=(match,)) for match in matches]
        [thread.start() for thread in threads]
        return [thread.join() for thread in threads]

    def run_triple_threats(self):
        if len(self.round_winners) < 4:
            return

        print(f"{Fore.MAGENTA}\n=== TRIPLE THREAT ROUND ===")
        match_round = "Triple Threat Round"
        while len(self.round_winners) > 4:
            matches = []
            current_round_players = self.round_winners
            self.round_winners = []
            for i in range(0, len(current_round_players), 3):
                if len(current_round_players) - i >= 3:
                    match_players = current_round_players[i:i + 3]
                    matches.append(Match(match_players, 'triple_threat', match_round))

                else:
                    self.round_winners.extend(current_round_players[i:])

            threads = [threading.Thread(target=self.conduct_match, args=(match,)) for match in matches]
            [thread.start() for thread in threads]
            return [thread.join() for thread in threads]

    def add_wild_card_entries(self):
        available_players = [
            name for name in wwe_finishing_moves.keys() if name not in [player.name for player in self.players]
        ]

        wild_card_player = random.choice(available_players)
        self.round_winners.append(
            Player(wild_card_player, random.randint(10, 100), wwe_finishing_moves[wild_card_player])
        )

        print(f"⚠️⚠️⚠️⚠️ WILD CARD ENTRY! ===> {wild_card_player} has been added to the semifinals!")

    def run_semifinals(self):
        print("\n=== SEMI-FINALS ===")

        match_round = "Semi-finals"

        # Two semifinal matches
        match_1_players = random.sample(self.round_winners, 2)
        match_2_players = [player for player in self.round_winners if player not in match_1_players]

        semi1 = Match(match_1_players, '1v1', match_round)
        semi2 = Match(match_2_players, '1v1', match_round)

        self.round_winners = []
        for match in [semi1, semi2]:
            winner = match.conduct()
            self.round_winners.append(winner)

    def run_final(self):
        match_round = "Grand Finale"
        print(f"{Fore.MAGENTA}\n=== GRAND FINALE ===")
        final_match = Match(self.round_winners, '1v1', match_round)
        self.final_winner = final_match.conduct()
        print(f"{Fore.GREEN}\n\n🏆 NEW WWE CHAMPION: {self.final_winner.name} ({self.final_winner.energy}) 🏆")
        print(f"{Fore.CYAN}The new champion celebrates victory with a final {self.final_winner.finishing_move}!")

    def conduct_match(self, match):
        with self.lock:
            winner = match.conduct()
            self.round_winners.append(winner)

            # Replenish winner's energy
            if self.final_winner is None:
                winner.replenish_energy()

    def run_tournament(self):
        self.run_first_round()
        self.run_triple_threats()

        if len(self.round_winners) == 2:
            self.run_final()
            return

        if not len(self.round_winners) == 4:
            self.add_wild_card_entries()

        self.run_semifinals()

        self.run_final()


def validate_max_players(max_player_str: str):
    # Check if input is None
    if max_player_str is None:
        return False, "Input cannot be None."

    # Check if the input is a digit
    if not max_player_str.isdigit():
        return False, "Input must be a number."

    # Convert to an integer to check if it's even
    max_players_input = int(max_player_str)

    # Check if the number is even
    if max_players_input % 2 != 0:
        return False, "Input must be an even number."

    return True, None


if __name__ == "__main__":
    max_players = input("Enter the maximum number of players: ")

    # Validate max_players input
    valid, message = validate_max_players(max_players)

    while not valid:
        print(message)
        max_players = input("Enter the maximum number of players: ")
        valid, message = validate_max_players(max_players)

    max_players = int(max_players)

    # Select random players and create Player objects
    selected_players = random.sample(list(wwe_finishing_moves.items()), max_players)
    players = [Player(name, random.randint(10, 100), move) for name, move in selected_players]

    # Initialize and run tournament
    tournament = TournamentOrchestrator(players)
    tournament.run_tournament()
