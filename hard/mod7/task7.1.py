import cProfile
from functions_to_profile import load_files, read_database, get_id, get_user_data, generate_words
import pstats

# Список названий функций, которые нужно профилировать в определенном порядке.
TASK_FUNCTIONS_ORDER = ['load_files', 'read_database', 'get_id', 'get_user_data', 'generate_words']

profile = cProfile.Profile()    # создается объект профилирования
profile.enable()                # метод включает профилирование

# цикл, в котором будут выполняться функции в порядке, указанном в TASK_FUNCTIONS_ORDER
for i in TASK_FUNCTIONS_ORDER:
	if i == "load_files":
		load_files()
	elif i == "read_database":
		read_database()
	elif i == "get_id":
		get_id()
	elif i == "get_user_data":
		get_user_data()
	elif i == "generate_words":
		generate_words()
		
profile.disable()               # метод отключает профилирование
profile.create_stats()          # создаются статистики профилирования

p = pstats.Stats(profile)       # создается объект p для анализа профилирования
p = p.get_stats_profile()       # метод возвращает информацию о профилировании для дальнейшего анализа

# цикл, в котором будет выводиться информация о времени выполнения и процентном соотношении каждой функции
for i in TASK_FUNCTIONS_ORDER:
    print(f"{p.func_profiles[i].cumtime:.4f}: {int(p.func_profiles[i].cumtime/p.total_tt*100)}%")
