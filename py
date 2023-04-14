def calculate_averages(people):
    teams = {}
    for person in people:
        team = person['team']
        if team not in teams:
            teams[team] = {'statements': [], 'reasons': []}
        teams[team]['statements'].append(person['statements'])
        teams[team]['reasons'].append(person['reasons'])
    averages = []
    for team, data in teams.items():
        avg_statements = sum(data['statements']) / len(data['statements'])
        avg_reasons = sum(data['reasons']) / len(data['reasons'])
        averages.append((team, avg_statements, avg_reasons))
    averages.sort(key=lambda x: (x[1], x[2]))
    return averages

# Example usage
people = [
    {'name': 'Alice', 'user_id': 1, 'team': 'A', 'statements': 3, 'reasons': 2},
    {'name': 'Bob', 'user_id': 2, 'team': 'B', 'statements': 4, 'reasons': 1},
    {'name': 'Charlie', 'user_id': 3, 'team': 'A', 'statements': 2, 'reasons': 3},
    # ...
]

averages = calculate_averages(people)
for team, avg_statements, avg_reasons in averages:
    print(f'Team {team}: {avg_statements:.2f} statements, {avg_reasons:.2f} reasons')
