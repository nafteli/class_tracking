import PySimpleGUI as sg


class MainWindow:
    data = [
        ["Name", "Age", "Country"],
        ["John", "32", "USA"],
        ["Jane", "28", "Canada"],
        ["Jim", "41", "UK"],
    ]
    sidedar = [
        [sg.Button("Vertical Button 1")],
        [sg.Button("Vertical Button 2")],
        [sg.Button("Vertical Button 3")],
    ]
    dataWindow = sg.Table(
            values=data,
            headings=["Name", "Age", "Country"],
            auto_size_columns=True,
            display_row_numbers=True,
            justification="center",
            num_rows=5,
        )

    def __init__(self) -> None:
        data = [
                ["Name", "Age", "Country"],
                ["John", "32", "USA"],
                ["Jane", "28", "Canada"],
                ["Jim", "41", "UK"],
            ]
        sidedar = [
                [sg.Button("Vertical Button 1")],
                [sg.Button("Vertical Button 2")],
                [sg.Button("Vertical Button 3")],
            ]
        dataWindow = sg.Table(
                values=data,
                headings=["Name", "Age", "Country"],
                auto_size_columns=True,
                display_row_numbers=True,
                justification="center",
                num_rows=5,
            )
        self.navbar = [
                sg.Button("מעקב תלמיד"[::-1]),
                sg.Button("מעקב יום"[::-1]),
                sg.Button("ניהול"[::-1]),
                sg.Button("קורסים"[::-1]),
                sg.Button("תלמידים"[::-1]),
                sg.Button("כיתות"[::-1]),
            ]
        self.main_window = [
                [sg.Frame("",[self.navbar],)],
                [sg.Column([[sg.Frame("",sidedar,)]]),
                dataWindow,],
            ]

    def run_main_window(self):
        window_main_window = sg.Window("Main Window", self.main_window)
        while True:
            event, values = window_main_window.read()
            if event in (None, "Exit"):
                break
        window_main_window.close()
