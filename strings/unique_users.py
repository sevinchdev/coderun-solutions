def normalize(email):
  username, domain = email.split("@")

  username = username.split("-")[0]
  username = username.replace(".","")

  domain = domain.rsplit(".",1)[0]

  return username + "@" + domain

n = int(input())
unique_users = set()

for i in range(n):
  email = input()
  email = normalize(email)

  unique_users.add(email)

  print(len(unique_users))

  