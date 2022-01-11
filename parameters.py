""" filename: parameters.py """
try:
    import config
except ImportError:
    import config_example as config

# search query 
search_query = 'site:linkedin.com/in/ AND "freelance grant writer" AND "united states"'


# file were scraped profile information will be stored  
file_name = 'results_file.csv'

# login credentials
linkedin_username = config.linkedin_username
linkedin_password = config.linkedin_password

