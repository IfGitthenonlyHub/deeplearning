import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("aW1wb3J0IHN5cwppbXBvcnQgbWF0aAppbnB1dCA9IHN5cy5zdGRpbi5yZWFkbGluZQoKcT1pbnQoaW5wdXQoKSkKZm9yIGkgaW4gcmFuZ2UocSk6CgluLG09bGlzdChtYXAoaW50LGlucHV0KCkuc3BsaXQoKSkpCglyPVswXSpuCgljPVswXSptCglhcnI9W10KCWZvciBpIGluIHJhbmdlKG4pOgoJCWFyci5hcHBlbmQoaW5wdXQoKSkKCglmb3IgaSBpbiByYW5nZShuKToKCQlmb3IgaiBpbiByYW5nZShtKToKCQkJaWYgYXJyW2ldW2pdPT0iLiI6CgkJCQlyW2ldKz0xCgkJCQljW2pdKz0xCgltaW5uPTEwMDAwMDAwMDAKCWZvciBpIGluIHJhbmdlKG4pOgoJCWZvciBqIGluIHJhbmdlKG0pOgoJCQlpZiBhcnJbaV1bal09PSIuIjoKCQkJCW1pbm49bWluKG1pbm4scltpXStjW2pdLTEpCgkJCWVsc2U6CgkJCQltaW5uPW1pbihtaW5uLHJbaV0rY1tqXSkKCglwcmludChtaW5uKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
