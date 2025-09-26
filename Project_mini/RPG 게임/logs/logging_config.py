import logging
import time
import os

# --------------------
# 로그 디렉토리 생성
# --------------------
log_dir = "./logs/log"
os.makedirs(log_dir + "/battle", exist_ok=True) # 폴더가 없으면 생성
os.makedirs(log_dir + "/error", exist_ok=True) # 폴더가 없으면 생성


# --------------------
# 파일명: 날짜 및 시간 단위
# --------------------
timestamp = time.strftime("%Y%m%d_%H%M%S")
info_log_file  = os.path.join(log_dir + "/battle", f"info_{timestamp}.log")
error_log_file = os.path.join(log_dir + "/error", f"error_{timestamp}.log")

# --------------------
# 출력 포맷
# --------------------
formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s",
                              datefmt="%Y-%m-%d %H:%M:%S")

# --------------------
# 콘솔 핸들러 (info/에러 모두 포함)
# --------------------
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

# --------------------
# info_logger
# --------------------
info_logger = logging.getLogger("info_logger")
info_logger.setLevel(logging.DEBUG)
if not info_logger.handlers:
    file_handler = logging.FileHandler(info_log_file, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    info_logger.addHandler(file_handler)
    info_logger.addHandler(console_handler)

# --------------------
# error_logger
# --------------------
error_logger = logging.getLogger("error_logger")
error_logger.setLevel(logging.ERROR)
if not error_logger.handlers:
    file_handler = logging.FileHandler(error_log_file, encoding="utf-8")
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(formatter)
    error_logger.addHandler(file_handler)
    error_logger.addHandler(console_handler)