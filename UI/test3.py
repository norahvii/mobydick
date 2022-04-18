import PySimpleGUI as sg

sg.theme('Dark Grey 9')

layout = [[sg.Text('Add book')],
          [sg.Input(), sg.FileBrowse()],
          [sg.Text('Add stop list')],
          [sg.Input(), sg.FileBrowse()],
          [sg.Button('Run'), sg.Button('Quit')]
          ]

window = sg.Window('Add files', layout)

while True:
    event, values = window.read()
    if event == 'Quit':
        windowclose()


windowclose()
