from tasks.task_88a_b import task88_a_b_menu
from tasks.task_86_b import task_86_b
from tasks.task_86_a import task_86_a
from tasks.task_330 import task330
from tasks.task178 import task178_menu
from tasks.task554 import task554_menu
from tasks.task332 import task332_menu
from tasks.task88vg import main
from tasks.task555 import get_pascal_triangle
from tasks.task_87 import task_87
from tasks.task_108 import task_108
from tasks.task_226 import task_226
from tasks.task_322 import task_322_menu
from tasks.task_331_a import task_331_a
from tasks.task_331_b import task_331_b
from tasks.task_num_107 import task_num_107
from tasks.task_num_243_b import task_num_243_b
from tasks.task_num_243_a import task_num_243_a
from tasks.task178_4 import get_elements_less_arithmetic_mean_of_its_neighbor
from tasks.task178_5 import get_elements_by_condition

if __name__ == "__main__":
    print("Choose and write one from the task below")
    choice_task_dict = {
        "task_86_a": task_86_a,
        "task_86_b": task_86_b,
        "task_330": task330,
        "task_108": task_108,
        "task_88_vg": main,
        "task_178_4": get_elements_less_arithmetic_mean_of_its_neighbor,
        "task_178_5": get_elements_by_condition,
        "task_178": task178_menu,
        "task_554": task554_menu,
        "task_332": task332_menu,
        "task_555": get_pascal_triangle,
        "task_87": task_87,
        "task_88": task88_a_b_menu,
        "task_226": task_226,
        "task_322": task_322_menu,
        "task_331_a": task_331_a,
        "task_331_b": task_331_b,
        "task_num_107": task_num_107,
        "task_num_243_a": task_num_243_a,
        "task_num_243_b": task_num_243_b
    }
    [print(x) for x in choice_task_dict.keys()]
    choice_task = input("Enter the name of tasks(ex. task_88a, ex. task_88b): ")
    choice_task = choice_task.lower()
    try:
        # choice_task_dict[choice_task]()
        print(choice_task_dict[choice_task]())
    except KeyError as e:
        raise ValueError('Undefined unit: {}'.format(e.args[0]))