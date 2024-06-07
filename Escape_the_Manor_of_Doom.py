# IT-140 - Introduction to Scripting
# Module 6 - 4 Milestone: Moving Between Rooms
# Student: Chris Milazzo

import sys

# Defines Player Class, to hold Player Character's Name and Player Character's Current Room
class Player(object):
    def __init__(self, name, current_room):
        self.name
        self.current_room

# Inventory List to store Game Items collected by Player Character
inventory = []

# Welcomes Player, and names Game
def game_welcome():
    print(
        '''
        Welcome!
        Can you...
        \U0001F480 Escape the Manor of Doom?! \U0001F480
        
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠫⠙⠩⠉⠫⠙⡝⡻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠑⠀⠑⢊⠲⣍⠻⣝⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠣⢌⠳⣜⠻⣼⢯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠅⢎⡱⢬⠳⡭⣞⣳⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢢⠐⣊⠕⡳⢼⡹⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠡⡈⢜⠱⣫⢵⣻⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⡘⠤⠫⡔⢯⣞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢠⢓⡘⡳⣮⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠀⡜⢠⢣⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⢁⠸⢄⢣⣻⡽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠄⣘⡜⢢⢇⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣎⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣷⣌⡃⢎⠵⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠊⠀⢀⣀⣠⣶⣴⣶⣶⣶⣾⣿⣆⡁⢀⣄⣀⠀⠀⠀⠀⢤⣰⣿⣿⣿⣿⣿⣿⣷⣾⣿⣽⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢀⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠄⠨⠷⠀⢀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠘⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠀⠀⠻⣿⣿⣿⡻⢿⠻⡟⠋⠁⠀⠀⠀⠀⠀⠀⣠⣤⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠐⠀⠀⠈⢹⠿⠿⠷⠷⠀⠀⠀⠀⠀⠀⠀⢀⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡛⢿⣿⣿⣿⣿⡿⠃⢠⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⣀⣀⣤⣀⣀⣀⠀⠀⠀⠀⠀⣰⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣼⣽⣯⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣰⠀⠀⠙⠋⢉⠛⣋⠛⠀⠀⠀⠀⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣴⣤⣄⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⢽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣿⣾⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿⣿⣿⡇⡀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣶⡑⢦⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠈⢻⣿⣿⣃⠀⠀⠀⠀⠀⠀⠀⠐⠾⡿⢏⡳⣉⠶⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠙⣿⣿⣿⠀⢹⣶⡄⠀⠀⠀⠀⣴⣶⣿⣵⡎⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠻⣿⣿⣦⣄⡉⠛⠒⠂⠀⢹⣿⠿⢿⡃⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠈⠁⠉⢻⣷⢶⣤⣤⣄⣼⣯⣀⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠂⠀⠀⠀⠀⠀⠻⠁⣀⣿⠇⠀⢻⡗⠉⢻⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠈⠀⠀⡀⠀⠀⠉⠻⠟⣶⣶⣿⢿⣦⣶⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⡀⠀⠠⠀⠀⠀⠀⠀⠈⠙⠎⠙⡻⢟⡿⣻⢟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠂⠀⠀⠀⠀⠀⠀⢀⠹⢎⢶⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⢀⢀⣄⣚⢤⣫⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        '''
    )
    input('\nThere you are! Come into my study... I have something to tell you...  (Press Enter to continue.)\n')
    print('\U0001F480   \U0001F480   \U0001F480   \U0001F480   \U0001F480')

# Provides Game backstory, and objectives
def game_intro():
    print(
        f'''
Your great-(great-great-great)-Uncle Aloysius “Trespasser Killer” Goldensun has finally passed.
Or so we assume.

He hasn’t taken delivery of his monthly order of food, ale, and recently-dead corpses at Manor Goldensun for six months.
Even considering how… slender (fine, skeletal) he’s looked for the past many (well, over a hundred) years, he must have run out of provisions weeks ago.
While it’s possible he’s got a garden and some chickens stashed somewhere on the grounds of the Manor, 
    little would be growing there under the perpetual, pitch-black cloud cover that shadows his towe.
(And only the Manor — really the surrounding countryside is quite pleasant… and completely uninhabited: No one wants to be Aloysius’ neighbor).

The family has “nominated” you to enter Uncle Aloysius’ home and confirm that he’s... passed:
Either “away” or somewhere from whence he’s definitely never returning.
Find Uncle Aloysius, or, better yet, his body.
He used to spend a disproportionate amount of time in the Dining Room, working his way through the wine cellar, so check there first.

It goes without saying that if Uncle Aloysius is alive, he won’t… welcome intruders.
Nor will the guards that he’s known to keep to “eject” uninvited guests.
You'll need protection.

The long-lost Goldensun Signet should (probably, possibly) protect you from Uncle Aloysius’ curses.
He’s had it squirreled away in the Manor since your father’s time.

Uncle Aloysius keeps his prized tokens and collectibles in the Sitting Room, to show off to guests.
(Not that any of them have been known make it out alive in the last forty years or so to boast of them; Aloysius is cautious of attracting thieves).

Oh, and if Uncle Aloysius hasn't... passed... well, only the power of the Sun can make him vulnerable to harm. Just mentioning....

There should be plenty of enchanted weapons about the place to deal with more mundane hazards.

Since you’re going, make sure you return with the Deed of Ownership for the Manor.
Baron Avaricious (your cousin, twelve times removed) has been making noises about seizing the Manor as properly belonging to his branch of the family.
(The baron might have made more than noises if the memory of his grandfather’s Unfortunate Fate wasn’t still sharp in everyone’s mind, after he demanded that Aloysius vacate the premises.)
Legend holds that the holder of the Deed possesses all the formidable power of Goldensun line...  
The Library is the place to look for legal documents, and the like. Uncle Aloysius keeps his more… specialized reading materials in his Laboratory; one supposes it might be there, too.

While you’re there, feel free to pick up any interesting items that the family might appreciate: It is your mother’s birthday next week.
Your aunts, in particular, have asked you to retrieve their lost cloaks, and hats:
They left them behind when your father’s Coming of Age party at the Manor went.. awry, fifty years ago.
Your grandfather thoroughly annoyed Aloysius, and Aloysius replied with some very unsavory curses.
Aunt Pauline’s hair has never been the same….
Check the Cloak Room, to start.

Now, here’s the key to the front door: Don't die.

\U0001F480   \U0001F480   \U0001F480   \U0001F480   \U0001F480
        '''
    )
    input('Press Enter to continue. \n')

# Creates new Game instance, and requests Player's Character Name
def new_game():
    new_game = False

    start_game = input('Are you ready to begin? Y / N ')

    # Sets new_game to True, enabling Function, main()
    if start_game == 'Y' or 'y':
        new_game = True
        Player.name = input("Enter your Player Name: ")
        print('\n\U0001F480   \U0001F480   \U0001F480   \U0001F480   \U0001F480\n')
        # game_intro()
    else: # FIX THIS
        game_welcome()
        # exit()

# Establishes Player in Courtyard of Manor, initializes the Player Property, curent_room, and first Inventory item (QA Test)
def begin_game():
    print(
        f'''
You find yourself in the Courtyard of Manor Goldensun.

To the East is a three-story sandstone tower.
Once the golden hue of the stones must have shone like a beacon under the evening sunlight that shines in the distant meadows to the West.
Now the tower broods like an ancient gravestone, gray and lifeless, in the dim light under the ever-circling black clouds that fill the sky.
Splashes of red the color of fresh blood blotch the walls where struck by the evening Sun.

In your pocket is the bright brass key for the double entry-doors before you, unused for decades if not longer.
No one in memory has visited Manor Goldensun, but the key has been diligently polished with the family silver:
An heirloom and a promise that, someday, the Manor would be open to the family again.

To the West the road stretches into the far distance, and, beyond it, home. From the evening shadows... things... are emerging; only death lies that way, now.

Now, {Player.name}, is your chance to explore the Manor, and reclaim it as the proper seat for your family!”

\U0001F480   \U0001F480   \U0001F480   \U0001F480   \U0001F480
        '''
    )

    # Initializes Player Property, Current Room, to 'Entry Hall'
    Player.current_room = 'Courtyard'

    # Initializes Inventory List with first Item, Entry Key
    inventory.append('Entry Key')

# Provides Player with instructions to Move, Take Items, Repeat Current Room Description and Inventory, and Exit
def player_instructions():
    print(
        f'''
        To navigate within the game, enter the command,
            
            move N S E or W

                N: Travel North
				S: Travel South
				E: Travel East
				W: Travel West


        To add an Item to your Inventory, enter the command,
			
			take ‘Item Name’
			
			
		To print your Current Room, Inventory and a description of your location, enter the command,
		
		    describe


        To exit the game, enter the command,
            
            exit

                \u2B50   \u2B50   \u2B50
        
		You are in the {Player.current_room}.

		Your Inventory contains: {inventory}

                \u2B50   \u2B50   \u2B50
        '''
    )

# Enables Player Character movement through the mapped rooms of the Game
def move_player(selected_action):

    # Splits Player input String to determine selected Direction of movement
    split_action = selected_action.split(' ', 1)
    direction = split_action[1]

    # Determines viability of selected Player direction through reference to >> rooms << Dictionary
    if direction in rooms[Player.current_room]:
        Player.current_room = rooms[Player.current_room][direction]
        print(rooms_descriptions[Player.current_room])
        # print(Player.current_room)
    else:
        print('There\'s nothing in that direction.')

    # Assigns newly-entered Room to current_room Property of Player Class
    return Player.current_room

# Enables the Player Character to add identified Items to Inventory
def take_item(selected_action):

    # Splits Player input String to determine Item the Player wishes to add to Inventory
    split_action = selected_action.split(' ', 1)
    selected_item = split_action[1]

    # Determines if Player-identified Item is a valid Game Item, and if it is located in the Current Room
    if selected_item == room_items[Player.current_room]:
        inventory.append(room_items[Player.current_room])
        print(
            f'''
        You've added the {room_items[Player.current_room]} to your Inventory!
            
        Your inventory contains: {inventory}
            
                \u2B50   \u2B50   \u2B50
            '''
        )
        # room_items.update({Player.current_room: ''})  # Deprecated in favor of room_item.pop (below)
        room_items.pop(Player.current_room)
    else:
        print("No such item is available to pick up.")

def describe_room():

    print(
        f'''
		        \u2B50   \u2B50   \u2B50
		
		You are in the {Player.current_room}.

		Your Inventory contains: {inventory}
		
		        \u2B50   \u2B50   \u2B50
        '''
    )
    print(rooms_descriptions[Player.current_room])

# Manages overall gameplay, and invokes subsidiary Functions as needed (e.g., move_player())
def main():
    while new_game:

        if 'Silver Long Sword' and 'Goldensun Signet Ring' and 'Deed of Ownership' and 'Sungem' in inventory:
            print(
                '''
    Congratulations! You have the tools that you need to defeat Uncle Aloysius!
    
    You have conquered the Manor of Doom!
    
        \u2B50   \u2B50   \u2B50
                '''
            )
            break
        elif 'Glowing Decanter' in inventory:
            print(
                '''
    The dark amber brandy is simply the finest you've ever seen!
    Its pulsing glow seems to beckon you...
    You're unable to resist a quick sip...
    Which is a mistake.
    The magical liquid burns through your veins, slowly corrupting you in agonizing waves of transformation.
    All you can see are your hands, clutched to your chest, rotting from within, as the cold of undeath takes you forever.
                
        \U0001F480   \U0001F480   \U0001F480
                '''
            )
            break
        elif Player.current_room == 'Fields of the Dead':
            print(
                '''
    You blood and breath are a siren call to the undead cursed to dwell forever in the Fields surrounding the Manor.
    
    You cannot run fast enough to escape them, nor find place safe from their intrusion.
    
    Their claws, rotting and sharp, seize your arms and legs, and the only question is whether you'll pass beyond or join them in undeath.
                
        \U0001F480   \U0001F480   \U0001F480
                '''
            )
            break
        elif Player.current_room == 'Pantry':
            print(
                '''
    You open the door to meet the eyes of... Uncle Aloysius --  
    Dressed in rich brocades of black and silver and skulls all over, it can't be anyone else.
    
    Standing in the middle of an amazingly well-stocked Pantry, he seems puzzled at your appearance, but almost indifferently so.
    Clearly more interested in the truly delicious-looking sandwich he's assembling, 
        he absently waves a slightly mayonnaised hand in your direction.
    
    Your final thought, as Death consumes your body, is, I haven't even eaten today.
                
        \U0001F480   \U0001F480   \U0001F480
                '''
            )
            break

        selected_action = input('What would you like to do next? ')

        action = selected_action.split()

        if action[0] == 'move':
            move_player(selected_action)
        elif action[0] == 'take':
            take_item(selected_action)
        elif action[0] == 'describe':
            describe_room()
        elif action[0] == 'exit':
            print('''
            You\'ve exited...
            
            \U0001F480   Game Over!   \U0001F480
            ''')
            break
        else:
            print("Invalid command.")

# Dictionary of mapped Game Rooms, and each Room's valid directions of travel to adjacent Rooms
# Referenced: mover_player()
rooms = {
    'Fields of the Dead': {'E': 'Courtyard'},
    'Courtyard': {'E': 'Entry Hall', 'W': 'Fields of the Dead'},
    'Entry Hall': {'N': 'Cloak Room', 'E': 'North Hallway', 'S': 'Sitting Room', 'W': 'Courtyard'},
    'Cloak Room': {'S': 'Entry Hall', 'E': 'North Parlor'},
    'North Parlor': {'E': 'Kitchen', 'S': 'North Hallway', 'W': 'Cloak Room'},
    'North Hallway': {'N': 'North Parlor', 'E': 'Salle de Bains', 'S': 'Sitting Room', 'W': 'Entry Hall'},
    'Salle de Bains': {'W': 'North Hallway', 'S': 'Pantry'},
    'Kitchen': {'N': 'North Parlor', 'S': 'Dining Room', 'W': 'Pantry'},
    'Sitting Room': {'N': 'Entry Hall', 'E': 'Pantry', 'S': 'Trophy Room'},
    'Pantry': {'N': 'Salle de Bains', 'E': 'Kitchen', 'S': 'Dining Room', 'W': 'Sitting Room'},
    'Trophy Room': {'N': 'Sitting Room', 'E': 'Dining Room'},
    'Dining Room': {'N': 'Pantry', 'E': 'Library', 'S': 'Lounge', 'W': 'Trophy Room'},
    'Lounge': {'N': 'Dining Room', 'E': 'Solarium'},
    'Library': {'S': 'Solarium', 'W': 'Dining Room'},
    'Solarium': {'N': 'Library', 'W': 'Lounge'}
}

# Dictionary of Game Items, by Room in which each is located
# Referenced: take_item()
room_items = {
    'Cloak Room': 'Golden Cape',
    'North Parlor': 'Glowing Decanter',
    'North Hallway': 'Silver Long Sword',
    'Salle de Bains': 'Diamond Fascinator',
    'Kitchen': 'Enchanted Cleaver',
    'Sitting Room': 'Silver Frog Ashtray',
    'Trophy Room': 'Goldensun Signet Ring',
    'Dining Room': 'Carving Knife',
    'Lounge': 'Silver Candleabra',
    'Library': 'Deed of Ownership',
    'Solarium': 'Sungem'
}

# Dictionary of mapped Game Rooms, and their Descriptions (noting Game Items), presented when each becomes Current Room
rooms_descriptions = {

    'Fields of the Dead': f'''

    As you leave the Manor Courtyard the shadows clinging to every nook, crevasse and overhang deepen to a pitiless black.
    The briefest glance into their depths seems to pull your soul from your body.
    
    And then the claws begin to emerge from them...
    
    ''',
    'Courtyard': f'''
    
    You are in the courtyard of Manor Goldensun.
    The empty flagstones are bounded on the North and South by formidable walls, unclimable and bare where not clawed by dry and crumbling vines.
    The Manor's sole visible building is a three-story sandstone tower, to the East.
    Once the golden hue of the stones must have shone like a beacon under the evening sunlight that shines in the distant meadows to the West.
    Now the tower broods like an ancient gravestone, gray and lifeless in the dim murk under the ever-circling black clouds that fill the sky.    

    To the East are the double entry-doors of tower.
    To the West the road stretches into the far distance, home lying beyond. From the evening shadows... things... are emerging; only death lies that way, now.
    
    ''',
    'Entry Hall': f'''
    
    You find yourself in a large square room, lit only by the dim light bleeding in through the open Manor doors.
    The tesselated marble floor might truly be white and black, but in the ruddy glow of evening, red alternates with abyssal black.
    You feel that, should you not step carefully, you may fall into depthless darkness below.
    
    To the North is a broad entry to a room that appears to hold an inordinate number of coats, cloaks, walking sticks and other outdoors paraphernalia.
    To the East extends a long corridor, with a least one door at its far end.
    To the South double-doors block your view of Manor beyond.
    To the West are the entry doors to the Manor, leading back to the Manor courtyard.
    
    ''',
    'Cloak Room': f'''
    
    You are in a rather smaller, windowless room, lit by tastefully minimalist pendulum lamps and several sconces.
    Before you, a small, elegant table holds several fetching mens hats in the vibrant colors of Spring flowers.
    To the left of the table, several floor racks hold a neatly-ordered regiment of walking sticks, umbrellas, and foldable field-chairs.
    Behind the table a veritable forest of coats, shawls, muffs, ruffs, and throws stretches into dim shadows.

    Among them, though, blazes a golden light that you initially mistake as coming from a hidden window.
    On closer look, the light is the reflected radiance of a Golden Cape that seems to shimmer like water lit by the noontime radiance of the Sun.
    Great-Aunt Zelda has often sighed over its loss, the irreplaceable gift of a long-past lover from distant shores.

    To the East are double-doors, partly ajar, the ruddy evening light shining through.
    To the South is a broad entry leading to the Entry Hall.
    
    ''',
    'North Hallway': f'''
    
    Strong oak floor boards point deeper into the Manor, the walls of the hallways softened by thick woolen tapestries.
    Only a single sconce is lit, near the West end, and a dim glow from the Entry Hall lessens the gloom.
    At precisely the mid-point of corridor a noble figure stands against the South wall.
    Approaching it resolves to a suit of silver armour, fixed in place to a wooden pedestal.

    The armoured figure holds a Silver Long Sword, nearly as tall as you, glimmering with an uncorruptable light, even in shadows of the Hallway.
    
    To the North are partly-cracked doors.
    To the West, at the very end of the corridor, is a thick wooden door.
    
    ''',
    'North Parlor': f'''
    
    Rich sapphire and emerald rugs every inch of visible floor in this magnificent room, muted in places by smaller throw-rugs of rich chocolate and amber.
    Couches, settees, chairs, lounges and a seemingly endless variety of furniture on which to relax cluster across the room.
    Windows line the entirety of the North wall, floor to ceiling, admitting the amber glow of evening and seemingly thick enough to withstand seige engines.
    Tables of every size accompany each cluster of seats, themselves covered with knick-knacks, vases, ashtrays, and entirely unidentifiable objects of great fragility.
    A prominent buffet, along the southeast wall holds a series of silver trays, glasses and, most prominently, carafes and decanters.

    All of the decanters appear empty, but one.
    That Glowing Decanter one seems to hold a rich brandy that almost burns with an inner light, quietly pulsing.
    
    To the East open doors offer a view of a dim corridor that appears to dog-leg South after only a short stretch.
    To the South partly-cracked doors offer exit to a room, or rooms unseen.
    To the West double-doors slightly ajar lead in the direction of the Entry Way.
    
    ''',
    'Salle de Bains': f'''
    
    Unexpectedly bright golden and silver lights flood every inch of this tiled, mirrored and gilded temple to beauty and cleanliness.
    Several large marble sinks line the West wall, over which float flawless mirrors that stretch to the ceiling.
    The North wall offers multiple discretely panelled doors, nearly invisible against the wainscoting, opening into small, porcelin rooms in which more personal needs can be addressed.
    The middle of the room holds several low chaises with accompanying side tables, across which are scattered hand mirrors, brushes, combs and other necessities for Keeping Up Appearances.

    Resting on one these delicate vanities blazes a captured star, spikes of white light from its crowning piercing each wall.
    Encrusted on every visible surface, the Diamond Fascinator fully deserves its reputation for creative design and showmanship.
    Great-Aunt Pauline has never found a chapeau, veil, or tiara to compensate for its loss... 
    Or fully mask the Unfortunate State of her hair since coming between Uncle Aloysius and the target of one of his curses.
    
    To the South opens a single, heavy white door, panelled like the rest of the unmirrored walls and offering no hint of what lies beyond.
    To the West a thick, panelled wooden door leads in the direction of the Entry Hall.
    
    ''',
    'Kitchen': f'''
    
    The blazing fires from the two roasting pits reflect from the dozens--hundreds--of pots, pans, trays and utensils hanging
        in seried ranks across the length and breadth of the room.
    At least two stoves are immediately visible, and every every piece of wall not taken by the hearths and stoves
        holds shelving filled with dishes, bowls, cups, and glasses of every size and material.
    The center of the room is dominated by a series of wooden work tables and butchers blocks.
    
    Embedded by its tip in the largest butcher block is a cleaver.
    More than an ordinary kitchen tool, simply to look at its fine edge is to be cut by its magically-honed blade.
    The Enchanted Cleaver is Death's tool, both an instrument to kill, and to... dispose of the remains.
    
    ''',
    'Sitting Room': f'''
    
    Cozy, inviting, and almost painfully domestic, you feel an almost irresistable compulsion to sit in one of lushly pholstered lounge chairs,
        and light a cigar, and simply... let the night pass.
    Each chair looks more comfortable than the last, and each accompanying side table filled with enticing delights:
        a humidor opened to display its cigars on one, a rank of liquers on a second, a gorgeously crafted chess set on a third.
    
    Seizing your attention on table graced with a fan of cigarillos stands, or rather squats, a truly subversive work of luxury:
    The Silver Frog Ashtray appears almost alive. In fact, it appears to be smirking at you.
    As you continue to stare, its eye seem--surely only seem--to glance down at the cigarillos, inviting you to partake.
    If any gift would satisfy your Mother, surely its this. Assuming she endures to her birthday, of course. 
    
    ''',
    'Pantry': f'''
    
    Pantry
    
    ''',
    'Trophy Room': f'''
    
    The heads are clearly glaring at you.
    Mounted above and below and across every inch of wallspace, they seem to resent your living presence more than the indignity of their fate.
    Deer, boar, auroch, giant serpent, elk, panther, manticore, and the collected heads of at least two chimera,
        each set of eyes promises a similar fate to you, should you step to close.
    
    Filling the floor almost as tightly as the beasts fill the walls are tall crystal cases, 
        their multiple shelves filled every manner of jewelry, chalice, sporting trophy, and small body part.
    You count at least half a dozen eyes, some preserved in small flasks, others of gemlike substances that retain their integrity.
    One case seems largely dedicated to hands, claws and paws. One particularly pale specimen twitches and reaches as you approach.
    Clearly, vampires endure even beyond dismemberment.
    
    A central display, taller and more ornately carved than the others, throws a rainbow of light across the room.
    The loose gems, bracelets, earrings, necklaces and rings are a dragon's hoard of wealth, and almost mezmerizing in their glory.
    
    Amongst these lavishly carved, embossed, encrusted, and polished pieces of supreme artisanship, one ring stands out for its drabness.
    A matte gold, and decorated only with a worn and nicked Goldensun coat of arms, the Goldensun Signet Ring is a pauper's trinket in this company. 
    
    ''',
    'Dining Room': f'''
    
    Set to host dozens of guests, an ebony dining table stretches the length of the immense room, its surface, 
        where visible under the plates, glasses, silver, candelabra, and centerpieces, perfectly reflects the room in its polished blackness.
        
    Along each wall a host of buffets, tall cabinets, charts and chafing tables stands ready to hold, transport, store and warm
        food and dishes for a regiment of diners. 
    
    While every piece in the room is spotlessly kept--not the smallest mote of dust visible on any surface--the room presents as a frozen tableau,
        and you wonder if anyone has eaten a meal here in your lifetime.
    
    At one end of the table, holding a pride of place raised above the neighboring settings, a silver post suspends a viciously curved, mirror-bright knife.
    The Carving Knife almost appears to float in mid-air, and while, from its presense in this room, seems intended to work upon the roasts,
        birds, and loins served to guests, clearly the knife is fit to carve more than a poor turkey.
    
    ''',
    'Lounge': f'''
    
    Lounge
    
    Silver Candleabra
    
    ''',
    'Library': f'''
    
    Library
    
    Deed of Ownership
    
    ''',
    'Solarium': f'''
    
    Solarium
    
    Sungem
    
    '''
}


game_welcome()

game_intro()

new_game()

# intro_splash()

begin_game()

player_instructions()

main()



# Unused Code!

# def user_command(selected_action):
#
#     if 'move' in selected_action:
#         move_player(selected_action)
#     elif 'take' in selected_action:
#         print('take')
#     elif 'Help'  in selected_action:
#         player_instructions()
#     else:
#         print('That isn\'t a valid command. Please try again.')
#         selected_action = input('What would you like to do next? ')


# Creates Game atmosphere, and indicates Game is Rogue-Lite
# def intro_splash():
#     print(
#         '''
# It is too late to turn back, now...
#
#         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠫⠙⠩⠉⠫⠙⡝⡻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠑⠀⠑⢊⠲⣍⠻⣝⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠣⢌⠳⣜⠻⣼⢯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠅⢎⡱⢬⠳⡭⣞⣳⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢢⠐⣊⠕⡳⢼⡹⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠡⡈⢜⠱⣫⢵⣻⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⡘⠤⠫⡔⢯⣞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢠⢓⡘⡳⣮⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠀⡜⢠⢣⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⢁⠸⢄⢣⣻⡽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠄⣘⡜⢢⢇⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣎⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣷⣌⡃⢎⠵⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠊⠀⢀⣀⣠⣶⣴⣶⣶⣶⣾⣿⣆⡁⢀⣄⣀⠀⠀⠀⠀⢤⣰⣿⣿⣿⣿⣿⣿⣷⣾⣿⣽⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢀⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠄⠨⠷⠀⢀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠘⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠀⠀⠻⣿⣿⣿⡻⢿⠻⡟⠋⠁⠀⠀⠀⠀⠀⠀⣠⣤⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠐⠀⠀⠈⢹⠿⠿⠷⠷⠀⠀⠀⠀⠀⠀⠀⢀⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡛⢿⣿⣿⣿⣿⡿⠃⢠⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⣀⣀⣤⣀⣀⣀⠀⠀⠀⠀⠀⣰⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣼⣽⣯⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣰⠀⠀⠙⠋⢉⠛⣋⠛⠀⠀⠀⠀⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣴⣤⣄⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⢽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣿⣾⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿⣿⣿⡇⡀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣶⡑⢦⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠈⢻⣿⣿⣃⠀⠀⠀⠀⠀⠀⠀⠐⠾⡿⢏⡳⣉⠶⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠙⣿⣿⣿⠀⢹⣶⡄⠀⠀⠀⠀⣴⣶⣿⣵⡎⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠻⣿⣿⣦⣄⡉⠛⠒⠂⠀⢹⣿⠿⢿⡃⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠈⠁⠉⢻⣷⢶⣤⣤⣄⣼⣯⣀⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠂⠀⠀⠀⠀⠀⠻⠁⣀⣿⠇⠀⢻⡗⠉⢻⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠈⠀⠀⡀⠀⠀⠉⠻⠟⣶⣶⣿⢿⣦⣶⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⡀⠀⠠⠀⠀⠀⠀⠀⠈⠙⠎⠙⡻⢟⡿⣻⢟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠂⠀⠀⠀⠀⠀⠀⢀⠹⢎⢶⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⢀⢀⣄⣚⢤⣫⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#
# Prepare yourself...
#         '''
#     )
#     input('Press Enter to continue')

