from bs4 import BeautifulSoup
from urllib2 import urlopen


def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, "lxml")


if __name__ == '__main__':
    my_link = "http://vlab.stern.nyu.edu/analysis/VOL.SPX:IND-R.GARCH"

    soup = make_soup(my_link)
    prediction_tag = soup.find("div", {"id": "sum_prediction"})
    vol_pred_num = prediction_tag.find("strong").encode_contents()
    prediction_line = prediction_tag.encode_contents()
    first_comma_pos = prediction_line.find(',')
    first_colon_pos = prediction_line.find(':')
    prediction_date = prediction_line[first_comma_pos + 2: first_colon_pos]
    # .encode_contents().strip()
    # print type(prediction_tag)
    # print prediction_tag
    print prediction_date
    print vol_pred_num

    params_tag = soup.find("h4")
    print params_tag