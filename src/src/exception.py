class DataProcessingException(Exception):
    """Exception raised for errors in data processing."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ModelTrainingException(Exception):
    """Exception raised for errors in model training."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class RecommendationException(Exception):
    """Exception raised for errors in generating recommendations."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
