class Plugboard(object):
    def __init__(self, wires=''):
        """
        wires: This is the mapping of pairs of characters
        """
        self.plug_map = self.generate_plug_map(wires)

    def generate_plug_map(self, wires):
        if len(wires) > 20 or len(wires) % 2 or len(set(wires)) < len(wires):
            raise ValueError
        if not isinstance(wires, str):
            raise TypeError
        plug_map = dict()
        for i in range(0, len(wires)-1, 2):
            plug_map[wires[i]] = wires[i+1]
            plug_map[wires[i+1]] = wires[i]
        return plug_map

    def process(self, c):
        """
        c: The single character to process
        """
        return self.plug_map[c] if c in self.plug_map.keys() else c
