from seleniumbase import SB
import json
import urllib
import argparse
import time


def you_message(text: str, out_type: str = 'json'):
    """Function to send a message and get results from YouChat.com

    Args:
        text (str): text to send
        out_type (str): type of result (json, string). Defaults to 'json'.


    Returns:
        str: response of the message
    """
    qoted_text = urllib.parse.quote_plus(text)
    result = {}
    data = ""
    with SB(uc=True) as sb:
        sb.open(
            f"https://you.com/api/streamingSearch?q={qoted_text}&domain=youchat")
        timeout = time.time() + 15  # Timeout - 15 sec
        stream_available = False
        while time.time() <= timeout:
            try:
                sb.assert_text("event: youChatIntent", timeout=0.1)
                stream_available = True
            except Exception:
                pass

            # Try to easy solve captcha challenge
            try:
                if sb.assert_element('iframe'):
                    sb.switch_to_frame("iframe")
                    sb.find_element(".ctp-checkbox-label", timeout=0.1).click()
                    sb.switch_to_default_content()
                    # sb.save_screenshot('sel2.png') # Debug
            except Exception:
                result['error'] = 'Selenium was detected! Try again later. Captcha not solved automaticly.'

            if stream_available:
                result.pop('error')
                data = sb.get_text("body pre")
                break
            

        res_message = ""
        for line in data.split("\n"):
            if line.startswith("data: {"):
                json_data = json.loads(line[5:])
                if 'youChatToken' in json_data:
                    res_message += json_data['youChatToken']
        result['generated_text'] = res_message

        if out_type == 'json':
            return json.dumps(result)
        else:
            str_res = result['error'] if (
                'error' in result) else result['generated_text']
            return str_res


def main_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('MESSAGE', help="Message to YouChat")
    parser.add_argument('-out_type', '-ot', help="Output type", default="json")
    args = parser.parse_args()
    text = args.MESSAGE
    print(you_message(text, args.out_type))


if __name__ == '__main__':
    main_cli()
