# from langchain_community.chat_models import ChatOpenAI
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.runnables import ConfigurableField

# WRITER_SYSTEM_PROMPT = "You are an AI critical thinker research assistant. Your sole purpose is to write well written, critically acclaimed, objective and structured reports on given text."  # noqa: E501


# # Report prompts from https://github.com/assafelovic/gpt-researcher/blob/master/gpt_researcher/master/prompts.py
# RESEARCH_REPORT_TEMPLATE = """Information: 
# --------
# {research_summary}
# --------

# Using the above information, answer the following question or topic: "{question}" in a detailed report -- \
# The report should focus on the answer to the question, should be well structured, informative, \
# in depth, with facts and numbers if available and a minimum of 1,200 words.

# You should strive to write the report as long as you can using all relevant and necessary information provided.
# You must write the report with markdown syntax.
# You MUST determine your own concrete and valid opinion based on the given information. Do NOT deter to general and meaningless conclusions.
# Write all used source urls at the end of the report, and make sure to not add duplicated sources, but only one reference for each.
# You must write the report in apa format.
# Please do your best, this is very important to my career."""  # noqa: E501


# RESOURCE_REPORT_TEMPLATE = """Information: 
# --------
# {research_summary}
# --------

# Based on the above information, generate a bibliography recommendation report for the following question or topic: "{question}". \
# The report should provide a detailed analysis of each recommended resource, explaining how each source can contribute to finding answers to the research question. \
# Focus on the relevance, reliability, and significance of each source. \
# Ensure that the report is well-structured, informative, in-depth, and follows Markdown syntax. \
# Include relevant facts, figures, and numbers whenever available. \
# The report should have a minimum length of 1,200 words.

# Please do your best, this is very important to my career."""  # noqa: E501

# OUTLINE_REPORT_TEMPLATE = """Information: 
# --------
# {research_summary}
# --------

# Using the above information, generate an outline for a research report in Markdown syntax for the following question or topic: "{question}". \
# The outline should provide a well-structured framework for the research report, including the main sections, subsections, and key points to be covered. \
# The research report should be detailed, informative, in-depth, and a minimum of 1,200 words. \
# Use appropriate Markdown syntax to format the outline and ensure readability.

# Please do your best, this is very important to my career."""  # noqa: E501

# model = ChatOpenAI(temperature=0, model="gpt-4")
# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", WRITER_SYSTEM_PROMPT),
#         ("user", RESEARCH_REPORT_TEMPLATE),
#     ]
# ).configurable_alternatives(
#     ConfigurableField("report_type"),
#     default_key="research_report",
#     resource_report=ChatPromptTemplate.from_messages(
#         [
#             ("system", WRITER_SYSTEM_PROMPT),
#             ("user", RESOURCE_REPORT_TEMPLATE),
#         ]
#     ),
#     outline_report=ChatPromptTemplate.from_messages(
#         [
#             ("system", WRITER_SYSTEM_PROMPT),
#             ("user", OUTLINE_REPORT_TEMPLATE),
#         ]
#     ),
# )
# chain = prompt | model | StrOutputParser()


###################################


# from langchain_community.chat_models import ChatOpenAI
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.runnables import RunnablePassthrough
# from research_assistant.search.web import chain as search_chain

# WRITER_SYSTEM_PROMPT = "You are an AI critical thinker research assistant. Your sole purpose is to write well written, critically acclaimed, objective and structured reports on given text."  # noqa: E501

# COURSE_OUTLINE_TEMPLATE = """Information: 
# --------
# {research_summary}
# --------

# Using the above information, generate a course outline on the following topic: "{question}". \
# The outline should be well-structured, informative, and include main sections and subsections. \
# Use appropriate Markdown syntax to format the outline and ensure readability.

# Please do your best, this is very important to my career."""  # noqa: E501

# COURSE_CONTENT_TEMPLATE = """Outline: 
# --------
# {course_outline}
# --------

# Using the above outline, generate detailed and lengthy content for each section and subsection of the course on the topic: "{question}". \
# The content should be well-structured, informative, and in-depth. \
# Use appropriate Markdown syntax to format the content and ensure readability.

# Please do your best, this is very important to my career."""  # noqa: E501

# outline_model = ChatOpenAI(temperature=0)
# content_model = ChatOpenAI(temperature=0.7)

# outline_prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", WRITER_SYSTEM_PROMPT),
#         ("user", COURSE_OUTLINE_TEMPLATE),
#     ]
# )

# content_prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", WRITER_SYSTEM_PROMPT),
#         ("user", COURSE_CONTENT_TEMPLATE),
#     ]
# )

# chain = RunnablePassthrough().assign(research_summary=search_chain) | outline_prompt | outline_model | StrOutputParser()
# chain = RunnablePassthrough().assign(course_outline=chain) | content_prompt | content_model | StrOutputParser()


#####################

from langchain_community.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from research_assistant.search.web import chain as search_chain

WRITER_SYSTEM_PROMPT = "You are an AI creative assistant specialized in social media content. Your purpose is to help users craft engaging, viral-worthy video scripts for platforms like TikTok and Instagram Reels. Utilize cutting-edge strategies and creative elements to ensure the scripts are captivating, actionable, and designed to maximize viewer engagement and shareability." 

VIRAL_VIDEO_SCRIPT_TEMPLATE = """Information: 
--------
{research_summary}
--------

Using the above information and the topic provided: "{question}", generate a script for a short-form video designed for TikTok and Instagram Reels. The script should include a compelling hook, maintain high energy and engagement throughout, and conclude with a strong payoff. Ensure the script is actionable, utilizes viral elements, and aligns with best practices for content that tends to perform well on these platforms.

Please make this script creative and engaging, as it is critical for capturing audience attention quickly."""

outline_model = ChatOpenAI(temperature=0)
content_model = ChatOpenAI(temperature=0.7)

viral_video_script_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", WRITER_SYSTEM_PROMPT),
        ("user", VIRAL_VIDEO_SCRIPT_TEMPLATE),
    ]
)
chain = RunnablePassthrough().assign(research_summary=search_chain) | viral_video_script_prompt | StrOutputParser()