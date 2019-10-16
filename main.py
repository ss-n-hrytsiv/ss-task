from tasks.task_88a_b import task88_a_b_menu
from tasks.task_86_b import task_86_b
from tasks.task_86_a import task86_a_b_menu
from tasks.task_330 import task_330_menu
from tasks.task178 import task178_menu
from tasks.task554 import task554_menu
from tasks.task332 import task332_menu
from tasks.task88vg import main
from tasks.task555 import task_555_menu
from tasks.task_87 import task_87_menu
from tasks.task_108 import task_108_menu
from tasks.task_226 import task_226_menu
from tasks.task_322 import task_322_menu
from tasks.task_331_a import task_331_a_menu
from tasks.task_331_b import task_331_b_menu
from tasks.task_num_107 import task_num_107
from tasks.task_num_243_b import task_num_243_b
from tasks.task_num_243_a import task_num_243_a
from tasks.task178_4 import task_178_4_menu
from tasks.task178_5 import task_178_5_menu
from tasks.task_559 import task_559_menu


if __name__ == "__main__":
    print("Choose and write one from the task below")
    choice_task_dict = {
        "task_86": task86_a_b_menu,
        "task_86_b": task_86_b,
        "task_330": task_330_menu,
        "task_108": task_108_menu,
        "task_88_vg": main,
        "task_178_4": task_178_4_menu,
        "task_178_5": task_178_5_menu,
        "task_178": task178_menu,
        "task_554": task554_menu,
        "task_559": task_559_menu,
        "task_332": task332_menu,
        "task_555": task_555_menu,
        "task_87": task_87_menu,
        "task_88": task88_a_b_menu,
        "task_226": task_226_menu,
        "task_322": task_322_menu,
        "task_331_a": task_331_a_menu,
        "task_331_b": task_331_b_menu,
        "task_num_107": task_num_107,
        "task_num_243_a": task_num_243_a,
        "task_num_243_b": task_num_243_b
    }
    [print(x) for x in choice_task_dict.keys()]
    choice_task = input("Enter the name of tasks(ex. task_88a, ex. task_88b): ")
    choice_task = choice_task.lower()
    try:
        choice_task_dict[choice_task]()
    except KeyError as e:
        raise ValueError('Undefined unit: {}'.format(e.args[0]))
    input()