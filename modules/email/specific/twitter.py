from utils import decorators, colored, request


@decorators.handle_errors
def start(email: str) -> None:
    colored.print_debug(f"Checking Twitter for email: {email}")

    url = "https://api.twitter.com/i/users/email_available.json"
    params = {"email": email}
    data = request.safe_request("GET", url, params=params,result_as_json=True)

    if data is None:
        colored.print_error("No response received from Twitter.")
        return

    print("----------")
    print("Recieved data:")
    for key, value in data.items():
        print(f" - {key}: {value}")
    print("----------")
    
    if data.get("taken") is True:
        colored.print_success("Account found in Twitter.")
    elif data.get("taken") is False:
        colored.print_warning("Account not found in Twitter.")
    else:
        colored.print_error("Unexpected response from Twitter.")
