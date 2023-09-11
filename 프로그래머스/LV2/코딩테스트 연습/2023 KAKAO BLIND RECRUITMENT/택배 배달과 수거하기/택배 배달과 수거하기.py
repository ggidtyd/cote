def parcel_service(cap, parcels, n):
    idx = 0
    for i in range(n-1, -1, -1):
        if cap >= parcels[i]:
            cap -= parcels[i]
            parcels[i] = 0
        else:
            parcels[i] -= cap
            idx = i + 1
            break
    return idx


def solution(cap, n, deliveries, pickups):
    answer = 0

    while n > 0 and deliveries[-1] == 0 and pickups[-1] == 0:
        n -= 1

    delivery_idx, pickup_idx = n, n

    while n:
        delivery_idx = parcel_service(cap, deliveries, delivery_idx)
        pickup_idx = parcel_service(cap, pickups, pickup_idx)

        answer += n * 2

        n = max(delivery_idx, pickup_idx)

    return answer