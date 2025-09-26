import logging
import time
import os

# --------------------
# 1. 로그 디렉토리 생성
# --------------------
base_dir = os.path.abspath("../re_4th/Project_mini/RPG 게임")
log_dir = os.path.join(base_dir, "logs", "log")
battle_dir = os.path.join(log_dir, "battle")
error_dir  = os.path.join(log_dir, "error")

os.makedirs(battle_dir, exist_ok=True)
os.makedirs(error_dir, exist_ok=True)

# --------------------
# 2. 파일명: 날짜 및 시간 단위
# --------------------
timestamp = time.strftime("%Y%m%d_%H%M%S")
info_log_file  = os.path.join(battle_dir, f"info_{timestamp}.log")
error_log_file = os.path.join(error_dir,  f"error_{timestamp}.log")



# --------------------
# 3. 출력 포맷
# --------------------
formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s",
                              datefmt="%Y-%m-%d %H:%M:%S")

# --------------------
# 4. info_logger
# --------------------
info_logger = logging.getLogger("info_logger")
info_logger.setLevel(logging.DEBUG)

if not info_logger.hasHandlers():
    # 파일 핸들러
    file_handler_info = logging.FileHandler(info_log_file, encoding="utf-8")
    file_handler_info.setLevel(logging.DEBUG)
    file_handler_info.setFormatter(formatter)
    info_logger.addHandler(file_handler_info)

    # 콘솔 핸들러
    console_handler_info = logging.StreamHandler()
    console_handler_info.setLevel(logging.INFO)
    console_handler_info.setFormatter(formatter)
    info_logger.addHandler(console_handler_info)

# --------------------
# 5. error_logger
# --------------------
error_logger = logging.getLogger("error_logger")
error_logger.setLevel(logging.ERROR)

if not error_logger.hasHandlers():
    # 파일 핸들러
    file_handler_error = logging.FileHandler(error_log_file, encoding="utf-8")
    file_handler_error.setLevel(logging.ERROR)
    file_handler_error.setFormatter(formatter)
    error_logger.addHandler(file_handler_error)

    # 콘솔 핸들러
    console_handler_error = logging.StreamHandler()
    console_handler_error.setLevel(logging.ERROR)
    console_handler_error.setFormatter(formatter)
    error_logger.addHandler(console_handler_error)