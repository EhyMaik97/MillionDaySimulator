"""
MillionDay Simulator
"""

import random
import json

def calculate_guesses(drawn_nums, played_nums, winning_combinations):
    """
    Calculate the number of guessed numbers and the amount won for a played combination.

    Args:
        drawn_nums (set): Set of drawn numbers.
        played_nums (set): Set of played numbers.
        winning_combinations (dict): Dictionary of winning combinations.

    Returns:
        tuple: A tuple containing the amount won and the updated dictionary of winning combinations.
    """
    guessed_nums = len(drawn_nums.intersection(played_nums))
    win_amt = 0

    match guessed_nums:
        case 5:
            win_amt += 1_000_000
            winning_combinations["5"] += 1
        case 4:
            win_amt += 1_000
            winning_combinations["4"] += 1
        case 3:
            win_amt += 50
            winning_combinations["3"] += 1
        case 2:
            win_amt += 2
            winning_combinations["2"] += 1

    return win_amt, winning_combinations

def simulate_lottery(num_extractions, num_tickets, playable_list):
    """
    Simulate a lottery game for a specific number of extractions and tickets.

    Args:
        num_extractions (int): Number of extractions to simulate.
        num_tickets (int): Number of tickets played for each extraction.
        playable_list (list): List of playable numbers.

    Returns:
        tuple: A tuple containing the total spent, total earned, and the dictionary of winning combinations.
    """
    total_spent = 0
    total_earned = 0
    winning_combinations = {
        "5": 0,
        "4": 0,
        "3": 0,
        "2": 0
    }

    for _ in range(num_extractions):
        drawn_nums = set(random.sample(playable_list, k=5))
        for _ in range(num_tickets):
            played_nums = set(random.sample(playable_list, k=5))
            total_spent += 1

            win_amt, winning_combinations = calculate_guesses(drawn_nums, played_nums, winning_combinations)
            total_earned += win_amt

    return total_spent, total_earned, winning_combinations

def main():
    """
    Main function to run the lottery simulation.
    """
    num_extractions = 2 * 365
    num_tickets = 100
    playable_list = list(range(1, 56))

    total_spent, total_earned, winning_combinations = simulate_lottery(num_extractions, num_tickets, playable_list)

    print(f"Winning Combinations: {json.dumps(winning_combinations, indent=2)}")
    print(f"Total Spent: {total_spent}")
    print(f"Total Earned: {total_earned}")

if __name__ == "__main__":
    main()