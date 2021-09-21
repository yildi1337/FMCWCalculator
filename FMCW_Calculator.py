####################################################################################################
#
# FMCW_Calculator.py
#
# Tool for calculating FMCW radar parameters.
#
# Phillip Durdaut, 2021-09-20
#
####################################################################################################
import PySimpleGUI as sg
import ctypes

# global constants
SYSTEM_COLOR = '#f0f0f0'
LABEL_WIDTH = 25
INPUT_WIDTH = 25
BUTTON_WIDTH = 23
SPEED_OF_LIGHT = 299792458
DECIMAL_DIGITS = 4

# set standard color theme
sg.theme('SystemDefault')

# message box
def mbox(title, text):
    return ctypes.windll.user32.MessageBoxW(0, text, title, 0)

# layout
layout = [
    [ sg.Text('Speed of light [m/s]:', size=(LABEL_WIDTH,1)), sg.Input(SPEED_OF_LIGHT, size=(INPUT_WIDTH,1), disabled=True, key='key_speed_of_light_ms') ],
    [ sg.Text('Sweep bandwidth [GHz]:', size=(LABEL_WIDTH,1)), sg.Input('10', size=(INPUT_WIDTH,1), key='key_sweep_bandwidth_GHz') ],
    [ sg.Text('Sweep time [ms]:', size=(LABEL_WIDTH,1)), sg.Input('1', size=(INPUT_WIDTH,1), key='key_sweep_time_ms') ],
    [ sg.Text('Distance to reflecting object [m]:', size=(LABEL_WIDTH,1)), sg.Input('1', size=(INPUT_WIDTH,1), key='key_distance_m') ],
    [ sg.Text('Difference frequency [kHz]:', size=(LABEL_WIDTH,1)), sg.Input('', size=(INPUT_WIDTH,1), key='key_difference_frequency_kHz') ],
    [ sg.Text('Resolution [mm]:', size=(LABEL_WIDTH,1)), sg.Input('', size=(INPUT_WIDTH,1), disabled=True, key='key_resolution_mm') ],
    [ sg.Text('') ],
    [ sg.Button('Calculate', size=(BUTTON_WIDTH,1)), sg.Button('Exit', size=(BUTTON_WIDTH,1)) ]
]

# create new window
window = sg.Window("FMCW Calculator (2021)", layout, finalize=True, margins=(25, 25), location=(100,150))

# run
while True:

    event, values = window.read()

    if event == "Calculate":        
        
        # analyze input parameters and convert them to base units
        nEmptyInputs = 0
        if values['key_sweep_bandwidth_GHz'] == '':
            nEmptyInputs = nEmptyInputs + 1  
        else:
            sweep_bandwidth_Hz = float(values['key_sweep_bandwidth_GHz']) * 1e9

        if values['key_sweep_time_ms'] == '':
            nEmptyInputs = nEmptyInputs + 1 
        else:
            sweep_time_s = float(values['key_sweep_time_ms']) / 1e3

        if values['key_distance_m'] == '':
            nEmptyInputs = nEmptyInputs + 1
        else:
            distance_m = float(values['key_distance_m'])

        if values['key_difference_frequency_kHz'] == '':
            nEmptyInputs = nEmptyInputs + 1
        else:
            difference_frequency_Hz = float(values['key_difference_frequency_kHz']) * 1e3

        # check for correct number of given input parameters
        if nEmptyInputs == 0:
            mbox('Error', 'One input field must be empty.')
            continue

        if nEmptyInputs > 1:
            mbox('Error', 'More input fields must be filled in.')
            continue

        # determine missing parameter
        if values['key_sweep_bandwidth_GHz'] == '':
            sweep_bandwidth_Hz = SPEED_OF_LIGHT * difference_frequency_Hz * sweep_time_s / (2 * distance_m)
            window.FindElement('key_sweep_bandwidth_GHz').update(str(round(sweep_bandwidth_Hz / 1e9, DECIMAL_DIGITS)))

        if values['key_sweep_time_ms'] == '':
            sweep_time_s = 2 * sweep_bandwidth_Hz * distance_m / (SPEED_OF_LIGHT * difference_frequency_Hz)
            window.FindElement('key_sweep_time_ms').update(str(round(sweep_time_s * 1e3, DECIMAL_DIGITS)))

        if values['key_distance_m'] == '':
            distance_m = SPEED_OF_LIGHT * difference_frequency_Hz * sweep_time_s / (2 * sweep_bandwidth_Hz)
            window.FindElement('key_distance_m').update(str(round(distance_m, DECIMAL_DIGITS)))

        if values['key_difference_frequency_kHz'] == '':
            difference_frequency_Hz = 2 * sweep_bandwidth_Hz * distance_m / (SPEED_OF_LIGHT * sweep_time_s)
            window.FindElement('key_difference_frequency_kHz').update(str(round(difference_frequency_Hz / 1e3, DECIMAL_DIGITS)))

        # determine resolution
        resolution_m = SPEED_OF_LIGHT / (2 * sweep_bandwidth_Hz)        
        window.FindElement('key_resolution_mm').update(str(round(resolution_m * 1e3, DECIMAL_DIGITS)))

    if event == "Exit" or event == sg.WIN_CLOSED:
        break

window.close()
