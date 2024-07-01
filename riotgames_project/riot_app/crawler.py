import requests
from bs4 import BeautifulSoup

def crawl_schedule():
    url = 'https://game.naver.com/esports/League_of_Legends/schedule/lck'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    # 경기 정보를 담고 있는 카드들을 선택
    match_cards = soup.find_all('div', class_='card_date__1kdC3')
    print(f"Found {len(match_cards)} match cards.")

    if not match_cards:
        print("No matches found. Please check the selectors.")
    else:
        for match in match_cards:
            try:
                # 날짜
                match_date = match.text.strip()
                print(f"Match Date: {match_date}")

                # 시간
                match_time_tag = match.find_next('span', class_='row_time__28bwr')
                match_time = match_time_tag.text.strip() if match_time_tag else 'N/A'
                print(f"Match Time: {match_time}")

                # 팀 A 이름 및 로고
                team_a_name_tag = match.find_next('span', class_='row_name__IDFHz')
                team_a_name = team_a_name_tag.text.strip() if team_a_name_tag else 'N/A'
                team_a_logo_tag = team_a_name_tag.find_previous('img', class_='row_logo__c8gh0')
                team_a_logo = team_a_logo_tag['src'] if team_a_logo_tag else 'N/A'
                print(f"Team A: {team_a_name}, Logo: {team_a_logo}")

                # 팀 B 이름 및 로고
                team_b_name_tag = team_a_name_tag.find_next('span', class_='row_name__IDFHz')
                team_b_name = team_b_name_tag.text.strip() if team_b_name_tag else 'N/A'
                team_b_logo_tag = team_b_name_tag.find_previous('img', class_='row_logo__c8gh0')
                team_b_logo = team_b_logo_tag['src'] if team_b_logo_tag else 'N/A'
                print(f"Team B: {team_b_name}, Logo: {team_b_logo}")

                # VS 이미지
                vs_image_tag = match.find_next('path', {'d': "M8.28 11L11.72.62H7.68L6.04 6.94H6L4.38.62H.2L3.6 11h4.68zm8.92.26c.68 0 1.33-.06 1.95-.18a5.77 5.77 0 001.68-.59c.5-.273.9-.653 1.2-1.14.3-.487.45-1.07.45-1.75 0-.787-.223-1.407-.67-1.86-.447-.453-1.05-.8-1.81-1.04-.467-.16-1.167-.32-2.1-.48-.72-.133-1.18-.24-1.38-.32a1.445 1.445 0 01-.33-.22.414.414 0 01-.13-.32c0-.307.113-.517.34-.63.227-.113.513-.17.86-.17s.64.1.88.3c.293.2.447.46.46.78h3.6c-.027-.627-.19-1.157-.49-1.59-.3-.433-.693-.773-1.18-1.02S19.517.61 18.95.51c-.567-.1-1.163-.15-1.79-.15-.56 0-1.127.053-1.7.16-.573.107-1.1.283-1.58.53-.48.247-.87.587-1.17 1.02-.3.433-.45.963-.45 1.59 0 .893.33 1.597.99 2.11.66.513 1.743.897 3.25 1.15.92.16 1.513.307 1.78.44.267.133.4.353.4.66 0 .267-.143.467-.43.6-.287.133-.59.2-.91.2-.48 0-.833-.1-1.06-.3-.293-.267-.453-.573-.48-.92h-3.78c.013.64.17 1.197.47 1.67.3.473.697.857 1.19 1.15.493.293 1.043.507 1.65.64s1.23.2 1.87.2z"})
                vs_image = vs_image_tag['d'] if vs_image_tag else 'N/A'
                print(f"VS Image: {vs_image}")

                # 데이터베이스 저장 로직
                # Match.objects.update_or_create(
                #     team_a_name=team_a_name,
                #     team_b_name=team_b_name,
                #     match_date=match_date,
                #     match_time=match_time,
                #     defaults={
                #         'team_a_logo': team_a_logo,
                #         'team_b_logo': team_b_logo,
                #         'vs_image': vs_image
                #     }
                # )

            except Exception as e:
                print(f"Error processing match: {e}")

if __name__ == "__main__":
    crawl_schedule()
