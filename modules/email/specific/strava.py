from utils import decorators, colored, request


@decorators.handle_errors
def start(email: str) -> None:
    colored.print_debug(f"Checking Strava for email: {email}")

    url = "https://www.strava.com/athletes/email_unique"
    params = {"email": email}
    response = request.safe_request("GET", url, params=params, result_as_json=False).text

    if response is None:
        colored.print_error("No response received from Strava.")
        return
    
    if "false" in response:
        colored.print_success("[+] Account found in Strava.")
    elif "true" in response:
        colored.print_warning("[-] Account not found in Strava.")
    else:
        colored.print_error("[!!] Unexpected response from Strava:")
        colored.print_info(response)
