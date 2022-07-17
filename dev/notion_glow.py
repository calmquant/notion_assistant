"""
Library for interaction with generic parts of the Notion Glow template

Namely, core databases - Todos, Notes and Bookmarks

And core item types
    - Application
    - Process
    - Project
    - Context

    - Working session
"""
from notion_assistant.javris.notion_client import NotionClient


class GlowNotionClient(NotionClient):

    def find_page(self, query, context=None):
        pass
        # todo: support shortcuts
        # todo: narrow search to main item types

        # todo: fancy dynamic heuristics
        # dynamically expand/narrow search based on # of results

        # request additional info from user via telegram
