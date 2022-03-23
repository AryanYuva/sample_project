print("exercise 8-7 functions,book python crash course")
def make_album(artist_name,album_name):
    music_dict = {}
    poll_active = True
    while poll_active:
        artist_name = input("Enter artist name\n")
        album_name = input("Enter album name\n")
        music_dict[artist_name] = album_name
        message = input("do you want to enter more album (yes/no)\n")
        if message == 'no':
            poll_active = False  
    print(music_dict)      
album = make_album(artist_name=" ",album_name=" ")
             