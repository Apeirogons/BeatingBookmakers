import random

def extract_features_and_labels(split_line, p0 = 17, p1 = 18, odds_start = 23, n_odds=3):
    try:
        p0_win = float(split_line[p0]) > float(split_line[p1])
        if p0_win:
            p0_win = [1.0, 0.0]
        else:
            p0_win = [0.0, 1.0]

    except ValueError:
        return -1
    except IndexError:
        return -1

    offered_odds = []
    for z in range(n_odds):
        try:
            offered_odds.append([float(x) for x in split_line[odds_start + 2 * z:odds_start + 2 * z + 2]])
        except ValueError:
            pass

    try:
        offered_odds = offered_odds[0]
    except IndexError:
        return -1
    return offered_odds, p0_win

def augment(extracted):
    flipped_odds = [extracted[0][1] , extracted[0][0]]
    flipped_winner = [not extracted[1][0], not extracted[1][1]]
    return flipped_odds, flipped_winner

def pack_sample(pack, n=64):
    sampled = random.sample(pack, n)
    features = [z[0] for z in sampled]
    labels = [z[1] for z in sampled]
    return features, labels