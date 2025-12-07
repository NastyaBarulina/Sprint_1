# Изначальное время, которое было дано:
total_time = '1h 45m,360s,25m,30m 120s,2h 60s'

# Разделяем строку на части по запятой, получаюся отдельные элементы:
separated_time = total_time.split(',')

total_minutes = 0

for time in separated_time:
    # Разделяем элементы по пробелам
    time_parts = time.split()
    
    for separated_part in time_parts:
        if 'h' in separated_part:
            hours = int(separated_part.replace('h', ''))
            total_minutes += hours * 60
        elif 'm' in separated_part:
            minutes = int(separated_part.replace('m', ''))
            total_minutes += minutes
        elif 's' in separated_part:
            seconds = int(separated_part.replace('s', '')) // 60
            total_minutes += seconds

print(total_minutes)