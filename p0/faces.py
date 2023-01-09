''' convert emoticons into faces
    :) = 🙂 and :( = 🙁
    '''
name = input()
name_converted = name.replace(':)','🙂').replace(':(','🙁')

print(name_converted)
