from glob import glob
from pathlib import Path


s_locale_file = 'locale.txt'

ls_locale = Path(s_locale_file).read_text().splitlines()
for i_locale_index in range(len(ls_locale)):
	s_locale = ls_locale[i_locale_index]
	if s_locale.startswith(' '):
		s_principal_locale = s_locale.lstrip(' ')
		ls_locale[i_locale_index] = s_principal_locale
		break

top_path = Path.cwd()
for s_file_path in glob(f'{top_path}/**/*.tsv', recursive=True):
	s_file_text = Path(s_file_path).read_text()
	ls_text_in_line = s_file_text.splitlines()
	s_header = ls_text_in_line.pop(0)

	ls_updated_entry = []
	for s_locale in ls_locale:
		for s_line in ls_text_in_line:
			if s_locale == s_line[:s_line.find('\t')]:
				ls_updated_entry.append(s_line)
				break
		else:
			ls_updated_entry.append(s_locale + '\t'*s_header.count('\t'))
	ls_updated_entry.sort()

	s_updated_file_text = s_header + '\n'
	for s_entry_line in ls_updated_entry:
		s_updated_file_text += s_entry_line + '\n'

	if s_updated_file_text != s_file_text:
		Path(s_file_path).write_text(s_updated_file_text)
