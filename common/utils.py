class SQLutils:
    @staticmethod
    def offset(page: int, limit: int) -> int:
        return (page - 1) * limit
