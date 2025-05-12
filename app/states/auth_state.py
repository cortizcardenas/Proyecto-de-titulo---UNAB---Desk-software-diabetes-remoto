import reflex as rx
import bcrypt
import sqlite3
from typing import Optional, TypedDict
from app import database


class User(TypedDict):
    id: int
    email: str
    full_name: str


class AuthState(rx.State):
    """Manages user authentication, session, and theme."""

    current_user: User | None = None
    theme: str = "light"

    @rx.var
    def is_logged_in(self) -> bool:
        """Checks if a user is currently logged in."""
        return self.current_user is not None

    @rx.var
    def user_full_name(self) -> str:
        """Returns the full name of the logged-in user, or a default message."""
        return (
            self.current_user["full_name"]
            if self.current_user
            else "Guest"
        )

    @rx.var
    def user_id(self) -> int | None:
        """Returns the ID of the logged-in user, or None."""
        return (
            self.current_user["id"]
            if self.current_user
            else None
        )

    def _hash_password(self, password: str) -> str:
        """Hashes a password using bcrypt and returns the hash decoded as UTF-8 string."""
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"), salt
        )
        return hashed_password.decode("utf-8")

    def _verify_password(
        self,
        stored_password_hash: str,
        provided_password: str,
    ) -> bool:
        """Verifies a provided password against a stored hash (stored as string)."""
        stored_password_hash_bytes = (
            stored_password_hash.encode("utf-8")
        )
        try:
            return bcrypt.checkpw(
                provided_password.encode("utf-8"),
                stored_password_hash_bytes,
            )
        except ValueError as e:
            print(
                f"Error verifying password (ValueError): {e}. Hash might be invalid or incompatible."
            )
            return False
        except Exception as e:
            print(
                f"An unexpected error occurred during password verification: {e}"
            )
            return False

    @rx.event
    def sign_up(self, form_data: dict):
        """Handles the user sign-up process."""
        email = form_data.get("email", "").strip()
        password = form_data.get("password", "").strip()
        full_name = form_data.get("full_name", "").strip()
        if not email or not password or (not full_name):
            yield rx.toast.error(
                "Full Name, Email and password are required."
            )
            return
        if "@" not in email or "." not in email:
            yield rx.toast.error("Invalid email format.")
            return
        if len(full_name) < 2:
            yield rx.toast.error(
                "Full name must be at least 2 characters."
            )
            return
        existing_user = database.get_user(email)
        if existing_user:
            yield rx.toast.error(
                f"Account with email {email} already exists."
            )
            return
        password_hash_str = self._hash_password(password)
        if database.add_user(
            email, password_hash_str, full_name
        ):
            user_row = database.get_user(email)
            if user_row:
                self.current_user = User(
                    id=user_row["id"],
                    email=user_row["email"],
                    full_name=user_row["full_name"],
                )
                yield rx.toast.success(
                    "Account created successfully!"
                )
                return rx.redirect("/dashboard")
            else:
                yield rx.toast.error(
                    "Account created but failed to automatically log in."
                )
                return rx.redirect("/sign-in")
        else:
            yield rx.toast.error(
                "Failed to create account. Please try again."
            )

    @rx.event
    def sign_in(self, form_data: dict):
        """Handles the user sign-in process."""
        email = form_data.get("email", "").strip()
        password = form_data.get("password", "").strip()
        if not email or not password:
            yield rx.toast.error(
                "Email and password are required."
            )
            return
        user_row = database.get_user(email)
        if (
            user_row
            and "password" in user_row.keys()
            and user_row["password"]
        ):
            stored_password_hash = user_row["password"]
            if self._verify_password(
                stored_password_hash, password
            ):
                self.current_user = User(
                    id=user_row["id"],
                    email=user_row["email"],
                    full_name=user_row["full_name"],
                )
                yield rx.toast.success("Login successful!")
                return rx.redirect("/dashboard")
            else:
                yield rx.toast.error(
                    "Invalid email or password."
                )
        else:
            yield rx.toast.error(
                "Invalid email or password."
            )

    @rx.event
    def sign_out(self):
        """Signs the current user out."""
        self.reset()
        yield rx.toast.info("Signed out successfully.")
        return rx.redirect("/sign-in")

    @rx.event
    def check_session(self):
        """Checks if the user is logged in. If not, redirects to the sign-in page.
        This should be used as an on_load event for protected pages.
        """
        if not self.is_logged_in:
            yield rx.toast.warning(
                "Please sign in to access this page."
            )
            return rx.redirect("/sign-in")

    @rx.event
    def toggle_theme(self):
        """Toggles the UI theme between light and dark."""
        self.theme = (
            "dark" if self.theme == "light" else "light"
        )
        print(f"Theme toggled to: {self.theme}")