import requests
from pprint import pprint
from bs4 import BeautifulSoup
import csv


date = input("Enter date (mm/dd/yyyy): ")

page = requests.get(f"https://www.yallakora.com/match-center/?date={date}")

print(page.status_code)

def main(page):
    src = page.content
    
    soup = BeautifulSoup(src, 'lxml')
    match_details = []
    
    championchips = soup.find_all('div', {'class': 'matchCard'})
    def get_match_info(championchips):
        championchips_title = championchips.contents[1].find('h2').text.strip()
        all_matches = championchips.contents[3].find_all('div', {'class': 'item'})
        noOfMatches = len(all_matches)
        

        for i in range(noOfMatches):
            team_A = all_matches[i].find('div', {'class': 'teamA'}).text.strip()
            team_B = all_matches[i].find('div', {'class': 'teamB'}).text.strip()
            match_result = all_matches[i].find('div', {'class': 'MResult'}).find_all('span', {'class': 'score'})
            score = f"{match_result[0].text.strip()} - {match_result[1].text.strip()}"
            match_time = all_matches[i].find('div', {'class': 'MResult'}).find('span', {'class': 'time'}).text.strip()
           
            # add match infor to matches_details
            match_details.append({'نوع البطولة': championchips_title, 'الفريق الأول': team_A, 'الفريق الثاني': team_B,
                                  'ميعاد المبارة': match_time, 'النتيجة': score})
    
    for i in range(len(championchips)):
        get_match_info(championchips[i])

    keys = match_details[0].keys()

    with open('matches.csv', 'w', encoding="utf-8") as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(match_details)

main(page)