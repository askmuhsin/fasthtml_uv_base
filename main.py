from fasthtml.fastapp import fast_app
from fasthtml.core import serve
from fasthtml.common import (
    H1, H2, H3, P, Div, Span, A, Button,
    Form, Input, Label, Ul, Li, 
    Title, Meta, Script, Titled, Container
)

app, rt = fast_app()

@rt
def index():
    return Titled("FastHTML Demo!", 
        P("Welcome to your first FastHTML app..."),
        Div(
            P("This demonstrates better structure with containers."),
            A("Learn more about FastHTML", href="https://fasthtml.dev")
        )
    )

serve()