import re,pyperclip

user_text=pyperclip.paste()


def email_regex(user_text):
    email_pattern=re.compile(r"\b[A-Za-z0-9._-]+@\w+\.[a-zA-Z]{2,}\b")
    email_match=email_pattern.findall(user_text)
    return email_match


def phone_num_regex(user_text):
    phone_num_pattern=re.compile(r"""(?:\b\d{10}\b)
                                 
                                 |

                                 (?:\b\+\d{1,3}[ -]?\d{10}\b)

                                 |

                                 (?:\b\d{3}[ .-]\d{3}[ .-]\d{4}\b)

                                 |

                                 (?:\(\d{3}\) \d{3}[ -]\d{4}\b)

                                 
                                 """,re.VERBOSE)
    phone_num_match=phone_num_pattern.findall(user_text)
    return phone_num_match

def date_regex(user_text):
    date_pattern=re.compile(r"""
                            \d{1,2}/\d{1,2}/\d{4}
                            |
                            \d{1,2}-\d{1,2}-\d{4}
                            |
                            \d{4}-\d{1,2}-\d{1,2}
                            |
                            \d{4}/\d{1,2}/\d{1,2}
                            
""",re.VERBOSE)
    date_match=date_pattern.findall(user_text)
    return date_match

def url_regex(user_text):
    url_pattern=re.compile(r"(?:https?://)?(?:www\.)?(?:[A-Za-z0-9-]+\.[a-z0-9]{2,63})(?:(?:(?:/[A-Za-z0-9_-]+)+)?)\b")
    url_match=url_pattern.findall(user_text)
    return url_match


def analyzer(user_text):
    master_dict={}
    email=set(email_regex(user_text))
    phone=set(phone_num_regex(user_text))
    date=set(date_regex(user_text))
    url=set(url_regex(user_text))
    master_dict["Phone numbers"]=phone
    master_dict["Emails"]=email
    master_dict["Dates"]=date
    master_dict["Web URLs"]=url
    for x in master_dict:
        print(f"{x:=^100}\n")
        if not master_dict[x]:
            print(f"Not found!")
        
        else:
            for y in master_dict[x]:
                print(f"-> {y}")
    print()

    
    for x in master_dict:
        print(f"{x} found : {len(master_dict[x])}")
    
analyzer(user_text)


    

                



                

    

