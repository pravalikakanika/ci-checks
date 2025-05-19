from notification.notification import send_notification


def test_send_notification_valid():
    assert send_notification("Hello", 2) == "Notification sent to user 2: Hello"


def test_send_notification_invalid():
    try:
        send_notification("", -1)
        assert False, "Expected ValueError"
    except ValueError:
        pass
