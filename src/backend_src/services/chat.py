import logging
from src.agents_src.crew import qa_crew

logger = logging.getLogger(__name__)


def get_answer(chat_history: list) -> dict:
    logger.info(f"Received chat_history: {chat_history}")
    # get the last message in the chat_history as user_query
    last_user_message = chat_history[-1]
    user_query = last_user_message["content"]
    logger.info(f"Extracted user_query: {user_query}")
    # Remove the last user message from chat_history
    history_without_last = chat_history[:-1]
    input_data = {
        "user_query": user_query,
        "chat_history": history_without_last,
    }
    logger.debug(f"Input data for qa_crew: {input_data}")
    result = qa_crew.kickoff(input_data)
    result_dict = result.to_dict()
    logger.info(f"Result from qa_crew: {result_dict}")
    return result_dict


# Example usage
# sample_chat_history = [
#     {"role": "user", "content": "What is Evolution?"},
#     {"role": "assistant", "content": "Evolution is the scientific theory describing how all life forms on Earth change over successive generations through alterations in their genetic material, leading to the diversity of life seen today. This process involves changes in an organism's genetic makeup (genome), which result from processes like mutation and are influenced by natural selection, where individuals with advantageous traits for their environment leave more offspring."},
#     {"role": "user", "content": "Explain in detail"}
# ]
# response = get_answer(sample_chat_history)
# print(response)