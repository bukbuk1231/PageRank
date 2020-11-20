import PageRankPreProcess
import math

def pageRank():
    outbounds, inbounds = PageRankPreProcess.calculate_all_pages('testcsv2')

    init_rank = 1 / len(outbounds)
    ranks = {node : init_rank for node in outbounds.keys()}
    
    while True:
        next_ranks = {}
        for node in outbounds.keys():
            rank = 0
            for inbound in inbounds[node]:
                rank += ranks[inbound] / outbounds[inbound]
            next_ranks[node] = rank
        
        isclose = True
        for key in ranks.keys():
            isclose &= math.isclose(ranks[key], next_ranks[key], abs_tol=1e-15)

        if isclose:
            break

        ranks = next_ranks

    ranks = sorted(ranks.items(), key=lambda item: item[1], reverse=True)
    
    print(ranks)
    return ranks

if __name__ == '__main__':
    pageRank()