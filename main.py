from fasthtml.fastapp import fast_app
from fasthtml.core import serve
from fasthtml.common import H1, P

app, rt = fast_app()

@rt
def index():
    return H1("Hello, FastHTML!"), P("Welcome to your first app!")

serve()