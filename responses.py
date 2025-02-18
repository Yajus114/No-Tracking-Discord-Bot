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
    links = {_analyse(urlparse(url).geturl()) for match in matches for url in match if url}
    return '\n'.join(f"<{link}>" for link in links) if links else ''
