import json
from utils import decorators, colored, request


@decorators.handle_errors
def start(email: str) -> None:
    colored.print_info(f"Checking Spotify for email: {email}")

    # f"https://spclient.wg.spotify.com/signup/public/v1/account?validate=1&email={email}"
    url = "https://spclient.wg.spotify.com/signup/public/v1/account"
    params = {
        "validate": "1",
        "email": email,
    }

    data = request.safe_request("GET", url, params=params, result_as_json=True)

    if not data:
        colored.print_error("No data returned from Spotify.")
        return

    print("----------")
    print("Recieved data:")
    for key, value in data.items():
        if key == "allowed_calling_codes":
            print(f" - {key}: {json.dumps(value, indent=4)}")
            continue
        print(f" - {key}: {value}")
    print("----------")
    
    status = data.get("status")
    if status == 20:
        colored.print_success("[+] Account found in Spotify.")
    else:
        colored.print_warning("[-] Account not found in Spotify.")
