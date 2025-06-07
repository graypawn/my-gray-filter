import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def get_url():
    url = "https://www.xn--h10bx0wsvp.net/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    link = soup.find('a', attrs={'aria-label': '북토끼 바로가기'})
    if link and link.has_attr('href'):
        # 절대 URL을 정리해서 https:// 부분 제거
        href = link['href']
        parsed = urlparse(href)
        # netloc + path 부분만 사용
        cleaned_url = parsed.netloc + parsed.path
        cleaned_url = cleaned_url.rstrip('/')
        return cleaned_url
    else:
        raise ValueError("aria-label='북토끼 바로가기'인 a 태그를 찾을 수 없습니다.")

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
