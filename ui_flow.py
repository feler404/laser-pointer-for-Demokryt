from m5stack import *
from m5stack_ui import *
from uiflow import *
import module

import network
import ntptime

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)

X_MIN = 90
X_MAX = 130
Y_MIN = 70
Y_MAX = 110
servo2 = module.get(module.SERVO2)

label_timer = M5Label('14:12:23', x=0, y=0, color=0x000, font=FONT_MONT_14, parent=None)
label_ip = M5Label('---', x=151, y=213, color=0x000, font=FONT_MONT_14, parent=None)
label_servo_y_value = M5Label('---', x=151, y=131, color=0x000, font=FONT_MONT_14, parent=None)
label_servo_x_value = M5Label('---', x=151, y=80, color=0x000, font=FONT_MONT_14, parent=None)
touch_button0 = M5Btn(text='ShowNetwork', x=100, y=160, w=120, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14,
                      parent=None)
line0 = M5Line(x1=0, y1=204, x2=320, y2=204, color=0x000, width=1, parent=None)
sliderX = M5Slider(x=10, y=54, w=300, h=12, min=X_MIN, max=X_MAX, bg_c=0xa0a0a0, color=0x08A2B0, parent=None)
sliderY = M5Slider(x=10, y=106, w=300, h=12, min=Y_MIN, max=Y_MAX, bg_c=0xa0a0a0, color=0x08A2B0, parent=None)


def sliderX_changed(value):
    sliderX.set_value(value)
    servo2.position(0, value)
    label_servo_x_value.set_text(str(value))
    pass


sliderX.changed(sliderX_changed)


def sliderY_changed(value):
    sliderY.set_value(value)
    servo2.position(2, value)
    label_servo_y_value.set_text(str(value))
    pass


sliderY.changed(sliderY_changed)


def touch_button0_pressed():
    global value
    label_ip.set_text(str(wlan.ifconfig()))
    pass


touch_button0.pressed(touch_button0_pressed)


def buttonA_wasPressed():
    global value
    pass


btnA.wasPressed(buttonA_wasPressed)


def buttonC_wasPressed():
    global value
    pass


btnC.wasPressed(buttonC_wasPressed)


def callback_timer3(_arg):
    global ntp, X_VALUE, Y_VALUE
    sliderX_changed(X_VALUE)
    sliderY_changed(Y_VALUE)
    print(ntp.formatTime(':'))
    label_timer.set_text(str(ntp.formatTime(':')))
    label_ip.set_text('---')
    pass


def main():
    global ntp, X_VALUE, Y_VALUE
    screen.set_screen_brightness(30)
    wlan = network.WLAN(network.STA_IF)
    print(wlan.ifconfig())
    ntp = ntptime.client(host='us.pool.ntp.org', timezone=2)
    timerSch.timer.init(period=1000, mode=timerSch.timer.PERIODIC, callback=callback_timer3)
    label_timer.set_align(ALIGN_IN_TOP_LEFT, x=0, y=0, ref=screen.obj)
    print('Start')

    from udp_server import init_udp_server, spin_udp_server
    init_udp_server(X_VALUE=X_MIN, Y_VALUE=Y_MIN)
    spin_udp_server()