from random import choice as select
from string import ascii_letters, digits, punctuation

def get_password(length: int) -> str:

    pass_w = ''
    chars = ascii_letters + digits + punctuation

    for _ in range(length):

        pass_w += select(chars)

    return pass_w

def check_user_data(user, platform):
    create_psw_ls = []
    new_psw_ls = []
    with open("./pass_vault/pass.txt", 'r') as fp:
        pass_list = fp.read().strip()
    create_psw_ls = pass_list.split("\n")
    for i in range(len(create_psw_ls)):
        new_psw_ls.append(create_psw_ls[i].split('||')) 
    
    
    for item in new_psw_ls:
        if user.lower() in item[0].lower().strip() and platform.lower() in item[-1].lower().strip():
            return (True, "You have an account with the same info!")
        else:
            return (False, "")

def set_write_pass(user, text, platform):
    (status, message) = check_user_data(user, platform)
    if status:
        print(message)
        return False
    else:
        with open("./pass_vault/pass.txt", 'a') as fp:
            fp.write(f"{user} || {text} || {platform}")
            fp.write('\n')
        print("password created!")
        return True
    
    

if __name__ == "__main__":
    x = check_user_data('john','microsoft')
    print(x)
    
