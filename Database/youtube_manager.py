import sqlite3

connection = sqlite3.connect("youtube.db")
cursor = connection.cursor()

cursor.execute(''' 

CREATE TABLE IF NOT EXISTS videos (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    duration INTEGER NOT NULL
);

''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name,duration):
    cursor.execute("INSERT INTO videos (name, duration) values (?,?)", (name,duration))
    connection.commit()
def update_video():
    pass

def remove_video():
    pass

def main():
    while True:
        print("Welcome to the YouTube Manager")
        print("1. Add a video")
        print("2. Remove a video")
        print("3. update a video")
        print("4. List videos")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        match (choice):
            case '1':
                name = input("Enter name:")
                duration = input("Enter Duration:")  
                add_video(name,duration) 

            case '2':
                remove_video()
            case '3':
                update_video() 
            case '4':
                list_videos()
            case '5':
                print("Goodbye!")
    connection.close()

if __name__ == '__main__':
    main()

