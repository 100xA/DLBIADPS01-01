def sort_by_end_time(activity):
    return activity[1]

def activity_selection_dp(activities):
    activities = sorted(activities, key=sort_by_end_time)
    length_activities = len(activities)

    dynamic_list = [1] * length_activities  
    for i in range(length_activities - 2, -1, -1):
        for j in range(i + 1, length_activities):
            if activities[i][1] <= activities[j][0]:
                dynamic_list[i] = max(dynamic_list[i], 1 + dynamic_list[j])

    return max(dynamic_list)



if __name__ == "__main__":
    activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
    max_activities_dp = activity_selection_dp(activities)
    print("Maximum number of activities (DP):", max_activities_dp)
