from langchain_community.document_loaders import GithubFileLoader

loader = GithubFileLoader(
    repo="langchain-ai/langchain",  # the repo name
    branch="master",  # the branch name
    access_token="",
    github_api_url="https://api.github.com",
    file_filter=lambda file_path: file_path.endswith(
        ".md"
    ),  # load all markdowns files.
)
documents = loader.load()
print(documents)