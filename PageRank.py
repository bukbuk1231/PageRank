import PageRankPreProcess
import math

def pageRank():
    outbounds, inbounds = PageRankPreProcess.calculate_all_pages('outlink_maps')
    # print(inbounds, outbounds)

    init_rank = 1 / len(outbounds)
    ranks = {node : init_rank for node in outbounds.keys()}
    
    while True:
        # print(sorted(ranks.items(), key=lambda item: item[1], reverse=True))
        next_ranks = {}
        for node in outbounds.keys():
            rank = 0
            for inbound in inbounds[node]:
                rank += ranks[inbound] / outbounds[inbound]
            rank = rank * (1 - 0.2) + (0.2 / len(outbounds))
            next_ranks[node] = rank

        if ranks == next_ranks:
            break

        ranks = next_ranks
        

    ranks = sorted(ranks.items(), key=lambda item: item[1], reverse=True)
 
    print(ranks)

    sum = 0
    for v in ranks:
        sum += v[1]
    print(sum)

    return ranks

if __name__ == '__main__':
    pageRank()