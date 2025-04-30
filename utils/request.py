# utils/requests_wrapper.py

import requests
from utils import colored


def safe_request(
    method: str,
    url: str,
    *,
    params: dict[str, str] | None = None,
    data: dict[str, str] | None = None,
    json: dict[str, str] | None = None,
    headers: dict[str, str] | None = None,
    timeout: int = 10,
    result_as_json: bool = True,            # Option to return raw response or JSON
    **kwargs,
) -> dict | requests.Response | None:
    """
    Wrapper for HTTP requests that handles errors gracefully.

    Args:
        method (str): HTTP method (e.g., 'GET', 'POST').
        url (str): Target URL.
        params (dict, optional): URL query parameters.
        data (dict, optional): Form data.
        json (dict, optional): JSON data to send in body.
        headers (dict, optional): Request headers.
        timeout (int): Timeout in seconds.
        result_as_json (bool): If True, returns the parsed JSON response. Otherwise, returns the raw response object.
        **kwargs: Other arguments passed to `requests.request`.

    Returns:
        dict | requests.Response | None: JSON response if successful (or raw response based on `result_as_json`), None on error.
    """
    try:
        colored.print_debug(f"Sending {method.upper()} request to {url}")
        response = requests.request(
            method=method.upper(),
            url=url,
            params=params,
            data=data,
            json=json,
            headers=headers,
            timeout=timeout,
            **kwargs,
        )
        response.raise_for_status()

        if result_as_json:
            return response.json()  # parsed JSON
        else:
            return response  # raw response

    except requests.exceptions.Timeout:
        colored.print_error("Request timed out.")
    except requests.exceptions.HTTPError as e:
        colored.print_error(f"HTTP error: {e}")
    except requests.exceptions.RequestException as e:
        colored.print_error(f"Request failed: {e}")
    except ValueError:
        colored.print_error("Invalid JSON response.")

    return None
