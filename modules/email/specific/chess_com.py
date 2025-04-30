from utils import decorators, colored, request

@decorators.handle_errors
def start(email: str) -> None:
    colored.print_info(f"Checking chess.com for email: {email}")

    # f"https://www.chess.com/callback/email/available?email={email}"
    url = f"https://www.chess.com/callback/email/available"
    data = request.safe_request("GET", url, params={"email": email}, result_as_json=True)
    
    if data is None:
        colored.print_error("No data returned from chess.com.")
        return

    if data.get("isEmailAvailable") is True:
        colored.print_warning("Account not found in chess.com.")
    elif data.get("isEmailAvailable") is False:
        colored.print_success("Account found in chess.com.")
    else:
        colored.print_error("Unexpected response format from chess.com.")
