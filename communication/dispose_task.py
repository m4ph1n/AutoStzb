from dispatcher.execute_type_1 import execute_type_1
from dispatcher.execute_type_2 import execute_type_2

from communication.task_store import add_store_data


async def dispose_task(websocket, task_config):
    from communication.comsumer import get_task
    if type(task_config) == int or type(task_config) == str:
        await websocket.send(get_task)
        return
    add_store_data(task_config['id'], task_config)
    if task_config['type'] == 1:
        execute_type_1(task_config)
    if task_config['type'] == 2:
        execute_type_2(task_config)
