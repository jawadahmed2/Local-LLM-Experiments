import os
import subprocess
from huggingface_hub import hf_hub_download


# Change the current working directory
os.chdir('SciAgentsDiscovery')

# Install the package using pip with quiet mode (-q)
subprocess.run(['pip', 'install', '-e', '.', '-q'], check=True)


os.environ['OPENAI_API_KEY']="ollama"

# SemanticScholar_api_key = ''
# os.environ['SEMANTIC_SCHOLAR_API_KEY']=SemanticScholar_api_key

SERPER_API_KEY=""
os.environ['SERPER_API_KEY']=SERPER_API_KEY

data_dir_output='./graph_giant_component_LLMdiscovery_example/'


def download_required_files():
    # Create the directory if it doesn't exist
    os.makedirs('./graph_giant_component', exist_ok=True)

    # List of files to download
    files_to_download = [
        'large_graph_simple_giant.graphml',
        'embeddings_simple_giant_ge-large-en-v1.5.pkl'
    ]

    # Download each file
    for filename in files_to_download:
        file_path = hf_hub_download(
            repo_id='lamm-mit/bio-graph-1K',
            filename=filename,
            local_dir='./graph_giant_component'
        )
        print(f"Downloaded {filename} to {file_path}")

# Call this function before initializing your ScienceDiscovery module
download_required_files()

from ScienceDiscovery import *


res = user.initiate_chat(recipient=manager,
message='''Develop a research proposal using random concepts. In the end, rate the novelty and feasibility of the research idea.''',
                        clear_history=True)

print(res)