from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()

results = search_tool.invoke('weather kot mithan wang today')

print(results)

print(search_tool.name)
print(search_tool.description)
print(search_tool.args)

# from langchain_community.tools import ShellTool

# shell_tool = ShellTool()

# results = shell_tool.invoke('dir')

# print(results)