from glob import glob
from pathlib import Path

s_anchor_locale = 'eng-Latn-US'

top_path = Path.cwd()
for s_file_path in glob(f'{top_path}/*/**/', recursive=True):
	s_file_name = '_' + s_file_path[s_file_path.rstrip('/').rfind('/')+1:].rstrip('/') + '_.md'
	file_path = Path(s_file_path).joinpath(s_file_name)
	s_text = file_path.read_text()
	ls_text_line = s_text.splitlines()
	for s_line in ls_text_line:
		if s_line.startswith('| ' + s_anchor_locale +  ' | '):
			if s_line.rstrip() == '| ' + s_anchor_locale +  ' | ' + s_file_name.rstrip('.md') +  ' |':
				continue
			print('| ' + s_anchor_locale +  ' | ' + s_file_name.rstrip('.md') +  ' |')
