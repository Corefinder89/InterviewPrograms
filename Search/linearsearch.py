class linSearch():
    def linear_search(self, values, searchFor):
        search_at = 0
        search_res = False
        pos = 0

        while search_at < len(values) and search_res is False:
            if values[search_at] == searchFor:
                search_res = pos
                print(str(pos))
                break
            else:
                search_at = search_at + 1

            pos = pos + 1

        if search_res is False:
            print("Element not found")

l=[64,34,25,12,22,11,90]
lsearch = linSearch()
lsearch.linear_search(l,500)
