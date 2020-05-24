iTunes_balance = 100
SHORT_TRACK_PRICE = 1.79
MEDIUM_TRACK_PRICE = 2.50
LONG_TRACK_PRICE = 4.50

while iTunes_balance > 0:
    number_of_short_tracks = int(input("How many short tracks are you purchasing? "))
    iTunes_balance -= number_of_short_tracks
    if iTunes_balance > 0:
        number_of_medium_tracks = int(input("How many medium tracks are you purchasing? "))
        iTunes_balance -= number_of_medium_tracks
        if iTunes_balance > 0:
            number_of_long_tracks = int(input("How many long tracks are you purchasing? "))
            iTunes_balance -= number_of_long_tracks
