import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbG9uZ2VzdE1vdW50YWluKHNlbGYsIEEpOgogICAgICAgIHJlcyA9IHVwID0gZG93biA9IDAKICAgICAgICBmb3IgaSBpbiByYW5nZSgxLCBsZW4oQSkpOgogICAgICAgICAgICBpZiBkb3duIGFuZCBBW2kgLSAxXSA8IEFbaV0gb3IgQVtpIC0gMV0gPT0gQVtpXTogdXAgPSBkb3duID0gMAogICAgICAgICAgICB1cCArPSBBW2kgLSAxXSA8IEFbaV0KICAgICAgICAgICAgZG93biArPSBBW2kgLSAxXSA+IEFbaV0KICAgICAgICAgICAgaWYgdXAgYW5kIGRvd246IHJlcyA9IG1heChyZXMsIHVwICsgZG93biArIDEpCiAgICAgICAgcmV0dXJuIHJlcw==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
