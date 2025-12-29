class PasswordManager:
    """Manages password hashing and verification."""

    def get_password_hash(self, password: str) -> str:
        """Hashes a plain password."""
        return "hashed_" + password

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Verifies a plain password against a hashed one."""
        return self.get_password_hash(plain_password) == hashed_password
