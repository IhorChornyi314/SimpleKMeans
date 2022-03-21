points = [
    (1, 1), (1, 2), (2, 4), (3, 1), (3, 2), (5, 5), (6, 4), (6, 6), (6, 14), (7, 4), (7, 10),
    (7, 13), (7, 14), (7, 15), (8, 2), (8, 3), (8, 12), (9, 4)
]

n_clusters = 3
init_centroids = [(2, 2), (6, 7), (3, 15)]


def get_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def get_cluster_centroids(clusters):
    result = []

    for cluster, index in zip(clusters.values(), range(len(clusters))):
        centroid_x = 0
        centroid_y = 0
        for point in cluster:
            centroid_x += point[0] / len(cluster)
            centroid_y += point[1] / len(cluster)
        result.append((centroid_x, centroid_y))
        print('New centroid for cluster %d is (%.2f, %.2f)' % (index + 1, centroid_x, centroid_y))

    return result


def get_clusters(centroids):
    global points
    result = {c: [] for c in centroids}
    for point in points:
        closest_centroid = centroids[0]
        for centroid in centroids:
            if get_distance(point, centroid) < get_distance(point, closest_centroid):
                closest_centroid = centroid
        print(
            'Closest centroid for point p%d (%d, %d) is (%.2f, %.2f).' %
            (points.index(point) + 1, point[0], point[1], closest_centroid[0], closest_centroid[1]),
            'The distance is %.2f' % get_distance(point, closest_centroid)
        )
        result[closest_centroid].append(point)
    return result


def k_means():
    global points, init_centroids
    old_clusters = {}
    clusters = {c: [] for c in init_centroids}
    max_num = 10000
    while old_clusters != clusters and max_num > 0:
        old_clusters = clusters
        print('\nComputing clusters...')
        new_clusters = get_clusters(list(clusters.keys()))
        print('\nReevaluating centroids...')
        new_centroids = get_cluster_centroids(new_clusters)
        clusters = {c: p for c, p in zip(new_centroids, new_clusters.values())}
        print('\nNew clusters:')
        for cluster in clusters:
            print('(%.2f, %.2f):' % (cluster[0], cluster[1]), clusters[cluster])
        max_num -= 1
    print('\nNew cluster is the same as old one, end of algorithm.')


k_means()
