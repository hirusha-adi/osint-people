import typing as t
from utils import decorators, colored, request

@decorators.handle_errors
def start(email: str) -> None:
    colored.print_info(f"Checking GitHub for email: {email}")

    # f"https://api.github.com/search/users?q={email}+in:email"
    url = "https://api.github.com/search/users"
    params = {"q": f"{email} in:email"}
    data = request.safe_request("GET", url, params=params, result_as_json=True)

    if data is None:
        colored.print_error("No data returned from GitHub.")
        return

    total_count = data.get("total_count", 0)

    if total_count == 0:
        colored.print_warning("Account not found in GitHub.")
        return

    colored.print_success(f"Accounts found in GitHub: {total_count}")
    print("----------")

    data: t.List[t.Union[None,t.Dict]] = data.get("items", [])
    for item in data:
        if item:
            print(f"Username: {item.get('login')}")
            print(f"ID: {item.get('id')}")
            print(f"Node ID: {item.get('node_id')}")
            print(f"Avatar URL: {item.get('avatar_url')}")
            print(f"Gravatar ID: {item.get('gravatar_id')}")
            print(f"Profile URL: {item.get('html_url')}")
            print(f"Followers URL: {item.get('followers_url')}")
            print(f"Following URL: {item.get('following_url')}")
            print(f"Gists URL: {item.get('gists_url')}")
            print(f"Starred URL: {item.get('starred_url')}")
            print(f"Subscriptions URL: {item.get('subscriptions_url')}")
            print(f"Organizations URL: {item.get('organizations_url')}")
            print(f"Repos URL: {item.get('repos_url')}")
            print(f"Events URL: {item.get('events_url')}")
            print(f"Received Events URL: {item.get('received_events_url')}")
            print(f"Type: {item.get('type')}")
            print(f"Site Admin: {item.get('site_admin')}")
            print(f"Score: {item.get('score')}")
            print("----------")

    if len(data) == 0:
        print("----------")
