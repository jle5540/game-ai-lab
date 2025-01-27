from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

from ollama import chat
from utils.llm_utils import pretty_stringify_chat, ollama_seed as seed

# Add you code below
sign_your_name = 'Pulin Agrawal'


# But before here.

options |= {'seed': seed(sign_your_name)}
# Chat loop
while True:
  response = chat(model=model, messages=messages, stream=False, options=options)
  # Add your code below


  # But before here.
  if messages[-1]['content'] == '/exit':
    break

# Save chat
with open(Path('lab03/attempts.txt'), 'a') as f:
  f.write('------------------------NEW ATTEMPT------------------------\n\n\n')
  f.write(pretty_stringify_chat(messages))
  f.write('\n\n\n------------------------END OF ATTEMPT------------------------\n\n\n')

