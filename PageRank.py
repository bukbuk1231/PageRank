import PageRankPreProcess
import math

def pageRank():
    outbounds, inbounds = PageRankPreProcess.calculate_all_pages('outlink_maps')

    init_rank = 1 / len(outbounds)
    ranks = {node : init_rank for node in outbounds.keys()}
    
    while True:
        next_ranks = {}
        for node in outbounds.keys():
            rank = 0
            for inbound in inbounds[node]:
                rank += ranks[inbound] / outbounds[inbound]
            rank = rank * (1 - 0.2) + (0.2 / len(outbounds))
            next_ranks[node] = rank

        similar = True
        for key in ranks.keys():
            similar &= math.isclose(ranks[key], next_ranks[key], rel_tol=1e-15)

        if similar:
            break

        ranks = next_ranks
        

    ranks = sorted(ranks.items(), key=lambda item: item[1], reverse=True)

    return ranks

if __name__ == '__main__':
    pageRank()