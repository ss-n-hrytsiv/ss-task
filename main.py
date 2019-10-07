import task_87, task_226, task_559, task322, task88_v_g
from algo_tasks import task_num_107, task_num_243_a, task_num_243_b
from practics import task_88b, task_88a, task330


if __name__ == "__main__":
    print("Choose and write one from the task below")
    choice_task_dict = {
        "task_88a": task_88a,
        "task_88b": task_88b,
        "task_330": task330,
        "task_87": task_87.task_87,
        "task_226": task_226.task_226,
        "task_559": task_559.task_559,
        "task_322": task322.main,
        "task88_v_g": task88_v_g.main,
        "task_num_107": task_num_107,
        "task_num_243_a": task_num_243_a,
        "task_num_243_b": task_num_243_b
    }
    [print(x) for x in choice_task_dict.keys()]
    choice_task = input("Enter the name of tasks(ex. task_88a, ex. task_88b): ")
    choice_task = choice_task.lower()
    try:
        print(choice_task_dict[choice_task]())
    except KeyError as e:
        raise ValueError('Undefined unit: {}'.format(e.args[0]))