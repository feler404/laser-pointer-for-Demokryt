from m5stack import *
from m5stack_ui import *
from uiflow import *
import network
import ntptime


screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)






label_timer = M5Label('14:12:23', x=0, y=0, color=0x000, font=FONT_MONT_14, parent=None)
label_ip = M5Label('---', x=151, y=177, color=0x000, font=FONT_MONT_14, parent=None)
label0 = M5Label('---', x=295, y=0, color=0x000, font=FONT_MONT_14, parent=None)
label_button_1 = M5Label('---', x=240, y=217, color=0x000, font=FONT_MONT_14, parent=None)
touch_button0 = M5Btn(text='ShowNetwork', x=100, y=141, w=120, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
line0 = M5Line(x1=0, y1=204, x2=320, y2=204, color=0x000, width=1, parent=None)

def touch_button0_pressed():
  # global params
  label_ip.set_text(str(wlan.ifconfig()))
  pass
touch_button0.pressed(touch_button0_pressed)

def buttonA_wasPressed():
  # global params
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonC_wasPressed():
  # global params
  pass
btnC.wasPressed(buttonC_wasPressed)

def callback_timer3(_arg):
  # global params
  print(ntp.formatTime(':'))
  label_timer.set_text(str(ntp.formatTime(':')))
  label_ip.set_text('---')
  pass


screen.set_screen_brightness(30)
wlan = network.WLAN(network.STA_IF)
print(wlan.ifconfig())
ntp = ntptime.client(host='us.pool.ntp.org', timezone=2)
timerSch.timer.init(period=1000, mode=timerSch.timer.PERIODIC, callback=callback_timer3)
label_timer.set_align(ALIGN_IN_TOP_LEFT, x=0, y=0, ref=screen.obj)
print('Start')