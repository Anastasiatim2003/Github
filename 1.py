def valid_data():
 while True:

  username = input()
  password = input()
  password_confirm = input()
  if len(username) < 3:
    print('Логин короткий')
  elif len(username) > 12:
    print('Логин длинный')
  elif len(password) < 6:
    print('Пароль короткий')
  elif password_confirm != password:
      print('Пароль не совпадает!')
  else:
      print('ok')