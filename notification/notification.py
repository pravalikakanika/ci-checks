def send_notification(message: str, user_id: int) -> str:
    if not message or user_id <= 0:
        raise ValueError("Invalid input")
    return f"Notification sent to user {user_id}: {message}"
