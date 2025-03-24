def sort_by_end_time(activity):
    return activity[1]

def greedy_activity_selection(activities):
    sorted_activities = sorted(activities, key=sort_by_end_time)
    selected = []
    last_end_time = 0 

    for activity in sorted_activities:
        start, end = activity
        if start >= last_end_time:
            selected.append(activity)
            last_end_time = end

    return selected

if __name__ == "__main__":
    activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
    selected_activities = greedy_activity_selection(activities)
    print("Greedy selected activities:", selected_activities)
