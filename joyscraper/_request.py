import time
from requests import get
from requests.exceptions import RequestException
from contextlib import closing


def simple_get(url, retry=False, retrycount=0, milliseconds=300):
    response = ''
    triedcount = 0
    while True:
        try:
            with closing(get(url, stream=True)) as resp:
                response = resp.content
            break
        except RequestException:
            if retry is True:
                if triedcount <= retrycount:
                    triedcount += 1
                    if triedcount is not 1:
                        log_error('An error occurred during the request to {0}, Retrying - [{1}]'.format(url, triedcount-1))
                    else:
                        log_error('An error occurred during the request to {0}'.format(url))
                    time.sleep(milliseconds)  # wait X mins before retry
                else:
                    break
            else:
                log_error('An error occurred during the request to {0}'.format(url))
                break
    return response


def is_good_response(resp):
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    print(e)
