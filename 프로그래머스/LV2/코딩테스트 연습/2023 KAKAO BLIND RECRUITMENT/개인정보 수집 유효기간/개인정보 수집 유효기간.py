def get_days(y, m, d):
    return y * 12 * 28 + m * 28 + d


def solution(today, terms, privacies):
    answer = []
    terms = [term.split(' ') for term in terms]
    terms_dic = {term[0] : int(term[1])*28 for term in terms}
    privacies = [privacie.split(' ') for privacie in privacies]
    privacies = [(list(map(int, privacy[0].split('.'))), privacy[1]) for privacy in privacies]

    today = list(map(int, today.split('.')))
    today_days = get_days(today[0], today[1], today[2])

    for i, v in enumerate(privacies):
        yms, term = v
        pdays = get_days(yms[0], yms[1], yms[2])
        if today_days - pdays >= terms_dic[term]:
            answer.append(i+1)
    return answer