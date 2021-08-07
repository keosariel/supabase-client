class SupabaseError(Exception):
    """Base class for all supabase errors

        :param message: A human-readable error message string.
    """

    def __init__(self, message):
        Exception.__init__(self, message)

class ClientConnectorError(SupabaseError):
    def __init__(self, message):
        SupabaseError.__init__(self, message)

class QueryError(SupabaseError):
    def __init__(self, message):
        SupabaseError.__init__(self, message)

class InvalidRangeError(SupabaseError):
    def __init__(self, message):
        SupabaseError.__init__(self, message)

class UnexpectedValueTypeError(SupabaseError):
    def __init__(self, message):
        SupabaseError.__init__(self, message)




