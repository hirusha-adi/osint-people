from utils import decorators, colored, request


@decorators.handle_errors
def start(email: str) -> None:
    colored.print_info(f"Checking Pinterest for email: {email}")

    url = "https://www.pinterest.fr/resource/EmailExistsResource/get/"
    params = {
        "source_url": "/",
        "data": '{"options": {"email": "' + email + '"}, "context": {}}',
    }

    data = request.safe_request("GET", url, params=params, result_as_json=True)

    if not data:
        colored.print_error("No data returned from Pinterest.")
        return

    exists = data.get("resource_response", {}).get("data")

    if exists:
        colored.print_success("[+] Account found in Pinterest.")
    else:
        colored.print_warning("[-] Account not found in Pinterest.")
