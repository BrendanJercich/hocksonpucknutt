# hocksonpucknutt
A generator for random hockey player names.

# Data source
I scraped my list of NHL player names from [HockeyDB](https://www.hockeydb.com/) and used BeautifulSoup to turn their tables into name lists. Then I broke those names into chunks in a very naive way (because using PyHyphen for the purpose didn't work very well). If you want to update that list for your purposes, download the relevant files and put them in `scrape`, then run `hockson.py`. That will give you something like the four text files in this repo.

# Data generation
The other script, `pucknutt.py`, takes those files and mashes them together, then spits out twenty combinations. You don't need the source data to use this script, it just parses the local name chunk text files. Some players have longer or shorter names and some will have nicknames as well, eg:

```
Mikalyn Boynlej
Gumpydn Laframwoit
Son Seifrion
Kea Djotatiokin
Came "Heal" Bourglows
Sea Behllsen
Uvis Trocnna
Parenic Bremgworth
Ollimer Labranyshyn
Vale Dingrou
```

# That's all
You can see a new list of names every hour [on my tilde.club page](https://tilde.club/~brendn/players.html).