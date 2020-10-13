import numpy as np


class ClusterFinder():
    def __init__(self, in_matrix):
        self.matrix = in_matrix*(-1)
        self.cluster_fields = None
        self.current_cluster_idx = 1

    def _get_neighbour_fields(self, field):
        neighbour_fields = []
        if field[0] - 1 >= 0:
            neighbour_fields.append((field[0] - 1, field[1]))
        if field[0] + 1 < self.matrix.shape[0]:
            neighbour_fields.append((field[0] + 1, field[1]))
        if field[1] - 1 >= 0:
            neighbour_fields.append((field[0], field[1] - 1))
        if field[1] + 1 < self.matrix.shape[1]:
            neighbour_fields.append((field[0], field[1] + 1))
        return neighbour_fields

    def _handle_cluster_field(self, field):
        self.matrix[field[0], field[1]] = self.current_cluster_idx
        neighbours = self._get_neighbour_fields(field)
        for neighbour_field in neighbours:
            if self.matrix[neighbour_field[0], neighbour_field[1]] < 0:
                self.cluster_fields.append(neighbour_field)

    def _fill_cluster_from_here(self, start_field):
        self.cluster_fields = [start_field]
        for field in self.cluster_fields:
            self._handle_cluster_field(field)

    def find_cluster(self):
        for i, j in np.ndindex(self.matrix.shape):
            field_must_be_added_to_cluster = (self.matrix[i, j] < 0)
            if field_must_be_added_to_cluster:
                self._fill_cluster_from_here((i, j))
                self.current_cluster_idx += 1
        return self.matrix


if __name__ == "__main__":
    in_matrix = np.matrix(
        [[1, 0, 0, 1, 1, 1],
         [0, 0, 0, 1, 0, 1],
         [1, 1, 0, 1, 1, 1],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 1, 0]],
        np.int32
    )

    clusterFinder = ClusterFinder(in_matrix)
    result_matrix = clusterFinder.find_cluster()
    print(result_matrix)
