import requests
import sys


def get_user_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "github-activity-cli"
    }
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        
        for event in data[:5]:
            event_type = event["type"]
            repo = event["repo"]["name"]
            
            if event_type == "PushEvent":
                commits = event["payload"]["size"]
                if commits == 1:
                  print(f"Pushed {commits} commit to {repo}")
                else:
                    print(f"Pushed {commits} commits to {repo}")
                    
            elif event_type == "ForkEvent":
                original = event["repo"]["name"]
                forkee =  event["payload"]["forkee"]["name"]
                print(f"{original} forked to {forkee}")
                
            elif event_type == "IssueEvent":
                action = event["payload"]["action"]
                print(f"{action} issue found in {repo}")
            
            elif event_type == "PullRequestEvent":
                action = event["payload"]["action"]
                print(f"{action} a pull request in {repo}")
                
            elif event_type == "WatchEvent":
                action = event["payload"]["action"]
                print(f"{action} starred in {repo}")
            
            elif event_type == "CreateEvent":
                ref_type = event["payload"]["ref_type"]
                print(f"{ref_type} created in {repo}")
                
            elif event_type == "DeleteEvent":
                deleted = event["paylood"]["ref_type"]
                print(f"{ref_type} deleted in {repo}")
            
            else:
                print(f"{event_type} in {repo}")
                
                
        
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid command")
        sys.exit(1)
        
    username = sys.argv[1]
    get_user_activity(username)
    