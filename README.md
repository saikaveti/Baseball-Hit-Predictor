# Baseball-Linear-Classifier

The inspiration for this project can be found here: https://www.mlb.com/apps/beat-the-streak

# Getting Data Points
In order to get the data for this project, I pulled data from Fangraphs, Baseball Reference, as well as Statcast. I used the following API in order to do so:  https://github.com/jldbc/pybaseball

Once the data was obtained in the form of a BeautifulSoup table, I parsed through it, pulling data that I believed to be important for calculating this probability.

I decided on the following parameters:
....

I understand that the statistics are not alway independent of each other, but all are important baseball statistics.

I then pulled whether or not the player got a hit on the given day, allowing me to get all the data needed to (hopefully) learn the parameters accurately.

