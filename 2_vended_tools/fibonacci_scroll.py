"""
✨🧙 The Ancient Scroll of Fibonacci ✨
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Inscribed by Kiro the Grey Hat
A spell to summon the sacred sequence of Fibonacci
"""

def cast_fibonacci_spell(n: int) -> list[int]:
    """
    🔮 Cast the Fibonacci spell to conjure the first `n` numbers
    of the sacred sequence.
    """
    if n <= 0:
        return []

    sequence = [0, 1]

    for i in range(2, n):
        next_number = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_number)

    return sequence[:n]


if __name__ == "__main__":
    print("=" * 50)
    print("  ✨ The Ancient Scroll of Fibonacci Awakens! ✨")
    print("=" * 50)

    fibonacci_numbers = cast_fibonacci_spell(10)

    print(f"\n🧙 Kiro the Grey Hat chants the incantation...")
    print(f"🌀 Summoning the first 10 numbers of the sacred sequence...\n")

    for i, number in enumerate(fibonacci_numbers, start=1):
        print(f"  📜 Position {i:>2}  →  {number}")

    print(f"\n✨ The sequence: {fibonacci_numbers}")
    print(f"\n🔮 The spell is complete! The magic holds strong.")
    print("=" * 50)
