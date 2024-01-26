from glob import glob
from pathlib import Path


s_export_directory = 'Markdown'

s_locale_file = 'locale.txt'

ls_locale = Path(s_locale_file).read_text().splitlines()
for s_locale in ls_locale:
	if s_locale.startswith(' '):
		s_anchor_locale = s_locale.strip()
		break

def s_get_item_separator(s_writing_system):
	if s_writing_system in ['Arab', 'Aran']:
		if '⁏' in s_line:
			return '⁏ '
		else:
			return '؛ '
	elif s_writing_system == 'Armn':
		return '․ '
	elif s_writing_system == 'Bamu':
		return '꛶ '
	elif s_writing_system in ['Bopo', 'Hani', 'Hans', 'Hant', 'Jpan']:
		return '；'
	elif s_writing_system == 'Grek':
		return '· '
	elif s_writing_system == 'Ethi':
		return '፤ '
	elif s_writing_system == 'Sgnw':
		return '𝪉'
	else:
		return '; '

top_path = Path.cwd()
top_path.joinpath(s_export_directory).mkdir(exist_ok=True)
for s_file_path in glob(f'{top_path}/**/*.tsv', recursive=True):
	s_file_text = Path(s_file_path).read_text()
	ls_text_in_line = s_file_text.splitlines()
	s_header = '|' + ls_text_in_line.pop(0).replace('\t', '|') + '|\n|' + '-|'*(ls_text_in_line[0].count('\t')+1) + '\n'

	s_file_text = s_header
	if s_file_path.endswith('_.tsv'):
		for s_line in ls_text_in_line:
			s_file_text += '|' + s_line.replace('\t', '|') + '|\n'
	else:
		for s_line in ls_text_in_line:
			ls_line = s_line.split('\t')
			if ls_line[0] != s_anchor_locale or ls_line[-1] == '':
				s_file_text += '|' + s_line.replace('\t', '|') + '|\n'
				continue

			s_writing_system = ls_line[0].split('-')[1]
			s_prerequisite_separator = s_get_item_separator(s_writing_system)

			s_prerequisite = ls_line[-1]
			ls_prerequisite = s_prerequisite.split(s_prerequisite_separator)
			for i_prerequisite_index in range(len(ls_prerequisite)):
				ls_prerequisite[i_prerequisite_index] = '[[' + ls_prerequisite[i_prerequisite_index] + ']]'
			s_prerequisite_with_bracket = s_prerequisite_separator.join(ls_prerequisite)
			s_file_text += '|' + s_line[:s_line.rfind('\t')].replace('\t', '|') + '|' + s_prerequisite_with_bracket + '|\n'

	s_export_subdirectory = top_path.joinpath(s_export_directory + s_file_path.removeprefix(str(top_path)).removesuffix(s_file_path[s_file_path.rfind('/'):]))
	Path(s_export_subdirectory).mkdir(parents=True, exist_ok=True)
	export_file_path = top_path.joinpath(s_export_directory + s_file_path.removeprefix(str(top_path)).removesuffix('.tsv') + '.md')
	export_file_path.write_text(s_file_text)
