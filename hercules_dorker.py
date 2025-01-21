import pyfiglet
from googlesearch import search

# ASCII Art Banner
def display_banner():
    """
    Displays the Hercules banner with a larger font size.
    """
    banner = pyfiglet.figlet_format("HERCULES", font="slant")  # Large banner with "slant" font
    print(banner)
    print("=== Sensitive File Hunter ===")
    print("Developed by: Shaheer Yasir (shaheeryasirx1@gmail.com)")
    print("Hacking Beyond Limits")
    print("=========================================\n")

# Predefined Google Dorking Queries
DORKS = [
    "ext:env intext:DB_PASSWORD",
    "ext:sql intext:password",
    "ext:log intext:password",
    "ext:config intext:dbuser",
    "ext:backup inurl:backup",
    "site:github.com inurl:.env",
    "site:pastebin.com password",
    "intitle:index.of passwd",
    "intitle:index.of wp-config.php",
    "intitle:index.of admin",
    "filetype:log error",
    "filetype:bak inurl:backup",
    "filetype:txt username password",
    "ext:json intext:apikey",
    "ext:xml intext:password",
    "inurl:/wp-content/uploads/ intext:backup",
    "inurl:admin intext:login",
]

# Function to perform Google Dorking
def perform_search(query, num_results=10):
    """
    Performs a Google search using the provided query.
    :param query: Google Dork query string.
    :param num_results: Number of results to retrieve per query.
    :return: List of search result URLs.
    """
    print(f"[*] Searching for: {query}")
    results = []
    try:
        for result in search(query, num_results=num_results, lang="en"):
            results.append(result)
            print(f"  [+] Found: {result}")
    except Exception as e:
        print(f"  [!] Error during search: {e}")
    return results

# Function to load external dork list
def load_external_dork_list(file_path):
    """
    Loads custom dorks from an external file.
    :param file_path: Path to the file containing dorks.
    :return: List of dorks from the file.
    """
    try:
        with open(file_path, "r") as file:
            dorks = [line.strip() for line in file.readlines() if line.strip()]
            print(f"[*] Loaded {len(dorks)} custom dorks from {file_path}")
            return dorks
    except FileNotFoundError:
        print(f"[!] Error: File not found: {file_path}")
        return []
    except Exception as e:
        print(f"[!] Error reading file: {e}")
        return []

# Main Functionality
def main():
    # Display Banner
    display_banner()

    # Ask user for the target website (optional feature)
    target_website = input("Enter the target website for Google Dorking (e.g., example.com) or press Enter to search globally: ").strip()

    # Ask user for custom dork list file (optional)
    external_dork_file = input("Enter the path to a custom dork list file (or press Enter to skip): ").strip()
    if external_dork_file:
        external_dorks = load_external_dork_list(external_dork_file)
    else:
        external_dorks = []

    # Merge predefined and external dorks
    all_dorks = DORKS + external_dorks

    # Modify dorks with target website if provided
    if target_website:
        all_dorks = [f"site:{target_website} {dork}" for dork in all_dorks]

    # Ask user for the number of results per query
    try:
        num_results = int(input("Enter the number of results to retrieve per query (e.g., 10): "))
    except ValueError:
        print("[!] Invalid input. Defaulting to 10 results per query.")
        num_results = 10

    print("\n[*] Starting Automated Google Dorking...\n")

    # Collect all results
    all_results = []
    for dork in all_dorks:
        results = perform_search(dork, num_results)
        all_results.extend(results)

    # Save results to a file
    with open("hercules_results.txt", "w") as f:
        for url in all_results:
            f.write(url + "\n")

    print("\n[*] Google Dorking Complete!")
    print(f"[*] Results saved to: hercules_results.txt")

if __name__ == "__main__":
    main()
