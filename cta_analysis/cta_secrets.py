with open("cta_analysis/bus_api_key.txt", "r") as f:
    BUS_API_KEY = f.readline().rstrip()

with open("cta_analysis/train_api_key.txt", "r") as f:
    TRAIN_API_KEY = f.readline().rstrip()
