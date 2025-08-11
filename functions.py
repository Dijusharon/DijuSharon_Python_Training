
from pathlib import Path

FILEPATH = Path("todos.txt")

def get_todos(filepath: Path = FILEPATH):
    """Return the list of todos as lines (each item ends with \n)."""
    if not filepath.exists():
        filepath.write_text("", encoding="utf-8")
    return filepath.read_text(encoding="utf-8").splitlines(keepends=True)

def write_todos(todos, filepath: Path = FILEPATH):
    """Persist the list of todos (expects items ending with \n)."""
    filepath.write_text("".join(todos), encoding="utf-8")
