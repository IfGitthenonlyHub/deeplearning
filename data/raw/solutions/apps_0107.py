import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("dCA9IGludChpbnB1dCgpKQpmb3IgXyBpbiByYW5nZSh0KToKICAgIGEsIGIsIGMsIGQgPSBsaXN0KG1hcChpbnQsIGlucHV0KCkuc3BsaXQoKSkpCiAgICBwb3NzaWJsZSA9IFsnWWEnLCAnWWEnLCAnWWEnLCAnWWEnXQogICAgaWYgKGErYiklMiA9PSAwOgogICAgICAgIHBvc3NpYmxlWzBdID0gJ1RpZGFrJwogICAgICAgIHBvc3NpYmxlWzFdID0gJ1RpZGFrJwogICAgZWxzZToKICAgICAgICBwb3NzaWJsZVsyXSA9ICdUaWRhaycKICAgICAgICBwb3NzaWJsZVszXSA9ICdUaWRhaycKICAgIGlmIChhK2QpID09IDA6CiAgICAgICAgcG9zc2libGVbMF0gPSAnVGlkYWsnCiAgICAgICAgcG9zc2libGVbM10gPSAnVGlkYWsnCiAgICBpZiAoYitjKSA9PSAwOgogICAgICAgIHBvc3NpYmxlWzFdID0gJ1RpZGFrJwogICAgICAgIHBvc3NpYmxlWzJdID0gJ1RpZGFrJwoKICAgIHByaW50KCcgJy5qb2luKHBvc3NpYmxlKSk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
