def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist.")
    else:
        return (x % m + m) % m

message_obj =  open("message.txt", "r")
message_text = message_obj.read()
message_text = message_text.split(" ")

while message_text[-1] == '':
    message_text.pop()

decrypted_message_str = ""

for number in message_text:
    mod41inv = mod_inverse(int(number), 41)
    if mod41inv <= 26: decrypted_message_str += str(chr(mod41inv + 64))
    elif mod41inv <= 36: decrypted_message_str += str(mod41inv - 27)
    elif mod41inv == 37: decrypted_message_str += "_"
    else: print("Something is wrong.")

print("picoCTF{" + decrypted_message_str + "}")