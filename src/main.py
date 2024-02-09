#! /usr/bin/env python3

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Input, Button
from textual.containers import Container, ScrollableContainer
from textual.binding import Binding


class Body(ScrollableContainer):
    pass


class LoginForm(Container):
    def compose(self) -> ComposeResult:
        yield Static("Username", classes="label")
        yield Input(placeholder="Username")
        yield Static("Password", classes="label")
        yield Input(placeholder="Password", password=True)
        yield Static()
        yield Button("Login", variant="primary")


class PfTui(App):
    """A Textual app to interact with projectfacts."""

    TITLE = "Projectfacts TUI"
    CSS_PATH = "pf-tui.tcss"
    BINDINGS = [
        ("ctrl+t", "toggle_dark", "Toggle dark mode"),
        Binding("ctrl+q", "app.quit", "Quit", show=True),
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Container(Header(), Body(LoginForm()))
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = PfTui()
    app.run()
