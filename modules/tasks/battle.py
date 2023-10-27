from modules.module_battle.module_draw import module_click_draw, module_draw_verify, \
    module_draw_info


def battle(l=1, times=0, *args):
    module_click_draw()
    module_draw_verify()
    result = module_draw_info()
    return {
        'type': 3,
        'lists': l,
        'times': times,
        'result': result
    }
