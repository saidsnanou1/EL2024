import webbrowser
import platform
import sys

# Dictionary containing URLs of favorite websites
websites = {
    "linkedin": "https://www.linkedin.com/in/said-snanou-637b60157/",
    "youtube": "https://www.youtube.com/@moatasemelsayed6226",
    "github": "https://github.com/saidsnanou1/EL2024",
}


# Function to check the platform and configure the default browser
def check_platform():
    global edge
    system = platform.system()

    if system == "Windows":
        edge = webbrowser.get(
            "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
        )
    elif system == "Linux":
        edge = webbrowser.get("firefox")
    else:
        # Display an error if the platform is neither Windows nor Linux
        print("ERROR: This code runs only on Windows and Linux")
        sys.exit(0)


def favorite_websites(link):
    if link == "1":
        edge.open(websites["linkedin"])
        main()
    elif link == "2":
        edge.open(websites["youtube"])
        main()
    elif link == "3":
        edge.open(websites["github"])
        main()
    elif link == "4":
        custom_url = input("Enter your URL (e.g., www.google.com): ").strip().lower()
        edge.open(custom_url)
        main()
    else:
        print("ERROR: Invalid index. Choose 1 to 4.")
        main()


# Main function to display the menu and handle user input
def main():
    index = 1
    for site in websites:
        print(f"Enter {index} : {site}")
        index += 1
    print(f"Enter {index} : if you want to select another website")

    link = input("Choose an index to open a website: ").strip().lower()
    check_platform()
    favorite_websites(link)


if __name__ == "__main__":
    main()
