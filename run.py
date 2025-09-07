import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def get_final_url(url: str) -> str:
    try:
        response = requests.get(url, allow_redirects=True, timeout=10)
        return response.url  # 최종적으로 이동한 URL 반환
    except requests.RequestException as e:
        return f"Error: {e}"

def get_url():
    return clean_url(get_final_url("https://jusocon.com/bbs/link.php?bo_table=nav3&wr_id=5&no=1"))

def clean_url(url):
    parsed = urlparse(url)

    # netloc + path 부분만 사용
    cleaned_url = parsed.netloc + parsed.path
    cleaned_url = cleaned_url.rstrip('/')
    return cleaned_url

def main():
    try:
        url = get_url()

        lines = [
            f"{url}##div[id*=\"-banner-\"] > div[class*=\" \"] > div[class*=\" \"][style*=\" \"]",
            f"{url}###hd_pop",
            f"{url}##img[src^=\"/tokinbtoki/\"]",
            f"{url}#?#ul[class] > li:has(> a[href*=\"tokkiweb.com\"])"
        ]

        with open('toki_filter.txt', 'w', encoding='utf-8') as f:
            for line in lines:
                f.write(line + "\n")

        print("toki_filter.txt 파일이 성공적으로 생성되었습니다.")
    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    main()
