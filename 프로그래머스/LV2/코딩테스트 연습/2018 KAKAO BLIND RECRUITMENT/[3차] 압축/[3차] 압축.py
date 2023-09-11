def solution(msg):
    answer = []
    lzw = dict()
    index = 27
    msg_len = len(msg)
    max_len = 1
    w_pos, c_pos = 0, 0
    
    for i in range(ord('A'), ord('Z')+1):
        lzw[chr(i)] = i-64

    while w_pos < msg_len:
        for w_len in range(max_len, 0, -1):
            c_pos = w_pos+w_len
            w = msg[w_pos:c_pos]
            if w in lzw:
                answer.append(lzw[w])
                if c_pos >= msg_len:
                    w_pos = c_pos
                    break
                wc = w + msg[c_pos]
                lzw[wc] = index
                index += 1
                w_pos = c_pos
                if len(wc) > max_len:
                    max_len = len(wc)
                break
    return answer
