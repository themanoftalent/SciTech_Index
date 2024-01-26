from glob import glob
from pathlib import Path


s_added_locale = 'zzz-Zzzz-ZZ'
if s_added_locale == '':
	exit

top_path = Path.cwd()
for s_file_path in glob(f'{top_path}/**/*.tsv', recursive=True):
	s_file_text = Path(s_file_path).read_text()
	if s_added_locale in s_file_text:
		continue

	ls_text_in_line = s_file_text.splitlines()
	ls_header = ls_text_in_line.pop(0)

	if s_file_path.startswith('_'):
		ls_text_in_line.append(s_added_locale + '\t')
	else:
		ls_text_in_line.append(s_added_locale + '\t'*2)
	ls_text_in_line.sort()

	s_file_text_with_added_locale = ls_header + '\n'
	for s_line in ls_text_in_line:
		s_file_text_with_added_locale += s_line + '\n'
	Path(s_file_path).write_text(s_file_text_with_added_locale)
