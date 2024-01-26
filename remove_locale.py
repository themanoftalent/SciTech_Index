from glob import glob
from pathlib import Path


s_removed_locale = 'zzz-Zzzz-ZZ'
if s_removed_locale == '':
	exit

top_path = Path.cwd()
for s_file_path in glob(f'{top_path}/**/*.tsv', recursive=True):
	s_file_text = Path(s_file_path).read_text()
	if s_removed_locale not in s_file_text:
		continue

	ls_text_in_line = s_file_text.splitlines()
	s_text_with_removed_locale = ''
	for s_line in ls_text_in_line:
		if not s_line.startswith(s_removed_locale):
			s_text_with_removed_locale += s_line + '\n'
	Path(s_file_path).write_text(s_text_with_removed_locale)
