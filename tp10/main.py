import logging

# logging.basicConfig(filename='example.log',format='%(levelname)s:%(message)s',encoding='utf-8', level=logging.DEBUG)
logging.basicConfig(format='%(levelname)s - %(asctime)s - %(message)s',filename='example.log', encoding='utf-8', level=logging.DEBUG)


def main():
    logging.warning('Watch out!')  # will print a message to the console
    logging.info('I told you so')  # will not print anything

if __name__ == '__main__':
    main()
