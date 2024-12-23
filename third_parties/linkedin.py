from dotenv import load_dotenv
import os
import requests

load_dotenv(override=True)


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """
    Scrape a person's LinkedIn profile
    """
    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/amirstm/b5ef8ed221791e6f0e3073588982bfb5/raw/5a41c20f688493a04ebb917963f3527cdf935785/amirstm_linkedin.json"
        response = requests.get(linkedin_profile_url, timeout=10)
    else:
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
        response = requests.get(
            api_endpoint,
            params={"url": linkedin_profile_url},
            headers=header_dic,
            timeout=10,
        )
    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")
    return data


if __name__ == "__main__":
    print(scrape_linkedin_profile("https://linkedin.com/in/amirstm", mock=True))
