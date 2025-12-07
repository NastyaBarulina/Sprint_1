new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']

# Перенос task_005
completed_tasks.append(new_tasks.pop())
#print(new_tasks)
#print(completed_tasks)

# Убрали задачу task_007
new_tasks.remove('task_007')
#print(new_tasks)

# Получаем последнюю задачу из списка new_tasks и выводим её
last_task_in_new_tasks = new_tasks[-1]
print(last_task_in_new_tasks)
#print(new_tasks[-1])