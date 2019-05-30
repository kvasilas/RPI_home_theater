import googlesearch

query = "amazon prime the tick"

for j in googlesearch.search(query, tld="co.in", num=10, stop=1, pause=2):
    print(j)
    print(type(j))

https://stackoverflow.com/questions/15561608/detecting-enter-on-a-qlineedit-or-qpushbutton
