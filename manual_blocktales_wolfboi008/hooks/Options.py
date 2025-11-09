# Object classes from AP that represent different types of options that you can create
from Options import Option, FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange, OptionGroup, PerGameCommonOptions, Visibility
# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value
from typing import Type, Any


####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#
class TotalCharactersToWinWith(Range):
    """Instead of having to beat the game with all characters, you can limit locations to a subset of character victory locations."""
    display_name = "Number of characters to beat the game with before victory"
    range_start = 10
    range_end = 50
    default = 50

class SoloMode(Toggle):
    """
    Enable Solo Mode, a mode where:
    1. Additional Party Member Items are removed from the item pool.
    2. Cards that are only beneficial in a party are removed from the item pool.
    """
    display_name: "Solo Mode"

class ISpyLogic(DefaultOnToggle):
    """
    Toggle if certain BUX Checks require the I Spy Card to obtain.
    Recommended for those that have no idea where some of the more hidden BUX are.
    """
    display_name: "I Spy Logic"

class Shopsanity(Toggle):
    """
    Add all of the items you can purchase in Shops as Checks.
    You do NOT have to buy everything in the Shops if you can't afford it.
    Just get to a Shop and you can send its Checks.
    Clarifying that now so people don't start grinding TIX for Shop Checks.
    (178 Checks)
    """
    display_name: "Shopsanity"

class BUXShopHints(DefaultOnToggle):
    """
    Toggle if the BUX Shop Checks will be automatically hinted at the start of the Multiworld.
    Disable if you want the items that are held in your BUX Shop to be a mystery...
    """
    display_name: "BUX Shop Hints"

class Levelsanity(DefaultOnToggle):
    """
    Add Level Ups as Checks.
    The Regions used for these are rough estimates on where you may level up.
    They may be slightly altered as I continue to update the Manual.
    (12 Checks)
    """
    display_name: "Levelsanity"

class Fishsanity(DefaultOnToggle):
    """
    Add catching fish as Checks.
    This also adds Worm as a Progression Consumable.
    You must have the Worm Item to fish.
    The fishing spot is located in the Meadows, in a room you normally go through.
    If you've been there before, you can easily warp to that room at anytime.
    (10 Checks)
    """
    display_name: "Fishsanity"

class Chatsanity(Toggle):
    """
    Add talking to NPCs as Checks.
    WARNING: If you enable this, prepare for way too much Filler.
    (705 Checks)
    """
    display_name: "Chatsanity"

class CAP(Choice):
    """
    As per Paragraph 4 of the CAP (Chatsanity Acknowledgement Pact), you must agree to the following to enable Chatsanity:
    By signing this definitely real contract, you acknowledge the consequences of having the Option 'Chatsanity' turned on, especially when enabled with a non-early Goal.
    Furthermore, you are aware of how many Checks and, by extension, how much Filler and/or Traps will be added to the pool for you as a result of this.
    Please sign the contract by choosing I Agree below to confirm that this is truly what you want.
    """
    option_i_agree = 0
    option_i_disagree = 1
    display_name: "CAP"

class Cutscenesanity(DefaultOnToggle):
    """
    Add in-game cutscenes as Checks.
    Cutscenes are usually the scenes where one or more of the following occur:
    - The screen has black bars on the sides
    - Unique NPC and/or Player animations
    - Forced interaction with characters that can't be avoided (like Kyoko in Chapter 2)
    ...or other things that are often unique to cutscenes.
    This is a bit iffy to determine what is/isn't a Cutscene, so input is appreciated so I can refine it.
    (79 Checks)
    """
    display_name: "Cutscenesanity"

class ThePit(Toggle):
    """
    Adds each floor of the Pit as Checks.
    Only enable if you don't mind potential in logic suffering.
    (40 Checks)
    """
    display_name: "The Pit"

class DisablePostGoalContent(DefaultOnToggle):
    """
    Remove Items and Checks that come after your selected Goal.
    Recommended for Syncs especially, but could be used in Asyncs, too.
    """
    display_name: "Disable Post-Goal Content"

class SoulType(Choice):
    """
    How does your soul look on the inside?
    This determines if you're going to be a nice person or a heartless person during your run.
    For example, Pure expects you to save Accountant Jim with the Dynamite, but Dark expects you to leave him there.
    (you monster)
    """
    option_pure = 0
    option_dark = 1
    display_name: "Soul Type"

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict[str, Type[Option[Any]]]) -> dict[str, Type[Option[Any]]]:
    options["solo_mode"] = SoloMode
    options["i_spy_logic"] = ISpyLogic
    options["shopsanity"] = Shopsanity
    options["bux_shop_hints"] = BUXShopHints
    options["levelsanity"] = Levelsanity
    options["fishsanity"] = Fishsanity
    options["chatsanity"] = Chatsanity
    options["cap"] = CAP
    options["cutscenesanity"] = Cutscenesanity
    options["the_pit"] = ThePit
    options["disable_postgoal_content"] = DisablePostGoalContent
    options["soul_type"] = SoulType
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: Type[PerGameCommonOptions]):
    # To access a modifiable version of options check the dict in options.type_hints
    # For example if you want to change DLC_enabled's display name you would do:
    # options.type_hints["DLC_enabled"].display_name = "New Display Name"

    #  Here's an example on how to add your aliases to the generated goal
    # options.type_hints['goal'].aliases.update({"example": 0, "second_alias": 1})
    # options.type_hints['goal'].options.update({"example": 0, "second_alias": 1})  #for an alias to be valid it must also be in options
    options.type_hints["co_op"].visibility = Visibility.none
    options.type_hints["bux_shop"].visibility = Visibility.none
    options.type_hints["shopsanity_currency"].visibility = Visibility.none
    options.type_hints["pure_soul"].visibility = Visibility.none
    options.type_hints["dark_soul"].visibility = Visibility.none
    options.type_hints["pre_prologue"].visibility = Visibility.none
    options.type_hints["prologue"].visibility = Visibility.none
    options.type_hints["chapter1"].visibility = Visibility.none
    options.type_hints["chapter2"].visibility = Visibility.none
    options.type_hints["chapter3"].visibility = Visibility.none
    options.type_hints["chapter4"].visibility = Visibility.none
    pass

# Use this Hook if you want to add your Option to an Option group (existing or not)
def before_option_groups_created(groups: dict[str, list[Type[Option[Any]]]]) -> dict[str, list[Type[Option[Any]]]]:
    # Uses the format groups['GroupName'] = [TotalCharactersToWinWith]
    return groups

def after_option_groups_created(groups: list[OptionGroup]) -> list[OptionGroup]:
    return groups
