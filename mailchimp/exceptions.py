class ChimpException(Exception): pass

class CampaignDoesNotExist(ChimpException): pass
class ListDoesNotExist(ChimpException): pass
class ConnectionFailed(ChimpException): pass
class TemplateDoesNotExist(ChimpException): pass