import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgYXRNb3N0TkdpdmVuRGlnaXRTZXQoc2VsZiwgZGlnaXRzOiBMaXN0W3N0cl0sIG46IGludCkgLT4gaW50OgogICAgICAgIGRlZiBsZXNzKGRpZ2l0cywgZCk6CiAgICAgICAgICAgIHJldHVybiBsZW4oW2kgZm9yIGkgaW4gZGlnaXRzIGlmIGkgPCBkIF0pCiAgICAgICAgCiAgICAgICAgY250ID0gMAogICAgICAgIGxkLCBsbiA9IGxlbihkaWdpdHMpLCBsZW4oc3RyKG4pKQogICAgICAgIE4gPSBzdHIobikKICAgICAgICBmb3IgaSBpbiByYW5nZShsbi0xKToKICAgICAgICAgICAgY250ICs9IGxkICoqIChpKzEpCiAgICAgICAgZm9yIGkgaW4gcmFuZ2UobG4pOgogICAgICAgICAgICBjbnQgKz0gbGVzcyhkaWdpdHMsIE5baV0pICogKGxkICoqIChsbiAtIGkgLTEpICkKICAgICAgICAgICAgaWYgTltpXSBub3QgaW4gZGlnaXRzOgogICAgICAgICAgICAgICAgcmV0dXJuIGNudAogICAgICAgIHJldHVybiBjbnQgKyAx").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
