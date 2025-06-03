# /clients/pyperadaptor.py

import pyperclip
import time


def waitForPaste(timeout=None):
    """This function call blocks until a non-empty text string exists on the
    clipboard. It returns this text.

    This function raises PyperclipTimeoutException if timeout was set to
    a number of seconds that has elapsed without non-empty text being put on
    the clipboard."""
    startTime = time.time()
    while True:
        clipboardText = pyperclip.paste()
        if clipboardText != '':
            print(type(clipboardText))
            return clipboardText
        time.sleep(0.01)

        if timeout is not None and time.time() > startTime + timeout:
            raise PyperclipTimeoutException('waitForPaste() timed out after ' + str(timeout) + ' seconds.')


def waitForNewPaste(timeout=None):
    """This function call blocks until a new text string exists on the
    clipboard that is different from the text that was there when the function
    was first called. It returns this text.

    This function raises PyperclipTimeoutException if timeout was set to
    a number of seconds that has elapsed without non-empty text being put on
    the clipboard."""
    startTime = time.time()
    originalText = pyperclip.paste()
    while True:
        currentText = pyperclip.paste()
        if currentText != originalText:
            return currentText
        time.sleep(0.01)

        if timeout is not None and time.time() > startTime + timeout:
            raise PyperclipTimeoutException('waitForNewPaste() timed out after ' + str(timeout) + ' seconds.')
