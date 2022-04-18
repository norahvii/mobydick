import PySimpleGUI as sg

sg.theme('Dark Grey 9')

layout = [[sg.Text('Add book')],
          [sg.Input(), sg.FileBrowse()],
          [sg.Text('Add stop list')],
          [sg.Input(), sg.FileBrowse()],
          [sg.OK(), sg.Cancel()]
          ]

window = sg.Window('Add files', layout)

event, values = window.read()
windowclose()
