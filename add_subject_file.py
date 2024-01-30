from glob import glob
from pathlib import Path


s_locale_file = 'locale.txt'
s_subject_header_file = 'subject_header.txt'

ls_locale = Path(s_locale_file).read_text().splitlines()
for i_locale_index in range(len(ls_locale)):
	s_locale = ls_locale[i_locale_index]
	if s_locale.startswith(' '):
		s_principal_locale = s_locale.lstrip(' ')
		ls_locale[i_locale_index] = s_principal_locale
		break

s_text = Path(s_subject_header_file).read_text().strip() + '\n'
for s_locale_entry in ls_locale:
	s_text += s_locale_entry + '\t\n'

top_path = Path.cwd()
for s_file_directory_path in glob(f'{top_path}/**/*/', recursive=True):
	s_file_name = '_' + s_file_directory_path[s_file_directory_path.rstrip('/').rfind('/')+1:].rstrip('/') + '_.tsv'

	ls_synonym_separator = [', ', '، ', '꛵ ', '、', '，', '፣ ', '𖬹 ', '꓾ ', '𖺗 ', ' ᠂ ', ' ᠈ ', '𑑍 ', '߸ ', '𝪇', '༔ ', '꘍ ']
	for s_synonym_separator in ls_synonym_separator:
		s_file_name = s_file_name.replace(s_synonym_separator, '_' + s_synonym_separator + '_')
		s_file_name = s_file_name.replace('_' + s_synonym_separator + '__' + s_synonym_separator + '_', s_synonym_separator*2)
	file_path = Path(s_file_directory_path).joinpath(s_file_name)
	if not file_path.is_file():
		print(file_path)
		file_path.write_text(s_text.replace(s_principal_locale + '\t', s_principal_locale + '\t' + s_file_name.removesuffix('.tsv')))
