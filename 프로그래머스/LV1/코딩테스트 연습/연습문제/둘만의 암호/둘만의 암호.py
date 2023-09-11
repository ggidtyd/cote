def solution(s, skip, index):
    answer = ""
    except_skip = []
    for i in range(ord('a'), ord('z')+1):
        if chr(i) in skip:
            continue
        except_skip.append(chr(i))

    except_skip = except_skip
    except_skip_len = len(except_skip)
    
    except_skip_idx_dic = dict()
    for i in range(except_skip_len):
        except_skip_idx_dic[except_skip[i]] = i
        
    for c in s:
        new_idx = (except_skip_idx_dic[c] + index) % except_skip_len
        answer += except_skip[new_idx]

    return answer