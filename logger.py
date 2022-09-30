from datetime import datetime



def calc_logger(x, y, action, sum):
    time = datetime.now().strftime()
    with open('logger.txt', 'a') as file:
        file.writelines('{} : {} {} {} = {}\n'.format(x, y, action, sum))


# Не разобрался куда его всунуть