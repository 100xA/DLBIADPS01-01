
def dp_activity_selection(activities):
    activities = sorted(activities, key=lambda x: x[1])
    n = len(activities)

    p = [-1] * n
    for j in range(n):
        for i in range(j - 1, -1, -1):
            if activities[i][1] <= activities[j][0]:
                p[j] = i
                break


    dp = [0] * n
    dp[0] = 1
    for j in range(1, n):
        include = 1 + (dp[p[j]] if p[j] != -1 else 0)
        exclude = dp[j - 1]
        dp[j] = max(include, exclude)
    
    return dp[-1]



if __name__ == "__main__":
    activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
    max_activities_dp = dp_activity_selection(activities)
    print("Maximum number of activities (DP):", max_activities_dp)
