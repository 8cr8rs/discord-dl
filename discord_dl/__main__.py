import sys

# Call at repository's root directory using:
# python -m discord_dl

# if (__package__ == None) and (not getattr(sys, "frozen", False)):
  # import os.path

import discord_dl

# Main functionalities will only run if the file is called directly.
if (__name__ == "__main__"):
  print("Running from file: " + __file__)
  discord_dl.main()