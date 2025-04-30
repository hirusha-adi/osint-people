from utils import decorators, colored, request


@decorators.handle_errors
def start(email: str) -> None:
    colored.print_info(f"Checking Imgur for email: {email}")

    url = "https://imgur.com/signin/ajax_email_available"
    payload = {"email": email}

    data = request.safe_request("POST", url, data=payload, result_as_json=True)

    if not data:
        colored.print_error("No data returned from Imgur.")
        return

    error = data.get("data", {}).get("error")
    available = data.get("data", {}).get("available")
    if error:
        colored.print_error(f"[!!] Error from Imgur: {error}")
    elif available is False:
        colored.print_success("[+] Account found in Imgur.")
    elif available is True:
        colored.print_warning("[-] Account not found in Imgur.")
    else:
        colored.print_error("Unexpected response format from Imgur.")
