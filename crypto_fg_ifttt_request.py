import requests
from datetime import datetime


def get_fng_data(url):
    """Gets latest BTC FNG index"""
    try:
        data = requests.get(url).json()
        value = data.get('data')[0].get('value')
        classification = data.get('data')[0].get('value_classification')
        return value, classification
    except IndexError as e:
        print('[{}] {} {}'.format(datetime.now(), type(e), e))


def create_payload(index_value, classification):
    """Writes json payload with information to provide to IFTTT"""
    dict = {"value1": classification, "value2": index_value}
    return dict


def send_ifttt_request(event, api_key, data):
    """Sends event to IFTTT"""
    maker_url = 'https://maker.ifttt.com/trigger/{}/with/key/{}'.format(event, api_key)
    print("Sending request to IFTTT")
    requests.post(maker_url, data=data)


if __name__ == '__main__':
    api_key = 'YOURKEYHERE'
    event = 'crypto_fg_index'
    fng_url = 'https://api.alternative.me/fng/'
    index_value, classification = get_fng_data(fng_url)
    data = create_payload(index_value, classification)
    send_ifttt_request(event, api_key, data)
    # print(json_file)
