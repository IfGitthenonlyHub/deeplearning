import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbGFyZ2VzdFZhbHNGcm9tTGFiZWxzKHNlbGYsIHZhbHVlczogTGlzdFtpbnRdLCBsYWJlbHM6IExpc3RbaW50XSwgbnVtX3dhbnRlZDogaW50LCB1c2VfbGltaXQ6IGludCkgLT4gaW50OgogICAgICAgIGNvdW50cyA9IGNvbGxlY3Rpb25zLmRlZmF1bHRkaWN0KGludCkKICAgICAgICB2bCA9IHNvcnRlZCh6aXAodmFsdWVzLGxhYmVscykpCiAgICAgICAgYW5zID0gMAogICAgICAgIHdoaWxlIG51bV93YW50ZWQgYW5kIHZsOgogICAgICAgICAgICB2YWwsbGFiID0gdmwucG9wKCkKICAgICAgICAgICAgaWYgY291bnRzW2xhYl0gPCB1c2VfbGltaXQ6CiAgICAgICAgICAgICAgICBhbnMgKz0gdmFsCiAgICAgICAgICAgICAgICBjb3VudHNbbGFiXSArPSAxCiAgICAgICAgICAgICAgICBudW1fd2FudGVkIC09IDEKICAgICAgICByZXR1cm4gYW5z").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
