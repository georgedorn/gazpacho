import pytest

from gazpacho.get import HTTPError, get

HEADERS_API = "https://httpbin.agrd.workers.dev/headers"


def test_get():
    url = "https://en.wikipedia.org/wiki/Gazpacho"
    content = get(url)
    assert "<title>Gazpacho - Wikipedia" in content

def test_get_headers():
    UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:69.0) Gecko/20100101 Firefox/69.0"
    headers = {"User-Agent": UA}  # header names are case-insensitive, but gaz expects "User-Agent" exactly
    content = get(HEADERS_API, headers=headers)
    nocase_headers = {key.lower(): content[key] for key in content}
    if UA != nocase_headers["user-agent"]:
        raise AssertionError

def test_get_with_multiple_headers():
    headers = {"x-foo": "foo", "x-bar": "bar", "User-Agent": "Testing Gazpacho"}
    content = get(HEADERS_API, headers=headers)
    nocase_headers = {key.lower(): content[key] for key in content}
    for key in headers:
        assert nocase_headers[key.lower()] == headers[key]

#def test_get_params():
#    url = "https://httpbin.org/anything"
#    params = {"foo": "bar", "bar": "baz"}
#    content = get(url, params)
#    assert params == content["args"]


#def test_HTTPError_404():
#    url = "https://httpstat.us/404"
#    with pytest.raises(HTTPError):
#        get(url)
