from bisect import bisect_left

def get_all_queries(src, src_idx, query, all_queries):  
    if src_idx == 4:
        all_queries[query] = []
        return 

    for v in src[src_idx]:
        get_all_queries(src, src_idx+1, query+v, all_queries)
        
def solution(info, query):
    ans = []
    all_queries = dict()
    src = [['cpp', 'java', 'python', '-'], ['frontend', 'backend', '-'], ['junior', 'senior', '-'], ['chicken', 'pizza', '-']]
    infos = [["".join(info[:-1]), int(info[-1])] for info in [data.split(' ') for data in info]]
    queries = [[query[0], int(query[1])] for query in [data.replace(" and ", '').split(" ") for data in query]]

    get_all_queries(src, 0, "", all_queries)

    for k in list(all_queries.keys()):
        for info in infos:
            for v in k.split('-'):
                if v not in info[0]:break
            else:all_queries[k].append(info[1])

    for k,_ in all_queries.items():
        all_queries[k].sort()
    
    for query in queries:
        ans.append(len(all_queries[query[0]]) - bisect_left(all_queries[query[0]], query[1]))
    return ans