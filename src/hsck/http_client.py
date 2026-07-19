import httpx
from hsck.logger import get_logger

logger = get_logger(__name__)

class HttpClient:
    USER_AGENT = (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/125.0.0.0 Safari/537.36"
    )

    def __init__(self):
        self.client = httpx.Client(
            verify=False,
            headers={"User-Agent": self.USER_AGENT},
        )

    def get(self, url: str, **kwargs) -> httpx.Response:
        kwargs.setdefault("timeout", 30)
        return self.client.get(url, **kwargs)

    def get_html(self, url: str) -> str:
        try:
            response = self.get(url)
            response.encoding = "utf-8"
            return response.text
        except Exception as e:
            logger.error(f"获取 {url} 失败: {e}")
            return ""

    def head(self, url: str, allow_redirects: bool = False, **kwargs) -> httpx.Response:
        kwargs.setdefault("timeout", 30)
        return self.client.head(url, follow_redirects=allow_redirects, **kwargs)

    @property
    def cookies(self) -> dict[str, str]:
        return dict(self.client.cookies)
