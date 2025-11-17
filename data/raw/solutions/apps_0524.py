import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("YXJyID0gbGlzdChpbnB1dCgpKQ0KbiA9IGxlbihhcnIpDQphbnMgPSBsaXN0KCkNCiNmb3IgaSBpbiBhcnI6DQogICAgI2Fucy5hcHBlbmQob3JkKGkpLTk2KQ0KbGkgPSBbJ2InLCdkJywnZicsJ2gnLCdqJywnbCcsJ24nLCdwJywncicsJ3QnLCd2JywneCcsJ3onXQ0KcyA9IHNldChhcnIpDQp0ZW1wID0gcy5pbnRlcnNlY3Rpb24obGkpDQpmb3IgXyBpbiByYW5nZShpbnQoaW5wdXQoKSkpOg0KICAgIHgseSA9IGxpc3QobWFwKGludCxpbnB1dCgpLnNwbGl0KCkpKQ0KICAgIGxpID0gbGlzdCh0ZW1wKQ0KICAgICNzID0gc2V0KCkNCiAgICBjPTANCiAgICBmb3IgaSBpbiByYW5nZSh4LTEseSk6DQogICAgICAgIGlmIGFycltpXSBpbiBsaToNCiAgICAgICAgICAgIGMrPTEgDQogICAgICAgICAgICBsaS5yZW1vdmUoYXJyW2ldKQ0KICAgICAgICBpZiBsZW4obGkpPT0wOg0KICAgICAgICAgICAgYnJlYWsNCiAgICBwcmludChjKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
