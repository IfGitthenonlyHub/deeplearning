import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("ZGVmIGYocyk6CiAgdD0iYWJhY2FiYSIKICBmb3IgaSBpbiByYW5nZSg3KToKICAgIGlmIHNbaV0hPSI/IiBhbmQgdFtpXSE9c1tpXTpyZXR1cm4gRmFsc2UKICByZXR1cm4gVHJ1ZQpkZWYgZyhzKToKICBjPTAKICBmb3IgaSBpbiByYW5nZSg3LGxlbihzKSsxKToKICAgIGlmIHNbaS03OmldPT0iYWJhY2FiYSI6Yys9MQogIHJldHVybiBjCgpmb3IgXyBpbiByYW5nZShpbnQoaW5wdXQoKSkpOgogIG49aW50KGlucHV0KCkpCiAgcz1pbnB1dCgpCiAgaWYgZyhzKT4xOgogICAgcHJpbnQoIk5vIikKICAgIGNvbnRpbnVlCiAgaWYgImFiYWNhYmEiIGluIHM6CiAgICBwcmludCgiWWVzIikKICAgIHByaW50KHMucmVwbGFjZSgiPyIsInoiKSkKICAgIGNvbnRpbnVlCiAgZmxhZz1GYWxzZQogIGZvciBpIGluIHJhbmdlKDcsbGVuKHMpKzEpOgogICAgaWYgZihzW2ktNzppXSk6CiAgICAgIHQ9KHNbOmktN10rImFiYWNhYmEiK3NbaTpdKS5yZXBsYWNlKCI/IiwieiIpCiAgICAgIGlmIGcodCk+MTpjb250aW51ZQogICAgICBwcmludCgiWWVzIikKICAgICAgcHJpbnQodCkKICAgICAgZmxhZz1UcnVlCiAgICAgIGJyZWFrCiAgaWYgbm90KGZsYWcpOnByaW50KCJObyIp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
