import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbGVhc3RPcHNFeHByZXNzVGFyZ2V0KHNlbGYsIHgsIHkpOgogICAgICAgIHBvcyA9IG5lZyA9IGsgPSAwCiAgICAgICAgd2hpbGUgeToKICAgICAgICAgICAgeSwgY3VyID0gZGl2bW9kKHksIHgpCiAgICAgICAgICAgIGlmIGs6CiAgICAgICAgICAgICAgICBwb3MsIG5lZyA9IG1pbihjdXIgKiBrICsgcG9zLCAoY3VyICsgMSkgKiBrICsgbmVnKSwgbWluKCh4IC0gY3VyKSAqIGsgKyBwb3MsICh4IC0gY3VyIC0gMSkgKiBrICsgbmVnKQogICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgcG9zLCBuZWcgPSBjdXIgKiAyLCAoeCAtIGN1cikgKiAyCiAgICAgICAgICAgIGsgKz0gMQogICAgICAgIHJldHVybiBtaW4ocG9zLCBrICsgbmVnKSAtIDE=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
