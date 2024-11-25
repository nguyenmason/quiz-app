import requests

class QuizAPI:
    """
    A class to interact with the Open Trivia Database API to fetch quiz questions.
    """
    def __init__(self):
        self.questions_url = "https://opentdb.com/api.php?amount=10&type=multiple"
        self.categories_url = "https://opentdb.com/api_category.php"

    def get_questions(self, category):
        """
        Fetches quiz questions from the Open Trivia Database API. Returns an empty list if an error is raised
        """
        try:
            response = requests.get(self.questions_url + "&category=" + str(self.get_categories()[category]))
            response.raise_for_status()  # Raise an exception for HTTP errors
            questions = response.json()
            return questions['results']
        except requests.exceptions.RequestException as e:
            return []
        
    def get_categories(self):
        try:
            response = requests.get(self.categories_url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            categories = response.json()
            return  {entry['name']: entry['id'] for entry in categories["trivia_categories"]}
        except requests.exceptions.RequestException as e:
            return []