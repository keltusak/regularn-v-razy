# Přijímá hesla o délce 8-16 znaků, obsahující alespoň jedno velké písmeno, jedno číslo a jeden speciální znak.
import re

def validate_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,16}$'
    return bool(re.match(pattern, password))