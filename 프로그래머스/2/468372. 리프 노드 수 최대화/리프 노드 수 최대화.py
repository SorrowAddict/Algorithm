def solution(dist_limit, split_limit):
    ans = 1

    pow2 = [1]
    while pow2[-1] * 2 <= split_limit:
        pow2.append(pow2[-1] * 2)

    pow3 = [1]
    while pow3[-1] * 3 <= split_limit:
        pow3.append(pow3[-1] * 3)

    for i in range(len(pow2)):
        for j in range(len(pow3)):
            if pow2[i] * pow3[j] > split_limit:
                break

            budget = dist_limit
            frontier = 1

            # 2-블록
            ok = True
            for _ in range(i):
                if budget >= frontier:
                    budget -= frontier
                    frontier *= 2
                else:
                    ans = max(ans, frontier + budget)
                    ok = False
                    break
            if not ok:
                continue

            # 3-블록
            for _ in range(j):
                if budget >= frontier:
                    budget -= frontier
                    frontier *= 3
                else:
                    ans = max(ans, frontier + budget * 2)
                    ok = False
                    break
            if not ok:
                continue

            ans = max(ans, frontier)

    return ans