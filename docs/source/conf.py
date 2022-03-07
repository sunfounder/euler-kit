# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import sphinx_rtd_theme

# -- Project information -----------------------------------------------------

project = 'SunFounder Euler Kit for Raspberry Pi Pico'
copyright = '2021, SunFounder'
author = 'Jimmy, SunFounder'

# The full version, including alpha/beta/rc tags
release = '1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autosectionlabel']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

from recommonmark.parser import CommonMarkParser
source_parsers = {
    '.md': CommonMarkParser,
}
source_suffix = ['.rst', '.md']

html_js_files = [
    'https://ezblock.cc/readDocFile/topHead.js',
]
html_css_files = [
    'https://ezblock.cc/readDocFile/topHead.css',
]


# new
rst_epilog = """
.. |img_take_color| image:: /img/edit_colors.png
.. |img_keypad_pressed| image:: /img/keypad_pressed.png
"""

# component pic
rst_epilog += """

.. |euler_list| image:: /img/component/euler_list.png
    :width: 800
.. |img_buzzer| image:: /img/component/buzzer.png
    :width: 600
.. |img_rgb_pin| image:: /img/component/rgb_pin.jpg
    :width: 200
.. |img_buzzer_symbol| image:: /img/component/buzzer_symbol.png
.. |img_7seg| image:: /img/component/7_segment.png
.. |img_7seg_cathode| image:: /img/component/segment_cathode.png
.. |img_74hc595| image:: /img/component/74HC595.png
.. |img_74jc595_1| image:: /img/component/74hc595_1.png
.. |img_74jc595_pin| image:: /img/component/74hc595_pin.png
.. |img_bb| image:: /img/component/breadboard.png
.. |img_bbi| image:: /img/component/breadboard_internal.png
.. |img_button| image:: /img/component/button.png
.. |img_button_symbol| image:: /img/component/button_symbol.png
.. |img_button2| image:: /img/component/button2.jpg
.. |img_4-digit-sche| image:: /img/component/4-digit-sche.png
.. |img_4-digit-sche-ca| image:: /img/component/4-digit-sche-ca.png
.. |img_788bs_i| image:: /img/component/image84.png
.. |img_788bs_sche| image:: /img/component/image85.png
.. |img_capacitor| image:: /img/component/capacitor.png
.. |img_103_capacitor| image:: /img/component/103_capacitor.png
.. |img_dc_motor_sche| image:: /img/component/motor_sche.png
.. |img_max7219| image:: /img/component/max7219_sche.png
.. |img_encoder| image:: /img/component/encoder205.jpeg
.. |img_encoder_timing| image:: /img/component/encoder206.png
.. |img_Hum-sch| image:: /img/component/Hum-sch.png
.. |img_Dht11| image:: /img/component/Dht11.png
.. |img_joystick| image:: /img/component/joystick318.png
.. |img_keypad| image:: /img/component/keypad314.png
.. |img_l293d1| image:: /img/component/l293d111.png
.. |img_l293d2| image:: /img/component/l293d334.png
.. |img_mpr121| image:: /img/component/mpr121200.jpeg
    :width: 600
.. |img_mpu6050_a| image:: /img/component/mpu223.png
.. |img_mpu6050_a2| image:: /img/component/mpu224.png
.. |img_mpu6050_g| image:: /img/component/mpu225.png
.. |img_reed_sche| image:: /img/component/reed.png
.. |img_relay_sche| image:: /img/component/relay142.jpeg
.. |img_stepper| image:: /img/component/stepper129.png
.. |img_stepper_timing| image:: /img/component/stepper130.png
.. |img_touch| image:: /img/component/touch168.png
.. |img_touch_sche| image:: /img/component/touch169.jpeg
.. |img_uln2003_sche| image:: /img/component/uln338.png
.. |img_uln2003| image:: /img/component/uln132.png
.. |img_ultrasonic| image:: /img/component/ultrasonic217.png
.. |img_ultrasonic_timing| image:: /img/component/ultrasonic228.png
.. |img_i2c_lcd| image:: /img/component/i2c_lcd1602.png
.. |img_led| image:: /img/component/LED.png
.. |img_led_symbol| image:: /img/component/led_symbol.png
.. |img_photoresistor| image:: /img/component/photoresistor.png
.. |img_photoresistor_symbol| image:: /img/component/photoresistor_symbol.png
.. |img_pir| image:: /img/component/pir.png
.. |img_PIR_working_principle| image:: /img/component/PIR_working_principle.jpg
.. |img_pir_back| image:: /img/component/pir_back.png
.. |img_pot| image:: /img/component/potentiometer.png
.. |img_pot_symbol| image:: /img/component/potentiometer_symbol.png
.. |img_res| image:: /img/component/resistor.png
.. |img_res_symbol| image:: /img/component/resistor_symbol.png
.. |img_res_card| image:: /img/component/resistance_card.jpg
.. |img_220ohm| image:: /img/component/220ohm.jpg
.. |img_rgb| image:: /img/component/rgb_led.png
.. |img_rgb_light| image:: /img/component/rgb_light.png
.. |img_rgb_symbol| image:: /img/component/rgb_symbol.png
.. |img_servo| image:: /img/component/servo.png
.. |img_servo_i| image:: /img/component/servo_internal.png
.. |img_servo_duty| image:: /img/component/servo_duty.png
.. |img_slide| image:: /img/component/slide_switch.png
.. |img_slide_prin| image:: /img/component/slide_principle.png
.. |img_slide_symbol| image:: /img/component/slide_symbol.png
.. |img_thermistor| image:: /img/component/thermistor.png
.. |img_thermistor_symbol| image:: /img/component/thermistor_symbol.png
.. |img_tilt| image:: /img/component/tilt_switch.png
.. |img_tilt_symbol| image:: /img/component/tilt_symbol.png
.. |img_transistor| image:: /img/component/transistor.png
.. |img_NPN&PNP| image:: /img/component/NPN&PNP.png
.. |img_ebc| image:: /img/component/ebc.png
.. |img_transistor_symbol| image:: /img/component/transistor_symbol.png
.. |img_ws2812| image:: /img/component/ws2812b.png
.. |img_mfrc522| image:: /img/component/mfrc522.png
.. |img_power_module| image:: /img/component/power_module.png
.. |img_limit_switch| image:: /img/component/limit_switch.png
.. |img_led_bar| image:: /img/component/led_bar_sche.png
.. |img_irrecv| image:: /img/component/infrared-receiver_01.png
.. |img_diode| image:: /img/component/diode.png
.. |img_pump| image:: /img/component/pump.jpg
.. |img_water_sensor| image:: /img/component/water_sensor.png
.. |img_esp8266| image:: /img/component/esp8266.png
"""

# wiring pic
rst_epilog += """
.. |wiring_74hc_7seg| image:: /img/wiring/wiring_led_segment_display.png
    :width: 600
.. |wiring_74hc_led| image:: /img/wiring/wiring_microchip_74hc595.png
    :width: 600
.. |wiring_buzzer| image:: /img/wiring/wiring_custom_tone.png
    :width: 600
.. |wiring_button| image:: /img/wiring/wiring_read_button_value.png
    :width: 600
.. |wiring_button_pullup| image:: /img/wiring/wiring_read_button_value_2.png
.. |wiring_tilt| image:: /img/wiring/wiring_read_button_value_4.png
.. |wiring_slide| image:: /img/wiring/wiring_read_button_value_3.png   
.. |wiring_limit_sw| image:: /img/wiring/wiring_read_button_value_5.png 
.. |wiring_led| image:: /img/wiring/wiring_led.png   
    :width: 600
.. |wiring_lcd| image:: /img/wiring/wiring_lcd.png
    :width: 600
.. |wiring_ws2812| image:: /img/wiring/wiring_rgb_strip.png
    :width: 600
.. |wiring_pot| image:: /img/wiring/wiring_turn_the_knob.png
.. |wiring_rgb| image:: /img/wiring/wiring_colorful_light.png
.. |wiring_servo| image:: /img/wiring/wiring_swing_servo.png
.. |wiring_temp| image:: /img/wiring/wiring_thermometer.png
.. |wiring_ultrasonic| image:: /img/wiring/wiring_ultrasonic.png
.. |wiring_4dig| image:: /img/wiring/wiring_4dig.png
.. |wiring_keypad| image:: /img/wiring/wiring_keypad.png
.. |wiring_joystick| image:: /img/wiring/wiring_joystick.png
.. |wiring_motor| image:: /img/wiring/wiring_motor.png
.. |wiring_water| image:: /img/wiring/wiring_water.png
.. |wiring_photoresistor| image:: /img/wiring/wiring_photoresistor.png
.. |wiring_pir| image:: /img/wiring/wiring_pir.png
.. |wiring_ledbar| image:: /img/wiring/wiring_ledbar.png
.. |wiring_reed| image:: /img/wiring/wiring_reed.png
.. |wiring_mpr121| image:: /img/wiring/wiring_mpr121.png
.. |wiring_mpu6050| image:: /img/wiring/wiring_mpu6050.png
.. |wiring_rfid| image:: /img/wiring/wiring_rfid.png
.. |wiring_irremote| image:: /img/wiring/wiring_irremote.png
.. |wiring_dht11| image:: /img/wiring/wiring_dht11.png
.. |wiring_ledmatrix_1| image:: /img/wiring/wiring_matrix_1.png
.. |wiring_ledmatrix_2| image:: /img/wiring/wiring_matrix_2.png
.. |wiring_ledmatrix_3| image:: /img/wiring/wiring_matrix_3.png
.. |wiring_ledmatrix_4| image:: /img/wiring/wiring_matrix_4.png
.. |wiring_irrecv| image:: /img/wiring/wiring_irrecv.png
.. |wiring_pump| image:: /img/wiring/wiring_pump.png
.. |wiring_s8050| image:: /img/wiring/wiring_transistor_s8050.png
.. |wiring_s8550| image:: /img/wiring/wiring_transistor_s8550.png
.. |wiring_relay_1| image:: /img/wiring/wiring_relay_1.png
.. |wiring_relay_2| image:: /img/wiring/wiring_relay_2.png
.. |wiring_light_theremin| image:: /img/wiring/wiring_light_theremin.png
.. |wiring_room_temp|  image:: /img/wiring/wiring_room_temp.png
.. |wiring_app_test|  image:: /img/wiring/wiring_app_test.png
.. |wiring_app_display|  image:: /img/wiring/wiring_esp8266_display.png
.. |wiring_app_actuator|  image:: /img/wiring/wiring_esp8266_actuator.png
.. |wiring_app_piano|  image:: /img/wiring/wiring_esp8266_piano.png
.. |wiring_app_plant_monitor|  image:: /img/wiring/wiring_esp8266_plant_monitor.png
"""

# wiring pic +
rst_epilog += """
.. |wiring_alarm_siren_lamp| image:: /img/wiring/wiring_alarm_siren_lamp.png
.. |wiring_digital_bubble_level|  image:: /img/wiring/wiring_digital_bubble_level.png
.. |wiring_fruit_piano|  image:: /img/wiring/wiring_fruit_piano.png
.. |wiring_game_10_second|  image:: /img/wiring/wiring_game_10_second.png
.. |wiring_game_guess_number|  image:: /img/wiring/wiring_game_guess_number.png
.. |wiring_somatosensory_controller|  image:: /img/wiring/wiring_motion_control.png
.. |wiring_passager_coumter|  image:: /img/wiring/wiring_passager_coumter.png
.. |wiring_reversing_aid|  image:: /img/wiring/wiring_reversing_aid.png
.. |wiring_rifd_music_player|  image:: /img/wiring/wiring_rifd_music_player.png
.. |wiring_traffic_light|  image:: /img/wiring/wiring_traffic_light.png
"""

# schematic pic
rst_epilog += """
.. |sch_74hc_7seg| image:: /img/schematic/sch_number_display.png
.. |sch_74hc_led| image:: /img/schematic/sch_microchip_74hc595.png
.. |sch_buzzer| image:: /img/schematic/sch_custom_tone.png
.. |sch_button| image:: /img/schematic/sch_reading_button_value.png
.. |sch_button_pullup| image:: /img/schematic/sch_reading_button_value2.png
.. |sch_tilt| image:: /img/schematic/sch_reading_button_value4.png
.. |sch_slide| image:: /img/schematic/sch_reading_button_value3.png   
.. |sch_limit_sw| image:: /img/schematic/sch_reading_button_value5.png 
.. |sch_led| image:: /img/schematic/sch_hello_led.png   
.. |sch_lcd| image:: /img/schematic/sch_liquid_crystal_display.png
.. |sch_ws2812| image:: /img/schematic/sch_rgb_led_strip.png
.. |sch_pot| image:: /img/schematic/sch_turn_the_knob.png
.. |sch_rgb| image:: /img/schematic/sch_colorful_light.png
.. |sch_servo| image:: /img/schematic/sch_swinging_servo.png
.. |sch_temp| image:: /img/schematic/sch_thermometer.png
.. |sch_ultrasonic| image:: /img/schematic/sch_measuring_distance.png
.. |sch_4dig| image:: /img/schematic/sch_time_counter.png
.. |sch_keypad| image:: /img/schematic/sch_4x4_keypad.png
.. |sch_joystick| image:: /img/schematic/sch_toggle_the_joystick.png
.. |sch_motor| image:: /img/schematic/sch_small_fan.png
.. |sch_water| image:: /img/schematic/sch_feel_the_water_level.png
.. |sch_photoresistor| image:: /img/schematic/sch_feel_the_light.png
.. |sch_pir| image:: /img/schematic/sch_detect_human_movement.png
.. |sch_ledbar| image:: /img/schematic/sch_display_the_level.png
.. |sch_reed| image:: /img/schematic/sch_feel_the_magnetism.png
.. |sch_mpr121| image:: /img/schematic/sch_electrode_keyboard.png
.. |sch_mpu6050| image:: /img/schematic/sch_6-axis_motion_tracking.png
.. |sch_rfid| image:: /img/schematic/sch_rfid.png
.. |sch_irremote| image:: /img/schematic/sch_ir_remote_control.png
.. |sch_dht11| image:: /img/schematic/sch_dht11.png
.. |sch_ledmatrix| image:: /img/schematic/sch_8x8_pixel_graphics.png
.. |sch_irrecv| image:: /img/schematic/sch_ir_remote_control.png
.. |sch_pump| image:: /img/schematic/sch_pumping.png
.. |sch_s8050| image:: /img/schematic/sch_transistor_s8050.png
.. |sch_s8550| image:: /img/schematic/sch_transistor_s8550.png
.. |sch_relay_1| image:: /img/schematic/sch_control_another_circuit.png
.. |sch_relay_2| image:: /img/schematic/sch_control_another_circuit2.png
.. |sch_light_theremin| image:: /img/schematic/sch_light_theremin.png
.. |sch_room_temp|  image:: /img/schematic/sch_room_temp.png
.. |sch_app_test|  image:: /img/schematic/sch_app_test.png
"""



# pico micropython start
rst_epilog += """
.. |mps_bootsel_onboard| image:: /img/micropython_start/bootsel_onboard.png
.. |mps_index_htm| image:: /img/micropython_start/index_htm.png
.. |mps_welcome_pico| image:: /img/micropython_start/welcome_pico.png
.. |mps_download_uf2| image:: /img/micropython_start/download_uf2.png
.. |mps_move_uf2| image:: /img/micropython_start/move_uf2.png
.. |mps_download_thonny| image:: /img/micropython_start/download_thonny.png
.. |mps_thonny_ide.jpg| image:: /img/micropython_start/thonny_ide.jpg
.. |mps_hello_shell| image:: /img/micropython_start/hello_shell.png
.. |mps_hello_world_script| image:: /img/micropython_start/hello_world_script.png
.. |mps_where_save| image:: /img/micropython_start/where_save.png
.. |mps_hello_world_save| image:: /img/micropython_start/hello_world_save.png
"""

# pico arduino start
rst_epilog += """
.. |ars_arduino_setup1| image:: /img/arduino_start/arduino_setup1.png
.. |ars_boards_manager| image:: /img/arduino_start/boards_manager.png
.. |ars_install_pico| image:: /img/arduino_start/install_pico.png
.. |ars_pico_board| image:: /img/arduino_start/pico_board.png
.. |ars_test_blink| image:: /img/arduino_start/test_blink.png
.. |ars_upload_blink| image:: /img/arduino_start/upload_blink.png
.. |ars_upload_process| image:: /img/arduino_start/upload_process.png
.. |ars_done_uploading| image:: /img/arduino_start/done_uploading.png
.. |ars_arduino_ide| image:: /img/arduino_start/arduino_ide.png
"""

# appenx arduino add lib
rst_epilog += """
.. |apx_add_lib1| image:: /img/appenx_add_lib/image291.png
.. |apx_add_lib2| image:: /img/appenx_add_lib/image292.png
.. |apx_add_lib3| image:: /img/appenx_add_lib/image293.png
.. |apx_add_lib4| image:: /img/appenx_add_lib/image294.png
.. |apx_add_lib5| image:: /img/appenx_add_lib/image295.png
.. |apx_add_lib6| image:: /img/appenx_add_lib/image296.png
.. |apx_add_lib7| image:: /img/appenx_add_lib/image297.png

"""

# faq
rst_epilog += """
.. |faq_save_to_pico| image:: /img/faq/save_to_pico.png
.. |faq_interepter_thonny| image:: /img/faq/interepter_thonny.png
"""

# pico pin
rst_epilog += """
.. |pico| image:: /img/pico.jpg
.. |pico_pin| image:: /img/pico_pin.jpg
.. |pin_adc| image:: /img/pin_pic3.png
.. |pin_pwm| image:: /img/pin_pic.png
.. |pin_i2c| image:: /img/pin_pic2.png
"""

# basic circuit
rst_epilog += """
.. |bc1| image:: /img/basic_circuit/bc1.png
.. |bc2| image:: /img/basic_circuit/bc2.png
.. |bc2.5| image:: /img/basic_circuit/bc2.5.png
.. |bc3| image:: /img/basic_circuit/bc3.png
"""

# sunfounder controller
rst_epilog += """
.. |sc_app_install| image:: /img/esp8266/sc_app_install.png
.. |sc_app_add_new_controller| image:: /img/esp8266/sc_app_add_new_controller.jpg
.. |sc_app_create_controller| image:: /img/esp8266/sc_app_create_controller.jpg
.. |sc_app_interface| image:: /img/esp8266/sc_app_interface.jpg
.. |sc_app_add_number| image:: /img/esp8266/sc_app_add_number.jpg
.. |sc_app_add_slider| image:: /img/esp8266/sc_app_add_slider.jpg
.. |sc_app_add_saved| image:: /img/esp8266/sc_app_add_saved.jpg
.. |sc_app_actuator| image:: /img/esp8266/sc_app_actuator.jpg
.. |sc_app_display| image:: /img/esp8266/sc_app_display.jpg
.. |ws_flowchart| image:: /img/esp8266/ws_flowchart.png
.. |sc_app_widget_act| image:: /img/esp8266/sc_app_act.png
.. |sc_app_widget_dis| image:: /img/esp8266/sc_app_dis.png
.. |sc_app_piano| image:: /img/esp8266/sc_app_piano.jpg
.. |sc_app_plant_monitor| image:: /img/esp8266/sc_app_plant_monitor.jpg
.. |sc_img_plant_monitor| image:: /img/esp8266/sc_img_plant_monitor.jpg

"""