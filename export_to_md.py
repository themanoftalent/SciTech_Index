from glob import glob
from pathlib import Path


s_export_directory = 'Markdown'

top_path = Path.cwd()
top_path.joinpath(s_export_directory).mkdir(exist_ok=True)
for s_file_path in glob(f'{top_path}/**/*.tsv', recursive=True):
	s_file_text = Path(s_file_path).read_text()
	ls_text_in_line = s_file_text.splitlines()
	s_header = '|' + ls_text_in_line.pop(0).replace('\t', '|') + '|\n|' + '-|'*(ls_text_in_line[0].count('\t')+1) + '\n'

	s_file_text = s_header
	for s_line in ls_text_in_line:
		s_file_text += '|' + s_line.replace('\t', '|') + '|\n'

	s_export_subdirectory = top_path.joinpath(s_export_directory + s_file_path.removeprefix(str(top_path)).removesuffix(s_file_path[s_file_path.rfind('/'):]))
	Path(s_export_subdirectory).mkdir(parents=True, exist_ok=True)
	export_file_path = top_path.joinpath(s_export_directory + s_file_path.removeprefix(str(top_path)).removesuffix('.tsv') + '.md')
	export_file_path.write_text(s_file_text)
