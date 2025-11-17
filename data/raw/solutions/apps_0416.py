import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgY2F0TW91c2VHYW1lKHNlbGYsIGdyYXBoKToKICAgICAgICBpbXBvcnQgZnVuY3Rvb2xzCiAgICAgICAgbj1sZW4oZ3JhcGgpCiAgICAgICAgCiAgICAgICAgQGxydV9jYWNoZShOb25lKQogICAgICAgIGRlZiBkcCh0LHgseSk6CiAgICAgICAgICAgIGlmIHQ9PTIqbjoKICAgICAgICAgICAgICAgIHJldHVybiAwCiAgICAgICAgICAgIGlmIHg9PXk6CiAgICAgICAgICAgICAgICByZXR1cm4gMgogICAgICAgICAgICBpZiB4PT0wOgogICAgICAgICAgICAgICAgcmV0dXJuIDEKICAgICAgICAgICAgaWYgdCUyPT0wOgogICAgICAgICAgICAgICAgaWYgYW55KGRwKHQrMSx4bix5KT09MSBmb3IgeG4gaW4gZ3JhcGhbeF0pOgogICAgICAgICAgICAgICAgICAgIHJldHVybiAxCiAgICAgICAgICAgICAgICBpZiBhbGwoZHAodCsxLHhuLHkpPT0yIGZvciB4biBpbiBncmFwaFt4XSk6CiAgICAgICAgICAgICAgICAgICAgcmV0dXJuIDIKICAgICAgICAgICAgICAgIHJldHVybiAwCiAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICBpZiBhbnkoZHAodCsxLHgseW4pPT0yIGZvciB5biBpbiBncmFwaFt5XSBpZiB5biE9MCk6CiAgICAgICAgICAgICAgICAgICAgcmV0dXJuIDIKICAgICAgICAgICAgICAgIGlmIGFsbChkcCh0KzEseCx5bik9PTEgZm9yIHluIGluIGdyYXBoW3ldIGlmIHluIT0wKToKICAgICAgICAgICAgICAgICAgICByZXR1cm4gMQogICAgICAgICAgICAgICAgcmV0dXJuIDAKICAgICAgICByZXR1cm4gZHAoMCwxLDIp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
