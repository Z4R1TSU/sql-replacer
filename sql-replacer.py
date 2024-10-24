def replace_question_marks(text, replacements):
  """
  将多行字符串中的问号替换为字符串数组中的对应字符串。

  Args:
    text: 包含多个问号的多行字符串
    replacements: 包含对应字符串的数组

  Returns:
    替换后的字符串
  """
  if len(replacements) != text.count("?"):
    raise ValueError("问号数量与替换字符串数量不匹配")

  i = 0
  result = text
  for replacement in replacements:
    result = result.replace("?", str(replacement), 1)
    i += 1
  return result

# --------------------- 下面可以修改要处理的SQL语句和要替换的信息

sql_string = '''
?
'''

params = [1]

real_sql = replace_question_marks(sql_string, params)

print(f"Real SQL: {real_sql}")  # 打印最终替换后的 SQL 语句