from utils import decorators, colored, request

@decorators.handle_errors
def start(email: str) -> None:
    colored.print_debug(f"Checking duolingo for email: {email}")

    # f"https://www.duolingo.com/2017-06-30/users?email={email}"
    url = "https://www.duolingo.com/2017-06-30/users"
    data = request.safe_request("GET", url, params={"email": email}, result_as_json=True)

    if data is None:
        colored.print_error("No data returned from duolingo.")
        return
    
    if not data.get("users"):
        colored.print_warning("Account not found in duolingo.")
    else:
        first_user: dict = data.get("users")[0]
        if first_user:
            username = first_user.get("username", None)
            if username:
                colored.print_success(f"Account found in duolingo, with username: {username}")
            else:
                colored.print_warning("Account not found in duolingo.")
        else:
            colored.print_warning("Account not found in duolingo.")
