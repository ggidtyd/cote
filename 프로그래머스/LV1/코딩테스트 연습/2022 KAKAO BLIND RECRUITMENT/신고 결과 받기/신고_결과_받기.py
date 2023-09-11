def solution(id_list, report, k):
    answer = [0]*len(id_list)
    report_type = set(report)

    id_report_num_dict = {id : 0 for id in id_list}
    
    for st in report_type:
        id_report_num_dict[st.split(" ")[1]] += 1
    
    for st in report_type:
        if id_report_num_dict[st.split(" ")[1]] >= k:
            answer[id_list.index(st.split(" ")[0])] += 1
        
    return answer