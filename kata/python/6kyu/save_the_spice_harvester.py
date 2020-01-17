def harvester_rescue(data):
    carryall_dist = ((data['carryall'][0][0] - data['harvester'][0]) ** 2 + (data['carryall'][0][1] - data['harvester'][1]) ** 2) ** 0.5
    worm_dist = ((data['worm'][0][0] - data['harvester'][0]) ** 2 + (data['worm'][0][1] - data['harvester'][1]) ** 2) ** 0.5
    return "The spice must flow! Rescue the harvester!" if (carryall_dist / data['carryall'][1]) + 1 < worm_dist / data['worm'][1] \
        else "Damn the spice! I'll rescue the miners!"
