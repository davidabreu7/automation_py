import re

def check_web_address(text):
  pattern = r"[A-Za-z\\\+\-\_]*\.[A-Za-z\\\+\-\_]*$"
  result = re.search(pattern, text)
  # print(result)
  return result != None

def check_time(text):
    pattern = r"[0-12]*\:[0-59]+.*[amAMpmPM]"
    result = re.search(pattern, text)
    # print(result)

    return result != None


def contains_acronym(text):
  pattern = r"\(.*[A-Za-z].*\)"
  result = re.search(pattern, text)
  print(result)
  return result != None


def check_zip_code (text):
  result = re.search(r".+[\d]{5}", text)
  print(result)
  return result != None


def transform_record(record):
  new_record = re.sub(r"(.*),(.*),(.*)", r"\1,+1-\2,\3",record)
  return new_record


def multi_vowel_words(text):
  pattern = r"\w*[aeiou]{3,}\w*"
  result = re.findall(pattern, text)
  return result


def transform_comments(line_of_code):
  result = re.sub(r"(\w*)(#{1,3})(.*)", r"\1//\3", line_of_code)
  return result


def convert_phone_number(phone):
  result = re.sub(r"(\d*)-(\d*)-(\d*)", r"(\1) \2-\3", phone)
  return result

