from browser_history import get_history

outputs = get_history()

# his is a list of (datetime.datetime, url) tuples
his = outputs.histories
for h in his:
    print(h[1])
