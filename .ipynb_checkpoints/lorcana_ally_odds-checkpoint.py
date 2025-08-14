#!/usr/bin/env python3
import math
import sys

# ---------- Core math ----------
def comb(n, r):
    """Combination nCr with guards."""
    if r < 0 or r > n:
        return 0
    return math.comb(n, r)

def ally_hit_probability(total_cards: int, allies_left: int, look: int = 3):
    """P(hit ≥ 1 Ally) when looking at 'look' cards from N with K Allies."""
    if total_cards < look:
        raise ValueError(f"Need at least {look} cards left in the deck to perform the ability.")
    if allies_left < 0 or allies_left > total_cards:
        raise ValueError("Allies left must be between 0 and total cards.")
    denom = comb(total_cards, look)
    if denom == 0:
        return 0.0
    no_ally = comb(total_cards - allies_left, look) / denom
    return 1 - no_ally

def hypergeo_pmf(k, N, K, n):
    """P(X=k) for Hypergeometric(N, K, n)."""
    return comb(K, k) * comb(N - K, n - k) / comb(N, n)

def print_distribution(N, K, n):
    """Print distribution of Allies found among looked cards."""
    max_k = min(K, n)
    print("\nExact distribution (number of Allies found among the looked cards):")
    for k in range(0, max_k + 1):
        p = hypergeo_pmf(k, N, K, n)
        print(f"  P(X = {k}) = {p:.6f}  ({p*100:.2f}%)")
    print()

# ---------- Interactive helpers ----------
def prompt_int(msg, allow_blank=False, default=None):
    while True:
        s = input(msg).strip().lower()
        if s == 'q':
            raise KeyboardInterrupt
        if s == '' and allow_blank:
            return default
        try:
            return int(s)
        except ValueError:
            print("Please enter an integer (or 'q' to quit).")

def interactive():
    print("=== Lorcana Ally Hit Odds Calculator ===")
    print("Tip: press Enter to keep default values. Type 'q' to quit.")
    default_n = 3
    while True:
        try:
            N = prompt_int("\nTotal cards left in deck (N): ")
            K = prompt_int("Allies left in deck (K): ")
            n = prompt_int(f"Cards looked at (n) [default {default_n}]: ", allow_blank=True, default=default_n)

            p_hit = ally_hit_probability(N, K, n)
            print(f"\nResult: P(hit ≥ 1 Ally) = {p_hit:.6f}  ({p_hit*100:.2f}%)")
            print_distribution(N, K, n)
        except ValueError as e:
            print(f"Input error: {e}")
            continue
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

# ---------- Main ----------
def main():
    # CLI mode: python lorcana_ally_odds.py N K n
    if len(sys.argv) == 4:
        try:
            N = int(sys.argv[1])
            K = int(sys.argv[2])
            n = int(sys.argv[3])
        except ValueError:
            print("All arguments must be integers.")
            sys.exit(1)

        try:
            p_hit = ally_hit_probability(N, K, n)
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)

        print(f"Result: P(hit ≥ 1 Ally) = {p_hit:.6f}  ({p_hit*100:.2f}%)")
        print_distribution(N, K, n)
        return

    # No/incorrect args → show usage then interactive
    if len(sys.argv) != 1:
        print("Usage: python lorcana_ally_odds.py <N> <K> <n>")
        print("Example: python lorcana_ally_odds.py 40 10 3")
        print("No arguments? You’ll enter interactive mode.\n")

    interactive()

if __name__ == "__main__":
    main()
