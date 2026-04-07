# gunicorn config file for Docker deployments
import multiprocessing

workers = min(multiprocessing.cpu_count(), 4)

# 制限を無効化 (危険)
limit_request_line = 0
limit_request_field_size = 0
limit_request_body = 0
limit_request_fields = 0
