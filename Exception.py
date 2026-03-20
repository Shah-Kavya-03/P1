import sys
import logging
def error_message_detail(error:Exception,error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"File: [{file_name}] at line number [{line_number}]: {str(error)}"
    logging.error(error_message)
    return error_message
class MyException(Exception):
    def __init__(self, error_message:str,error_deatil:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_deatil)
    def __str__(self):
        return self.error_message