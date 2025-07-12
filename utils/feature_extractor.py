
import re

def extract_features(url):
    features = {}
    features['have_ip'] = 1 if re.search(r'(\d+\.\d+\.\d+\.\d+)', url) else 0
    features['url_length'] = len(url)
    features['have_at_symbol'] = 1 if '@' in url else 0
    features['prefix_suffix'] = 1 if '-' in url else 0
    features['https_token'] = 1 if 'https' in url.lower() and 'https://' not in url.lower() else 0
    return list(features.values())
