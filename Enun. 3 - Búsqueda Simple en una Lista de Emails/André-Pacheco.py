emails = ['ana@gmail.com', 'luis@outlook.com', 'mia@gmail.com', 'juan@yahoo.com']

count_gmail = sum(1 for email in emails if email.endswith('@gmail.com'))
print(f"1) Cantidad de emails de Gmail: {count_gmail}")

emails_com = [email for email in emails if email.endswith('.com')]
print("2) Emails que terminan en '.com':", emails_com)

existe_luis = 'luis@outlook.com' in emails
print(f"3) ¿'luis@outlook.com' está en la lista?: {existe_luis}")
