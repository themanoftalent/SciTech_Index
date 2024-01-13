from glob import glob
from pathlib import Path

s_anchor_locale = 'eng-Latn-US'

top_path = Path.cwd()
for s_file_path in glob(f'{top_path}/**/*.md', recursive=True):
	s_text = Path(s_file_path).read_text()
	ls_text_line = s_text.splitlines()
	for s_line in ls_text_line:
		if not s_line.startswith('| ' + s_anchor_locale +  ' | '):
			continue
		i_item_start_index = len('| ' + s_anchor_locale +  ' | ')
		i_item_end_index = i_item_start_index + s_line[i_item_start_index:].find(' |')
		s_item = s_line[i_item_start_index:i_item_end_index]

		s_file_name = s_file_path[s_file_path.rfind('/')+1:].removesuffix('.md')

		if s_item != s_file_name:
			print(s_item)
			print(s_file_path)
			print()
