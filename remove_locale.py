from glob import glob
from pathlib import Path

s_removed_locale = 'tst-Test-TT'
if s_removed_locale == '':
	exit

top_path = Path.cwd()
for s_file_path in glob(f'{top_path}/**/*.md', recursive=True):
	s_file_text = Path(s_file_path).read_text()
	ls_line = s_file_text.splitlines()
	s_text_with_removed_locale = ''
	for s_line in ls_line:
		if not s_line.startswith('| ' + s_removed_locale):
			s_text_with_removed_locale += s_line + '\n'
	Path(s_file_path).write_text(s_text_with_removed_locale)
