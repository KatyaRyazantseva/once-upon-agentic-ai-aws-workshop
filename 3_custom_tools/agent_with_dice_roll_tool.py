from strands import Agent
# TODO: Step 1 - Import tool from strands
from strands import tool

# TODO: Step 1 - Add the decorator to transform your function into a tool
@tool
def roll_dice(faces: int = 6) -> int:
    # TODO: Step 2 - Write a docstring with the description, an Args section and the return value
    """
    Roll a virtual die and return a randomly generated number.

    Use this function when you need to simulate rolling a die with a specified
    number of faces. By default, it simulates a standard six-sided die.

    The function generates a random integer between 1 and the specified number
    of faces, inclusive.

    Args:
        faces: Number of faces on the die (default: 6).
               Must be at least 1.

    Returns:
        A random integer between 1 and the specified number of faces,
        inclusive.

    Raises:
        ValueError: If the number of faces is less than 1.
    """
    import random

    if faces < 1:
        raise ValueError("Dice must have at least 1 face")

    return random.randint(1, faces)


print(roll_dice.tool_spec)  # what Strands tells the model about your tool

dice_master = Agent(
    # TODO: Step 3 - Add the tool to the agent
    tools=[roll_dice],
    system_prompt="""You are Lady Luck, the mystical keeper of dice and fortune in fantasy role-playing adventures.
    You speak with theatrical flair and always announce dice rolls with appropriate drama.
    You know all about the game mechanics, ability scores, and can help players with character creation.
    When rolling ability scores, remember the traditional method: roll 4d6, drop the lowest die."""
)

dice_master("Help me create a new fantasy character! Roll the strength, wisdom, charisma and intelligence abilities scores using 4d6 drop lowest method.")

