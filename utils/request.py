import requests
import typing as t
from utils import colored


class Session:
    def __init__(self) -> None:
        self.session = requests.Session()

    def close(self) -> None:
        self.session.close()

    def request(
        self,
        method: str,
        url: str,
        *,
        params: t.Optional[dict[str, str]] = None,
        data: t.Optional[dict[str, str]] = None,
        json: t.Optional[dict[str, t.Any]] = None,
        headers: t.Optional[dict[str, str]] = None,
        timeout: int = 10,
        result_as_json: bool = False,
        result_as_text: bool = False,
        result_as_content: bool = False,
        **kwargs: t.Any,
    ) -> t.Union[dict[str, t.Any], str, bytes, requests.Response, None]:
        """
        Make a request using a persistent session and handle errors gracefully.

        Args:
            method (str): HTTP method (GET, POST, etc.).
            url (str): The full request URL.
            params (dict, optional): Query string parameters.
            data (dict, optional): Form data to include.
            json (dict, optional): JSON body.
            headers (dict, optional): HTTP headers.
            timeout (int): Timeout in seconds.
            result_as_json (bool): If True, return response.json(). Highest precedence.
            result_as_text (bool): If True, return response.text. Lower than JSON.
            result_as_content (bool): If True, return response.content. Lowest of the three.
            **kwargs: Additional arguments passed to requests.

        Returns:
            dict | str | bytes | Response | None: Parsed content or raw response, or None on error.
        """
        try:
            method = method.upper()
            colored.print_info(f"[Session] Sending {method} request to {url}")
            response = self.session.request(
                method=method,
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
                try:
                    return response.json()
                except ValueError:
                    colored.print_error("Invalid JSON received from the server.")
                    return None
            if result_as_text:
                return response.text
            if result_as_content:
                return response.content

            return response  # Default to returning raw response

        except requests.exceptions.Timeout:
            colored.print_error("Request timed out.")
        except requests.exceptions.HTTPError as e:
            status_code = e.response.status_code if e.response else "Unknown"
            colored.print_error(f"HTTP error {status_code}: {e}")
        except requests.exceptions.ConnectionError:
            colored.print_error("Connection error: Unable to reach the server.")
        except requests.exceptions.RequestException as e:
            colored.print_error(f"Request failed: {e}")
        except Exception as e:
            colored.print_error(f"Unexpected error: {e}")

        return None

def safe_request(
    method: str,
    url: str,
    *,
    params: t.Optional[dict[str, str]] = None,
    data: t.Optional[dict[str, str]] = None,
    json: t.Optional[dict[str, t.Any]] = None,
    headers: t.Optional[dict[str, str]] = None,
    timeout: int = 10,
    result_as_json: bool = False,
    result_as_text: bool = False,
    result_as_content: bool = False,
    **kwargs: t.Any,
) -> t.Union[dict[str, t.Any], str, bytes, requests.Response, None]:
    """
    Wrapper for HTTP requests using a persistent session with graceful error handling.

    Returns:
        dict | str | bytes | Response | None
    """
    session = Session()
    try:
        return session.request(
            method=method,
            url=url,
            params=params,
            data=data,
            json=json,
            headers=headers,
            timeout=timeout,
            result_as_json=result_as_json,
            result_as_text=result_as_text,
            result_as_content=result_as_content,
            **kwargs,
        )
    finally:
        session.close()
