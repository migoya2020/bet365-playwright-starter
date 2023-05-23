import os
from bet365_loader import launchBrowser, logger


# just make sure we have playwright browsers installed
try:
    os.system('playwright install')
except:
    pass

def main():
    launchBrowser()
    
if __name__ == '__main__':
    logger.info("Main app starts....")
    main()