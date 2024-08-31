from m5stack import *
from m5stack_ui import *
from uiflow import *
import module
import network
import ntptime
import wifiCfg


from init_config import STATE, Logger

NTP_SERVER = 'us.pool.ntp.org'
TIME_ZONE = 2
screen_light_mode = 30
log_list = ["---", "---", "---"]
servo2 = module.get(module.SERVO2)

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)

X_MIN = STATE['X_POINT'].min
X_MAX = STATE['X_POINT'].max
Y_MIN = STATE['Y_POINT'].min
Y_MAX = STATE['Y_POINT'].max

label_timer = M5Label('14:12:23', x=0, y=0, color=0x000, font=FONT_MONT_14, parent=None)
label_ip = M5Label('---', x=0, y=0, color=0x000, font=FONT_MONT_14, parent=None)
label_log_0 = M5Label('---', x=0, y=218, color=0x000, font=FONT_MONT_14, parent=None)
label_log_1 = M5Label('---', x=0, y=202, color=0x000, font=FONT_MONT_14, parent=None)
label_log_2 = M5Label('---', x=0, y=186, color=0x000, font=FONT_MONT_14, parent=None)
label_servo_y_value = M5Label('---', x=151, y=131, color=0x000, font=FONT_MONT_14, parent=None)
label_servo_x_value = M5Label('---', x=151, y=80, color=0x000, font=FONT_MONT_14, parent=None)
button_switch_light = M5Btn(text='L', x=300, y=0, w=20, h=20, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
line0 = M5Line(x1=0, y1=180, x2=320, y2=180, color=0x000, width=1, parent=None)
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


def callback_lcd_clock(_arg):
    global ntp
    # label_timer.set_text(str(ntp.formatDatetime('-', ':')))
    label_timer.set_text(str(ntp.formatTime(':')))


def sync_ntp(_arg):
    global ntp
    pass


def button_switch_light_pressed():
    global screen_light_mode
    if screen_light_mode == 30:
        button_switch_light.set_bg_color(0x999999)
        screen_light_mode = 100
    else:
        button_switch_light.set_bg_color(0xFFFFFF)
        screen_light_mode = 30
    screen.set_screen_brightness(screen_light_mode)


screen.set_screen_brightness(screen_light_mode)
wifiCfg.doConnect(STATE['WIFI_SID'], STATE['WIFI_PASS'])

wlan = network.WLAN(network.STA_IF)
ntp = ntptime.client(host=NTP_SERVER, timezone=TIME_ZONE)
timerSch.timer.init(period=1000, mode=timerSch.timer.PERIODIC, callback=callback_lcd_clock)
label_timer.set_align(ALIGN_IN_TOP_LEFT, x=0, y=0, ref=screen.obj)
label_ip.set_align(ALIGN_IN_TOP_MID, x=30, y=0, ref=screen.obj)
label_ip.set_text("IP: " + str(wlan.ifconfig())[2:15])
label_log_0.set_long_mode(3)
label_log_0.set_size(w=320)
label_log_1.set_long_mode(3)
label_log_1.set_size(w=320)
label_log_2.set_long_mode(3)
label_log_2.set_size(w=320)
sliderX_changed(STATE['X_POINT'].value)
sliderY_changed(STATE['Y_POINT'].value)
button_switch_light.pressed(button_switch_light_pressed)


def screen_log(msg):
    global log_list
    log_list.insert(0, msg)
    log_list = log_list[:3]
    label_log_0.set_text(log_list[0])
    label_log_1.set_text(log_list[1])
    label_log_2.set_text(log_list[2])


lcd_logger = Logger(time_nf=ntp.formatTime, log_nf=screen_log)
