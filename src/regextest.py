import re
text = 'There\'s a reason you get this matchmaking issue. We don\'t have email notification or people trying to hit random people every level there.\' A description'
print(re.match(r'(.*?)"', text).group(0))