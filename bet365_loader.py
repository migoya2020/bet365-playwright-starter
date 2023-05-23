import datetime
import os
from playwright.sync_api import sync_playwright, Page, expect, WebSocket
from loguru import logger


current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file = f"bet365app_{current_time}.log"
logger.add(log_file, rotation="500 MB",
           format="{time} - {level} - {message}", enqueue=True)

dir_path = os.path.dirname(os.path.realpath(__file__))
BASE_URL='https://www.bet365.com/#/IP/B1'

DEFAULT_ARGS = [
    # '--disable-background-networking',
    '--enable-features=NetworkService,NetworkServiceInProcess',
    # '--disable-background-timer-throttling',
    # '--disable-backgrounding-occluded-windows',
    # '--disable-breakpad',
    # '--disable-client-side-phishing-detection',
    # '--disable-component-extensions-with-background-pages',
    # '--disable-default-apps',
    # '--disable-dev-shm-usage',
    # '--disable-extensions',
    # // BlinkGenPropertyTrees disabled due to crbug.com/937609
    # '--disable-features=TranslateUI,BlinkGenPropertyTrees,ImprovedCookieControls,SameSiteByDefaultCookies,LazyFrameLoading',
    # '--disable-hang-monitor',
    # '--disable-ipc-flooding-protection',
    # '--disable-popup-blocking',
    # '--disable-prompt-on-repost',
    # '--disable-renderer-backgrounding',
    # '--disable-sync',
    # '--force-color-profile=srgb',
    # '--metrics-recording-only',
    # '--no-first-run',
    '--enable-automation',
    # '--incognito',
    # '--password-store=basic',
    # '--use-mock-keychain',
    # '--no-sandbox',
    # '--hide-scrollbars',
    # '--mute-audio',
]
myargs = ["--start-maximized", "--disable-dev-shm-usage", '--enable-gpu-debugging', '--allow-http-screen-capture', '--autoplay-policy=no-user-gesture-required','--ash-enable-software-mirroring', '--ash-enable-stable-overview-order', '--no-sandbox', '--ignore-certificate-errors', '--disable-blink-features=AutomationControlled',  '--"(useAutomationExtension", True)']
request_headers = {
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en',
    #'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    #   'Cookie': 'rmbs=3; cc=1; state=114; _ga=GA1.1.1094883960.1677152006; bet365SportsExtra=settings=0,0,0,0,0,22,0,,0,0; _ga_45M1DQFW2B=GS1.1.1678782591.4.0.1678782591.0.0.0; Affiliates=Code=365_01399169%2f169841434211&prd=Sports; aps03=cf=N&cg=1&cst=0&ct=102&hd=N&lng=1&oty=2&tzi=22; __cf_bm=DtlgfLYbio1AL7S89NhrVQ1r8o7P7RHi8NdH_nxEoZg-1679049547-0-AcCiXGJx0xkqH7eVC9x3E7xAszBECfbTM577ilqR9D1INHGFl80XKrdOOZhYXIMGNcGCX4m5e92RP47eixDV70E=; pstk=046457F4A16F4A61B041BFFEC7416D90000003; swt=AS3aLomj0ArLiLHrOXv3P4IsOqgNH+aAN6pqaMkKDbLlXTAGrLlPuKHLByf2q8gAPFoWqKyQuiz4Zuzyl9k3o92XQNmgEp/f5bK3kZsaUWnW1PBEsluqCpNl8cq3uUZ5auPHaCC6uzbFIJc4VZ7IXnHMJJJOFVj6MoRQbx6OLw==',
    #   'Sec-Fetch-Dest': 'document',
    #   'Sec-Fetch-Mode': 'navigate',
    #   'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}


def launchBrowser():
    with sync_playwright() as pw:
        # create browser instance
        # browser = pw.firefox.launch_persistent_context(no_viewport=True, channel='firefox', ignore_https_errors=True, bypass_csp=False, java_script_enabled=True,ignore_default_args=DEFAULT_ARGS,  user_data_dir=dir_path+"/firefoxProfile", headless=False,  extra_http_headers=request_headers)
        # Uncomment to use Chromium
        browser = pw.chromium.launch_persistent_context(no_viewport=True, channel='chrome',ignore_https_errors=True,bypass_csp=False, java_script_enabled=True,  ignore_default_args=DEFAULT_ARGS, user_data_dir=dir_path+"/chromeProfile",headless=False,  extra_http_headers=request_headers)
        
        # create page instance
        page = browser.new_page()
        initial_response = page.goto(BASE_URL)
        # page.locator("button", has_text="Accept all and continue").wait_for()
        logger.info(f"Initial Response: {initial_response.status}")
        logger.info("Page Title: {}", page.title())

         
        # Wait for this section to be visible
        inplay_div_locator = page.locator("div.wcl-PageContainer_Colcontainer")
        expect(inplay_div_locator).to_be_visible(timeout=40000)
        logger.info(f"Browser is loaded sucessfully...")
        page.wait_for_event("websocket", timeout=0)
