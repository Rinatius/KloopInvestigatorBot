import strings as s
import constants as c
import botsearcher as bs
import dialogflow_tools as dft


class BotCommand(object):

    def __init__(self):
        self.start_text = s.start_text

    def serve(self, user):
        user.update_service_messages(self.start_text)

    def search(self, query, user):

        if query[0] == c.LITERAL_SEARCH_SYMBOL:
            self.literal_search(query[1:], user)
        elif query[0] == c.SERVICE_SYMBOL:
            self.serve(user)
        else:
            self.complex_search(query, user)

    @staticmethod
    def literal_search(query, user):

        bot_searcher = bs.BotSearcher()
        df = bot_searcher.find_company(query)

        user.current_result = df
        user.current_query = query

    @staticmethod
    def complex_search(query, user):

        query_dialogflow = dft.prepare_for_dialogflow(query)
        response = dft.dialogflow_request(query_dialogflow)

        try:
            bot_searcher = bs.BotSearcher()
            search_method = getattr(bot_searcher, response["result"]["metadata"]["intentName"])
            df = search_method(**response["result"]["parameters"])

            user.current_result = df
            user.current_query = query
        except AttributeError:
            user.update_service_messages(s.function_not_ready)
