def solve(arrival_times, threshold):
    if len([x for x in arrival_times if x <= 0]) >= threshold:
        return "SIM"
    else:
        return "NÃO"