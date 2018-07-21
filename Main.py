import datetime
from RetrieveData import *
from PlayerList import *
from WriteData import *


write_data_object = RetrieveData(datetime.datetime.now())

###print(read.list_of_dates())
print()

date = write_data_object.get_current_date_only()

write_data_object.write_batting_for_date("playerdatatable.txt")
write_data_object.write_batting_for_single_date("PlayerHitStat.txt")

playerlist = PlayerList("playerdatatable.txt", "PlayerHitStat.txt")

list = playerlist.prune_list()


for player in list:
	player.print_player()

print(len(list))
