class DatabaseService:
    def __init__(self):
        # self._savedMessages = self._get_all_saved_messages()
        self._savedMessages = []

        db = DatabaseService()

    def _get_all_saved_messages():
        return "SELECT "

    @property
    def savedMessages(self):
        if not self._savedMessages:
            self._savedMessages = _get_all_saved_messages()
        return self._savedMessages