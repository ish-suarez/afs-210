import random

'''
    Initializing An Instance Of A Song
'''
class Song():
    def __init__(self, title, artist) -> None:
        self.title = title
        self.artist = artist
        pass

    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist
        
    def __str__(self):
        return self.title + " by " + self.artist 

    def __eq__(self, other):
        return ((self.title, self.artist) == (other.title, other.artist))
        
    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        
    def __gt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))


'''
    Your Que Class For Traversing the Song Queue
''' 
class YourQue:
    def __init__(self, c = 0, p = False) -> None:
        self.que = []
        self.set_c(c)
        self.set_p(p)
        pass

    def set_c(self, index):
        self.c = index

    def set_p(self, p):
        self.p = p

    'Adding a song to the que'
    def add(self, song):
        if self.que_size() > 0:
            self.que.insert(self.que_size() + 1, song) # insert song
        else:
            self.que.insert(0, song) # Place first song at 0

    'Que size'
    def que_size(self):
        return len(self.que)

    'Play function'
    def play(self, song_index):
        self.c = song_index
        self.set_p(True)

    'Show que Function'
    def show_que(self):
        x = 1
        print("\nYour Que:\n")
        for i in self.que:
            print(f'{str(x)}. {str(i)}')
            x += 1

    'Currently playing function'
    def currently_playing(self):
        if self.p:
            print(f'\nCurrently Playing: {self.que[self.c]}')
        else:
            print('\nNo Song Is Currently Playing')

    'Next Function'
    def next(self):
        if self.p:
            que_length = len(self.que) - 1
            
            if self.c == que_length: # If last song, Play first
                next_song = 0
            else:
                next_song = self.c + 1 # if first song, play second and so on

            print("\nSkipping....")
            self.play(next_song)
        else:
            print('\nNo Song Is Currently Playing')

    'Rewind Function'
    def rewind(self):

        if self.p:
            que_length = len(self.que) - 1 # Setting Que legnth
            
            if self.c == 0: # if first song playing 
                prev_song = que_length
            else:
                prev_song = self.c - 1 # Play prev index

            print("\nReplaying....")
            self.play(prev_song)
        else:
            print('\nNo Song Is Currently Playing')

    'Remove Function'
    def remove_song(self, title):
        song_index = 0 # Song Index to be removed
        
        # Forloop of que
        for i in self.que:
            if i.title == title: # Title to be removed
                break   
            song_index += 1 # Runs to increase index to search for song

        self.que.pop(song_index) # Remove Song In Index
    
    'Shuffle Function'
    def shuffle(self):
        que_length = self.que_size()
        
        for i in range(que_length // 2):
            first_number = self.que.pop(0) # Pop and append to end of half the list
            self.que.append(first_number)
        
        for i in range(que_length):
            random_num = random.randint(0, que_length - 1) # Random Number selected

            list_element = self.que.pop(random_num) # Pop and append to end
            self.que.append(list_element)

def menu():
    print('\n')
    print(20 * "-" , "MENU" , 20 * "-")
    print("1. Add Song to Playlist")
    print("2. Remove song from Playlist")
    print("3. Play")
    print("4. Skip")
    print("5. Go Back")
    print("6. Shuffle")
    print("7. Show Currently Playing Song")
    print("8. Show Current Playlist Order")
    print("0. Exit")
    print(47 * "-")
    print('\n')

currentQue = YourQue()
currentQue.add(Song('Back in black', 'ACDC'))
currentQue.add(Song('Gummy Bear Song', 'Gummy Bear Guy'))
currentQue.add(Song('Chicken On a Raft', 'Chicken On A Raft Guy'))
currentQue.add(Song('If Walls Could Talk', '5 seconds of summer'))
currentQue.add(Song('Young Blood', '5 seconds of summer'))

'''
    While Statement For Menu
'''
while True:
    menu() # call the menu

    case = int(input()) # Input for media player

    '''
        Switch Statement Using Python
    '''
    if case == 1:
        title = input('Enter Song Title: ') # Enter Song Title
        artist = input('Enter Song Artist: ') # Enter The Artist

        new_song = Song(title, artist) # New Song Variable 

        currentQue.add(new_song)  # Add song to playlist

        print(f'{new_song} Added to Playlist')

    elif case == 2:
        title = input('Enter the Song Title to be Removed: ') # Removal input

        currentQue.remove_song(title) # Remove Song

        print(f'{title} Removed from Playlist')

    elif case == 3:
        currentQue.play(0) # Play first song in Que

        currentQue.currently_playing() # Currently Playing Display

    elif case == 4:
        currentQue.next() # Skip Song

        currentQue.currently_playing() # Currently Playing Display

    elif case == 5:
        currentQue.rewind() # Rewind

        currentQue.currently_playing()  # Currently Playing Display

    elif case == 6:
        currentQue.shuffle() # Shuffle Then Play Que
        currentQue.play(0)

        currentQue.currently_playing() # Currently Playing Display

    elif case == 7:
        currentQue.currently_playing()  # Currently Playing Display

    elif case == 8:
        currentQue.show_que() # Show Que

    elif case == 0:
        print('Thank You for Using My Mediaplayer')
        break