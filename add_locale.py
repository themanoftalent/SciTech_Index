from glob import glob
from pathlib import Path

s_added_locale = 'tst-Test-TT'
if s_added_locale == '':
	exit

top_path = Path.cwd()
for s_file_path in glob(f'{top_path}/**/*.md', recursive=True):
	s_file_text = Path(s_file_path).read_text()
	if s_added_locale in s_file_text:
		continue
	ls_line = s_file_text.splitlines()
	ls_content_line = ls_line[2:-1]
	if s_file_path.endswith('_.md'):
		ls_content_line.append(f'| {s_added_locale} |  |')
	else:
		ls_content_line.append(f'| {s_added_locale} |  |  |')
	ls_content_line.sort()

	s_file_text_with_added_locale = ls_line[0] + '\n' + ls_line[1] + '\n'
	for s_line in ls_content_line:
		s_file_text_with_added_locale += s_line + '\n'
	s_file_text_with_added_locale += ls_line[-1]
	Path(s_file_path).write_text(s_file_text_with_added_locale)
