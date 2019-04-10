import googlesearch

def search_title(title):
    found_list = []
    keys = [' netflix', ' amazon prime', ' hulu', ' crackle']
    for x in range(len(keys)):
        query = keys[x] + title
        for j in googlesearch.search(query, tld="co.in", num=10, stop=1, pause=2):
            found_list.append(j)
    print(found_list)
    search_keys = ['www.netflix.com/title', 'www.amazon.com/', 'www.hulu', 'www.sonycrackle']
    final_list = []
    for i in range(len(keys)):
        if(search_keys[i] in found_list[i]):
            final_list.append(found_list[i])
    return(final_list)
