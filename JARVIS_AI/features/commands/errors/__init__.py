# features/commands/errors/__init__.py

class JarvisError(Exception):
    pass


class CommandError(JarvisError):
    pass


class VoiceRecognitionError(JarvisError):
    pass


class FileManagerError(JarvisError):
    pass


class OrganizerError(JarvisError):
    pass


class StartupError(JarvisError):
    pass


class ShutdownError(JarvisError):
    pass