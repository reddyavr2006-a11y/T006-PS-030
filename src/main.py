from loaders import load_subscribers

subscribers = load_subscribers("subscribers.csv")

print("Subscribers Loaded:", len(subscribers))

