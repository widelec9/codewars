class Blobservation:
    def __init__(self, h, w=0):
        self.h = h
        self.w = w if w else h
        self.blobs = []

    def _merge_dup_blobs(self):
        blobs_trunc = [tuple(b[:2]) for b in self.blobs]
        dup_counter = {k: blobs_trunc.count(k) for k in blobs_trunc}
        if len(dup_counter.values()) != list(dup_counter.values()).count(1):
            dups = {}
            for item in [i for i in dup_counter if dup_counter[i] != 1]:
                dups[item] = [i for i, j in enumerate(blobs_trunc) if j == item]
            rem = []
            for dup, pos in dups.items():
                while len(pos) > 1:
                    self.blobs[pos[-2]][2] += self.blobs[pos[-1]][2]
                    rem += [dups[dup].pop()]
            self.blobs = [b for i, b in enumerate(self.blobs) if i not in rem]

    def populate(self, gen):
        for blob in gen:
            if type(blob) != dict or type(blob['x']) == bool or type(blob['y']) == bool or type(blob['size']) == bool or None in blob.values():
                raise TypeError
            elif blob['x'] < 0 or blob['x'] > self.h - 1 or blob['y'] < 0 or blob['y'] > self.w - 1 or blob['size'] < 0:
                raise ValueError
        for blob in gen:
            self.blobs += [[blob['x'], blob['y'], blob['size']]]
        self._merge_dup_blobs()

    def _get_sign(self, x):
        if x == 0:
            return 0
        return (-1, 1)[x > 0]

    def _get_target(self, blob):
        # Add calculated distances
        potential_targets = [b + [max(abs(b[0]-blob[0]), abs(b[1]-blob[1]))] for b in self.blobs if b[2] < blob[2]]
        # If multiple targets are at the same movement distance, the blob with the largest size is focused
        min_dist = min([b[3] for b in potential_targets])
        check_dist = [b for b in potential_targets if b[3] == min_dist]
        if len(check_dist) > 1:
            # If there are multiple targets that have both the largest size and shortest movement distance, priority is set in clockwise rotation, starting from the 12 position
            max_size = max([b[2] for b in check_dist])
            check_size = [b for b in check_dist if b[2] == max_size]
            if len(check_size) > 1:
                potential_targets = sorted(check_size, key=lambda target: ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)).index((self._get_sign(target[0]-blob[0]), self._get_sign(target[1]-blob[1]))))
            else:
                potential_targets = sorted(check_dist, key=lambda x: x[2], reverse=True)
        else:
            potential_targets = sorted(potential_targets, key=lambda x: x[3])
        return potential_targets[0]

    def move(self, n=1):
        if type(n) == bool or n < 1:
            raise ValueError
        if len(self.blobs) == 0:
            return
        else:
            for i in range(n):
                min_size = min([b[2] for b in self.blobs])
                blobs_greater_than_min_size = [b for b in self.blobs.copy() if b[2] > min_size]
                blobs_targets = [[blob, self._get_target(blob)] for blob in blobs_greater_than_min_size]
                for bt in blobs_targets:
                    move_dir = (self._get_sign(bt[1][0]-bt[0][0]), self._get_sign(bt[1][1]-bt[0][1]))
                    idx_blob = self.blobs.index(bt[0])
                    self.blobs[idx_blob][0] += move_dir[0]
                    self.blobs[idx_blob][1] += move_dir[1]
                self._merge_dup_blobs()

    def print_state(self):
        return sorted(self.blobs)