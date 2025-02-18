import re
from urllib.parse import urlparse


def _analyse(url: str) -> str:
    # if '?s=' in url:
    #     return url[:url.find('?s=')]
    if '?si=' in url:
        return url[:url.find('?si=')]
    return ''


def get_response(user_input: str) -> str:
    pattern: str = r'<(https?://[^>\s]+)>|\[(?:[^\]]+)\]\(\s*(https?://[^\s)]+)\s*\)|\b(https?://[^\s)]+)'
    matches = re.findall(pattern, user_input)
    links = {urlparse(url).geturl() for match in matches for url in match if url}
    if not links:
        return ''
    responses: list = []
    for link in links:
        res: str = _analyse(link)
        if res:
            responses.append(res)
    return '\n'.join(_ for _ in responses) if responses else ''
