import json
filename = "videos.txt"
def load_videos():
    try:
        with open(filename, 'r') as file:
            videos = json.load(file)
            return videos
    except FileNotFoundError:
        return []

def save_videos(videos):
    with open(filename, 'w') as file:
        json.dump(videos, file)

def list_videos(videos):
    print("*"*50)
    for index, video in enumerate(videos):
        print(f"{index + 1}. {video}")
    print("*"*50)

def add_video(videos):
    title = input("Enter the title of the video: ")
    duration = input("Enter the duration of the video (in minutes): ")
    videos.append({"title": title, "duration": duration})
    save_videos(videos)
    print("Video added successfully!")

def remove_video(videos):
    print("Enter the index of the video you want to remove: ")
    list_videos(videos)
    index = int(input())
    if index < 1 or index > len(videos):
        print("Invalid index. Please try again.")
        return
    videos.pop(index - 1)
    save_videos(videos)

def update_video(videos):
    list_videos(videos)
    index = int(input("Enter the index of the video you want to update: "))
    if index < 1 or index > len(videos):
        print("Invalid index. Please try again.")
        return
    title = input("Enter the new title of the video: ")
    duration = input("Enter the new duration of the video (in minutes): ")
    videos[index - 1] = {"title": title, "duration": duration}
    save_videos(videos)
    print("Video updated successfully!")

def main():
    videos = load_videos()
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
                add_video(videos)    
            case '2':
                remove_video(videos)
            case '3':
                update_video(videos) 
            case '4':
                list_videos(videos)
            case '5':
                print("Goodbye!")
                exit()
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
            