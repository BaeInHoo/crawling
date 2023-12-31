import requests
from bs4 import BeautifulSoup

data2 = ['차1-1', '차1-2', '차1-3', '차1-4', '차1-5',
          '차2-1', '차2-2', '차2-3', '차2-4', '차2-5', '차2-6',
          '차3-1', '차3-2', '차3-3', '차3-4', '차3-5', '차3-6', '차3-7', '차3-8',
          '차4-1', '차4-2',
          '차5-1', '차5-2',
          '차6-1',
          '차7-1', '차7-2',
          '차8-1', '차8-2', '차8-3',
          '차9-1', '차9-2',
          '차10-1',
          '차11-1', '차11-2', '차11-3', '차11-4', '차11-5', '차11-6',
          '차12-1', '차12-2',
          '차13-1', '차13-2', '차13-3', '차13-4',
          '차14-1',
          '차15-1',
          '차16-1', '차16-2', '차16-3', '차16-4', '차16-5',
          '차17-1', '차17-2',
          '차18-1', '차18-2',
          '차19-1',
          '차20-1', '차20-2',
          '차21-1',
          '차31-1', '차31-2', '차31-3', '차31-4',
          '차32-1',
          '차33-1', '차33-2',
          '차41-1',
          '차42-1', '차42-2', '차42-3',
          '차43-1', '차43-2', '차43-3', '차43-4', '차43-5', '차43-6', '차43-7',
          '차44-1',
          '차45-1', '차45-2', '차45-3', '차45-4', '차45-5', '차45-6',
          '차46-1',
          '차47-1', '차47-2', '차47-3',
          '차48-1',
          '차51-1', '차51-2',
          '차52-1',
          '차53-1',
          '차54-1', '차54-2', '차54-3', '차54-4', '차54-5',
          '차55-1', '차55-2', '차55-3', '차55-4', '차55-5', '차55-6', '차55-7',
          '차61-1', '차61-2', '차61-3',
          '보1',
          '보2','보3','보4',
          '보5','보6','보7',
          '보8','보9','보10','보11','보12',
          '보13',
          '보14', '보15', '보16',
          '보17', '보18',
          '보19',
          '보20', '보21',
          '보22', '보23',
          '보24', '보25', '보26',
          '보27-1', '보27-2', '보28',
          '보29-1', '보29-2', '보30', '보31', '보32', '보33', '보34', '보35', '보36',
          '거1-1', '거1-2', '거1-3', '거1-4', '거1-5',
          '거2-1', '거2-2',
          '거3-1', '거3-2', '거3-3', '거3-4',
          '거4-1', '거4-2', '거4-3', '거4-4',
          '거5-1', '거5-2', '거5-3', '거5-4',
          '거6-1', '거6-2', '거6-3', '거6-4',
          '거7-1', '거7-2', '거7-3', '거7-4', '거7-5', '거7-6',
          '거8-1', '거8-2',
          '거9-1', '거9-2', '거9-3', '거9-4', '거9-5', '거9-6', '거9-7', '거9-8',
          '거10-1', '거10-2', '거10-3', '거10-4',
          '거21-1',
          '거31-1', '거31-2',
          '거32-1', '거32-2',
          '거33-1', '거33-2',
          '거41-1',
          '거42-1',
          '거43-1', '거43-2', '거43-3']

for item in data2:
  url2 = "https://accident.knia.or.kr/myaccident-content?chartNo="

  res = requests.get(url2 + item, verify=False)
  res.raise_for_status()
  soup = BeautifulSoup(res.text, "lxml")

  print("-----------[", item, "]------------")
  # id가 referprcdnt인 값 찾기
  data4 = soup.select("#referprcdnt")
  for item in data4:
    print(item.get_text())
