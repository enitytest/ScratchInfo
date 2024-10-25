# Import the necessary module
from scratch import User

# Function to get all possible information about a Scratch user
def get_user_info(username):
    # Create a User object
    user = User(username)

    # Retrieve and print user information
    print(f"\nUsername: {user.exactUsername()}")
    print(f"User  ID: {user.id()}")
    print(f"Profile Picture: {user.profilepicture()}")
    print(f"Join Date: {user.joindate()}")
    print(f"Bio: {user.bio()}")
    print(f"Country: {user.country()}")
    print(f"Followers Count: {user.followersCount()}")
    print(f"Following Count: {user.followingCount()}")
    print(f"Followers: {user.followers()}")
    print(f"Following: {user.following()}")
    print(f"Projects Count: {user.projectsCount()}")
    print(f"Projects: {user.projects()}")
    print(f"Scratch Team Member: {user.scratchteam()}")
    print(f"User  Link: {user.link()}")

# Main program
if __name__ == "__main__":
    # Ask for the username
    username = input("Username: ")
    
    # Get user information
    get_user_info(username)