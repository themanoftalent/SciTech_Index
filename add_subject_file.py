from glob import glob
from pathlib import Path


ls_all_locale = Path('locale.txt').read_text().splitlines()
for i_locale_index in range(len(ls_all_locale)):
	s_locale = ls_all_locale[i_locale_index]
	if s_locale.startswith(' '):
		s_anchor_locale = s_locale.lstrip(' ')
		ls_all_locale[i_locale_index] = s_anchor_locale
		break

s_text = 'locale\tsubject\n'
for s_locale_entry in ls_all_locale:
	s_text += s_locale_entry + '\t\n'

top_path = Path.cwd()
for s_file_directory_path in glob(f'{top_path}/**/*/', recursive=True):
	s_file_name = '_' + s_file_directory_path[s_file_directory_path.rstrip('/').rfind('/')+1:].rstrip('/') + '_.tsv'

	ls_synonym_separator = [',', '،', '꛵', '、', '，', '፣', '𖬹', '꓾', '𖺗', '᠂', '᠈', '𑑍', '߸', '𝪇', '༔', '꘍']
	for s_synonym_separator in ls_synonym_separator:
		if s_synonym_separator in ['、', '，']:
			s_file_name = s_file_name.replace(s_synonym_separator, '_' + s_synonym_separator + '_')
			s_file_name = s_file_name.replace('_' + s_synonym_separator + '__' + s_synonym_separator + '_', s_synonym_separator*2)
		elif s_synonym_separator in ['᠂', '᠈']:
			s_file_name = s_file_name.replace(' ' + s_synonym_separator + ' ', '_ ' + s_synonym_separator + ' _')
			s_file_name = s_file_name.replace('_ ' + s_synonym_separator + ' __ ' + s_synonym_separator + ' _', ' ' + s_synonym_separator*2 + ' ')
		else:
			s_file_name = s_file_name.replace(s_synonym_separator + ' ', '_' + s_synonym_separator + ' _')
			s_file_name = s_file_name.replace(s_synonym_separator + '_' + s_synonym_separator + ' _', s_synonym_separator*2 + ' ')
	file_path = Path(s_file_directory_path).joinpath(s_file_name)
	if not file_path.is_file():
		print(file_path)
		s_text = s_text.replace(s_anchor_locale + '\t', s_anchor_locale + '\t' + s_file_name.removesuffix('.tsv'))
		file_path.write_text(s_text)
