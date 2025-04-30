import hashlib
from utils import decorators, colored, request


@decorators.handle_errors
def start(email: str) -> None:
    colored.print_info(f"Checking Gravatar for email: {email}")

    hashed_email = hashlib.sha256(email.lower().encode("utf-8")).hexdigest()
    url = f"https://en.gravatar.com/{hashed_email}.json"

    response = request.safe_request("GET", url, result_as_json=False)
    if response is None:
        colored.print_error("No response from Gravatar.")
        return

    if "User not found" in response.text:
        colored.print_warning("[-] Account not found in Gravatar.")
        return

    try:
        data = response.json()
        entry = data.get("entry", [{}])[0]

        print("----------")
        # Basic Information
        print("\nBasic Information:")
        for key in ["displayName", "preferredUsername", "profileUrl", "thumbnailUrl"]:
            value = entry.get(key)
            if value:
                print(f" - {key}: {value}")
        # Photos
        photos = entry.get("photos", [])
        if photos:
            print("\nPhotos:")
            for photo in photos:
                print(f" - {photo.get('type')}: {photo.get('value')}")
        # Accounts
        accounts = entry.get("accounts", [])
        if accounts:
            print("\nLinked Accounts:")
            for acc in accounts:
                print(f" - Platform: {acc.get('name')}")
                print(f"   Username: {acc.get('username')}")
                print(f"   Display: {acc.get('display')}")
                print(f"   URL: {acc.get('url')}")
                print(f"   Verified: {acc.get('verified')}")
                print("")
        print("----------")

        colored.print_success("[+] Account found in Gravatar.")

    except Exception as e:
        colored.print_error(f"Error parsing Gravatar data: {e}")
