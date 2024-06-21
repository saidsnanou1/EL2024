import pyautogui
import time


def clear_search_bar():
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")


def move_and_click(x, y, duration=1):
    pyautogui.moveTo(x, y, duration)
    pyautogui.click()


def open_vscode():
    # For Windows
    pyautogui.hotkey("win", "s")
    time.sleep(1)
    pyautogui.typewrite("Visual Studio Code")
    time.sleep(1)
    pyautogui.press("enter")


def install_extension(extension_name):

    pyautogui.hotkey("ctrl", "shift", "x")
    time.sleep(2)

    clear_search_bar()

    pyautogui.typewrite(extension_name)
    time.sleep(2)

    pyautogui.press("enter")
    time.sleep(2)

    try:
        button_location = None
        while button_location is None:
            button_location = pyautogui.locateOnScreen(
                "I:\\EL2024\\Python\\02_containers\\install.png"
            )
            time.sleep(1)

        button_x, button_y = pyautogui.center(button_location)
        move_and_click(button_x, button_y)

    except pyautogui.ImageNotFoundException:
        print("Image not found")

    time.sleep(5)


def main():
    open_vscode()
    time.sleep(5)

    extensions = [
        "llvm-vs-code-extensions.vscode-clangd",
        "matepek.vscode-catch2-test-adapter",
        "ms-vscode.cmake-tools",
        "twxs.cmake",
        "cschlosser.doxdocgen",
    ]

    for extension in extensions:
        install_extension(extension)
        time.sleep(2)


if __name__ == "__main__":
    main()
