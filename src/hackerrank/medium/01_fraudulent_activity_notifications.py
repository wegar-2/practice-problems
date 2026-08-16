# problem: https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem

from collections import deque


def _calculate_median(exp_dict: dict[int, int], d: int):
    cum_sum = []
    for i, (k, v) in enumerate(exp_dict.items()):
        if i == 0:
            cum_sum.append(v)
        else:
            cum_sum.append(v + cum_sum[-1])

    if d % 2 == 1:
        s = next((x for x in cum_sum if x >= d // 2 + 1))
        return cum_sum.index(s)
    s_l, s_r = (
        next((x for x in cum_sum if x >= d // 2)),
        next((x for x in cum_sum if x >= d // 2 + 1))
    )
    return 0.5 * (cum_sum.index(s_l) + cum_sum.index(s_r))



def activity_notifications(
        expenditure: list[int],
        d: int
):
    exp_dict: dict[int, int] = {e: 0 for e in range(0, 200)}
    notif_count: int = 0
    data: deque[int] = deque()

    for i, x in enumerate(expenditure):
        if i <= d-1:
            data.append(x)
            exp_dict[x] += 1
        else:
            if x >= 2*_calculate_median(exp_dict, d):
                notif_count += 1
            exp_dict[data.popleft()] -= 1
            data.append(x)
            exp_dict[x] += 1
    return notif_count


if __name__ == "__main__":
    # activity_notifications(
    #     expenditure=[1, 2, 3, 4, 4],
    #     d=4
    # )
    activity_notifications(
        expenditure=[10, 20, 30, 40,50],
        d=3
    )