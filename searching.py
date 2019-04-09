def search_title(title):
    found_list = []
    keys = ['netflix', 'amazon prime', 'hulu']
    for i in keys:
        query = key[i] + title
        for j in googlesearch.search(query, tld="co.in", num=10, stop=1, pause=2):
            found_list.append(j)

    return(found_list[])
