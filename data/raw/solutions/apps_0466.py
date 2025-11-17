import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWFza1BJSShzZWxmLCBTOiBzdHIpIC0+IHN0cjoKICAgICAgICBOPWxlbihTKQogICAgICAgIGlmICdAJyBpbiBTOgogICAgICAgICAgICBTPVMubG93ZXIoKQogICAgICAgICAgICBmaXJzdCxyZXN0PVMuc3BsaXQoJ0AnKQogICAgICAgICAgICByZXR1cm4gZmlyc3RbMF0rJyonKjUrZmlyc3RbLTFdKydAJytyZXN0CiAgICAgICAgZWxzZToKICAgICAgICAgICAgZGlnaXRzPScnLmpvaW4oYyBmb3IgYyBpbiBTIGlmIGMuaXNkaWdpdCgpKQogICAgICAgICAgICBhPVtdCiAgICAgICAgICAgIGlmIGxlbihkaWdpdHMpPjEwOgogICAgICAgICAgICAgICAgYS5hcHBlbmQoJysnKycqJyoobGVuKGRpZ2l0cyktMTApKQogICAgICAgICAgICBhLmFwcGVuZCgnKioqJykKICAgICAgICAgICAgYS5hcHBlbmQoJyoqKicpCiAgICAgICAgICAgIGEuYXBwZW5kKGRpZ2l0c1stNDpdKQogICAgICAgICAgICByZXR1cm4gJy0nLmpvaW4oYSk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
