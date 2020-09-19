import requests as req
import json
import time
from fake_useragent import UserAgent


def pars_www_olimp_bet(): #психованная функция парсинга
    NULL = 'NULL'

    def pars():
        day_start = ((time.time()*1000) // 86400000) * 86400000 + 75600000
        day = 86400000
        data = []
        session = req.Session()
        session.headers.update({'User-Agent': UserAgent().chrome})

        for i in range(6): #6 макс дней на перед вроде
            url = f'https://www.olimp.bet/apiru/prematch/calendar?from={int(day_start + day*i)}&to={int(day_start+day*(i+1)-1)}'
            r = session.get(url)
            data.append(r.json())
        return data

    def data_to_json():
        data = pars()
        ans = []
        for day in data:
            for sport in day:
                for champ in sport['champs']:
                    for event in champ['events']:
                        if len(event['name'].split('-')) == 1:
                            continue
                        temp = {
                            'url' : 'www.olimp.bet',
                            'time' : NULL,
                            'date' : event['start'], #millisecond since 1970
                            'champ_name' : champ['champName'],
                            'team_name_1' : event['name'].split('-')[0],
                            'team_name_2' : event['name'].split('-')[1],
                            'max_bet' : event['maxBet'],
                            'sport' : sport['sportName'],
                            'k_win_team_1' : NULL,
                            'k_win_team_2' : NULL,
                            'k_draw' : NULL,
                            'bet_type' : 'single bet',
                            'is_as' : False ,
                            'checked' : False,
                        }
                        for market in event['markets']: # добавление сортировок по ставкам (там их дофига) взял только победы и ничью
                            if (market['name'] == 'П1'):
                                temp['k_win_team_1'] = market['value']
                            if (market['name'] == 'П2'):
                                temp['k_win_team_2'] = market['value']
                            if (market['name'] == 'X'):
                                temp['k_win_team_1'] = market['value']
                        ans.append(temp)
        return ans

    return data_to_json()


if __name__ == '__main__':
    data = pars_www_olimp_bet()
    print('кол-во', len(data))
    print(json.dumps(data[100], indent=4, ensure_ascii=False))
    print('end')
