# server.py
from os import path

from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base
from rich import print as pp

writing_sample_path = "./doc/writing_sample.txt"
if path.exists(writing_sample_path):
    pp(f"[bold green]Found writing sample at {writing_sample_path}[/]")
    with open(writing_sample_path, "r") as f:
        writing_sample = f.read()
else:
    pp(f"[bold yellow][Warning] {writing_sample_path} not found![/]")
    writing_sample = """Social media have become a major source of news and information for American citizens (Walker & Matsa, 2021) where journalists monitor public opinion and popular trends (Tandoc Jr & Vos, 2016), and newsrooms try to attract audiences and traffic (Wojcieszak et al., 2021). One important way in which social media have changed journalism lies in the use of engagement metrics: these metrics, such as the number of likes, reactions, shares, collectively signal what audiences demand, and may, in turn dictate news organizations’ priorities in content production (Christin, 2020; Tandoc Jr & Vos, 2016). The incorporation of social media metrics ..."""
# Create an MCP server
mcp = FastMCP("Demo")


# @mcp.resource("config://writing_sample")
# def get_config(writing_sample=writing_sample) -> str:
#     """Static configuration data"""
#     return writing_sample


@mcp.prompt()
def write_like_subhayan(writing: str, writing_sample: str = writing_sample) -> str:
    """
    This function is used to create a prompt in order to write like Subhayan.
    """
    pp("[bold blue]Processing writing review...[/]")
    return """Please review this academic writing, to make it clear, coherent, concise, and cohesive:\n\n`{writing}`\n\nAccording to the writing sample:\n\n`{writing_sample}`\n\nOnly return the result without quotes. Do not run the function twice, just return the result.\n\n"""


@mcp.tool()
def rewrite(writing: str) -> str:
    """Echo a message as a tool"""
    return f"""1. run function `write_like_subhayan` with the following arguments:\n\n`{writing}`\n\n2. once you get the first result, parse `content[0]['text']` from it and return the result without quotes."""


if __name__ == "__main__":
    mcp.run()
