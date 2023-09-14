from seleniumbase import SB
import json, urllib, argparse

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
        sb.open(f"https://you.com/api/streamingSearch?q={qoted_text}&domain=youchat")
        try:
            sb.assert_text("event: youChatIntent", timeout=12)
            data = sb.get_text("body pre")
        except Exception:
            result['error'] = 'Selenium was detected! Try again later.'

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
            str_res = result['error'] if ('error' in result) else result['generated_text']
            return str_res

if __name__=='__main__':     
    parser = argparse.ArgumentParser()
    parser.add_argument('MESSAGE', help="Message to YouChat")
    parser.add_argument('-out_type', '-ot', help="Output type", default="json") 
    args = parser.parse_args()
    text = args.MESSAGE
    print(you_message(text, args.out_type))