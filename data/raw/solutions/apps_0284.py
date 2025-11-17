import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgYmFnT2ZUb2tlbnNTY29yZShzZWxmLCB0b2tlbnM6IExpc3RbaW50XSwgUDogaW50KSAtPiBpbnQ6CiAgICAgICAgaWYgbm90IHRva2VuczogcmV0dXJuIDAKICAgICAgICAKICAgICAgICB0b2tlbnMuc29ydCgpCiAgICAgICAgCiAgICAgICAgcG9pbnQgPSAwCiAgICAgICAgd2hpbGUgdG9rZW5zOgogICAgICAgICAgICBpZiBQIDwgdG9rZW5zWzBdOgogICAgICAgICAgICAgICAgaWYgcG9pbnQgYW5kIGxlbih0b2tlbnMpID4gMToKICAgICAgICAgICAgICAgICAgICBQICs9IHRva2Vucy5wb3AoKQogICAgICAgICAgICAgICAgICAgIHBvaW50IC09IDEKICAgICAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICAgICAgYnJlYWsKICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgIFAgLT0gdG9rZW5zLnBvcCgwKQogICAgICAgICAgICAgICAgcG9pbnQgKz0gMQogICAgICAgIAogICAgICAgIHJldHVybiBwb2ludA==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
