def fight(robot_1, robot_2, tactics):
    robots = [robot_1, robot_2] if robot_1['speed'] >= robot_2['speed'] else [robot_2, robot_1]
    turn = 0
    while robot_1['health'] > 0 and robot_2['health'] > 0 and (robot_1['tactics'] or robot_2['tactics']):
        if robots[turn]['tactics']:
            robots[turn ^ 1]['health'] -= tactics[robots[turn]['tactics'].pop(0)]
        turn ^= 1
    if robot_1['health'] == robot_2['health']:
        return 'The fight was a draw.'
    return '{} has won the fight.'.format(robot_1['name'] if robot_1['health'] > robot_2['health'] else robot_2['name'])
