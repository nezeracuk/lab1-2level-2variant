def minimum_types_of_beer(N, B, workers_preferences):
    beer_preference_sets = [set() for _ in range(B)]
    visited_workers = set()
    min_beer_count = 0

    for worker_id, preference in enumerate(workers_preferences):
        for beer_type_id, has_preference in enumerate(preference):
            if has_preference == 'Y':
                beer_preference_sets[beer_type_id].add(worker_id)


    for beer_lovers in sorted(beer_preference_sets, key=len, reverse=True):
        if not beer_lovers <= visited_workers:
            min_beer_count = min_beer_count + 1
            visited_workers.update(beer_lovers)
            if len(visited_workers) == N:
                break

    return min_beer_count
