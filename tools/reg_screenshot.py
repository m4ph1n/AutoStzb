from device.main import return_device
from path.img import path
from tools.reg_img_draw import fill_image


#  除传入的区域，其他一律涂黑
def general_screenshot_tools(area=(0, 0, 0, 0)):
    d = return_device()
    d.screenshot().save(path)
    fill_image(path, area)